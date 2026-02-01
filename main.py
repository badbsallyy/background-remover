from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image
import io
import os
import httpx
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment
CLIPDROP_API_KEY = os.getenv("CLIPDROP_API_KEY")
if not CLIPDROP_API_KEY:
    print("WARNING: CLIPDROP_API_KEY not set. Background removal will fail.")

app = FastAPI(
    title="Background Remover API",
    description="A simple and effective API for removing backgrounds from images using Clipdrop API",
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

# Serve static files
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the web UI"""
    try:
        with open("static/index.html", "r") as f:
            return f.read()
    except FileNotFoundError:
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
    Remove background from an uploaded image using Clipdrop API
    
    Args:
        file: Image file (PNG, JPG, JPEG)
        
    Returns:
        PNG image with transparent background
    """
    # Check if API key is configured
    if not CLIPDROP_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="API key not configured. Please set CLIPDROP_API_KEY environment variable."
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
        
        # Call Clipdrop API for background removal
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                "https://clipdrop-api.co/remove-background/v1",
                files={
                    "image_file": (file.filename, contents, file.content_type)
                },
                headers={
                    "x-api-key": CLIPDROP_API_KEY
                }
            )
            
            if response.status_code != 200:
                error_detail = response.text
                if response.status_code == 401:
                    error_detail = "Invalid API key. Please check your CLIPDROP_API_KEY."
                elif response.status_code == 402:
                    error_detail = "API quota exceeded. Please upgrade your Clipdrop plan."
                elif response.status_code == 400:
                    error_detail = "Invalid image format or size."
                
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"Clipdrop API error: {error_detail}"
                )
            
            # Get the processed image
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
        raise HTTPException(
            status_code=503,
            detail=f"Failed to connect to Clipdrop API: {str(e)}"
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


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
