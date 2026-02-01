from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, HTMLResponse, FileResponse
from PIL import Image
import io
import os
import httpx
import base64
import urllib.parse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment
POLLINATION_API_KEY = os.getenv("POLLINATION_API_KEY")
if not POLLINATION_API_KEY:
    print("WARNING: POLLINATION_API_KEY not set. Background removal will fail.")

# Background removal prompt for Pollinations AI
BACKGROUND_REMOVAL_PROMPT = "remove background, isolated subject, transparent background, cutout"

app = FastAPI(
    title="Background Remover API",
    description="A simple and effective API for removing backgrounds from images using Pollinations AI",
    version="2.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the web UI"""
    try:
        # Try to read from static directory
        static_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "index.html")
        if os.path.exists(static_path):
            with open(static_path, "r") as f:
                return f.read()
        # Fallback for Vercel deployment
        return """
        <html>
            <body>
                <h1>Background Remover API</h1>
                <p>API is running. Use POST /api/remove-background to remove backgrounds from images.</p>
                <p>Documentation available at <a href="/docs">/docs</a></p>
            </body>
        </html>
        """
    except Exception as e:
        print(f"Error serving root: {str(e)}")
        return """
        <html>
            <body>
                <h1>Background Remover API</h1>
                <p>API is running. Use POST /api/remove-background to remove backgrounds from images.</p>
                <p>Documentation available at <a href="/docs">/docs</a></p>
            </body>
        </html>
        """


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "background-remover"}


@app.post("/api/remove-background")
async def remove_background(file: UploadFile = File(...)):
    """
    Remove background from an uploaded image using Pollinations AI
    
    Args:
        file: Image file (PNG, JPG, JPEG)
        
    Returns:
        PNG image with transparent background
        
    Note:
        Processing may take up to 60 seconds for AI-based background removal
    """
    # Check if API key is configured
    if not POLLINATION_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="API key not configured. Please set POLLINATION_API_KEY environment variable."
        )
    
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="File must be an image (PNG, JPG, JPEG)"
        )
    
    try:
        # Read the uploaded image
        contents = await file.read()
        
        # Prepare the image for Pollinations AI
        # Convert image to base64 for sending as data URI
        image_base64 = base64.b64encode(contents).decode('utf-8')
        data_uri = f"data:{file.content_type};base64,{image_base64}"
        
        # Call Pollinations AI API for background removal using kontext model
        # Use the /image endpoint with kontext model and data URI
        async with httpx.AsyncClient(timeout=60.0) as client:
            # Construct the API URL with prompt and parameters
            api_url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote(BACKGROUND_REMOVAL_PROMPT)}"
            params = {
                "model": "kontext",
                "image": data_uri,  # Pass data URI as parameter
                "nologo": "true"
            }
            
            response = await client.get(
                api_url,
                params=params,
                headers={
                    "Authorization": f"Bearer {POLLINATION_API_KEY}"
                }
            )
            
            if response.status_code != 200:
                error_detail = response.text
                if response.status_code == 401:
                    error_detail = "Invalid API key. Please check your POLLINATION_API_KEY."
                elif response.status_code == 402:
                    error_detail = "API quota exceeded. Please check your Pollinations AI balance."
                elif response.status_code == 400:
                    error_detail = "Invalid image format or size."
                
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"Pollinations AI API error: {error_detail}"
                )
            
            # Get the processed image directly from response
            output_buffer = io.BytesIO(response.content)
            output_buffer.seek(0)
        
        # Generate output filename
        if file.filename and '.' in file.filename:
            base_name = file.filename.rsplit('.', 1)[0]
        else:
            base_name = file.filename or "image"
        
        # Return the processed image
        return StreamingResponse(
            output_buffer,
            media_type="image/png",
            headers={
                "Content-Disposition": f"attachment; filename=no-bg-{base_name}.png"
            }
        )
        
    except httpx.TimeoutException:
        raise HTTPException(
            status_code=504,
            detail="Request timeout. The image might be too large or the service is slow."
        )
    except httpx.RequestError as e:
        # Log the error for debugging
        print(f"Failed to connect to Pollinations AI API: {str(e)}")
        raise HTTPException(
            status_code=503,
            detail="Failed to connect to the image processing service. Please try again later."
        )
    except Exception as e:
        # Log the error for debugging
        print(f"Error processing image: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Error processing image. Please try again or contact support."
        )


@app.get("/api/docs")
async def api_documentation():
    """API documentation"""
    return {
        "endpoints": [
            {
                "path": "/",
                "method": "GET",
                "description": "Web UI for background removal"
            },
            {
                "path": "/health",
                "method": "GET",
                "description": "Health check endpoint"
            },
            {
                "path": "/api/remove-background",
                "method": "POST",
                "description": "Remove background from an image",
                "parameters": {
                    "file": "Image file (multipart/form-data)"
                },
                "response": "PNG image with transparent background"
            }
        ]
    }


# Vercel serverless function handler
handler = app
