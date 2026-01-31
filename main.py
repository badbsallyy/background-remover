from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from rembg import remove
from PIL import Image
import io
import os

app = FastAPI(
    title="Background Remover API",
    description="A simple and effective API for removing backgrounds from images",
    version="1.0.0"
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
    Remove background from an uploaded image
    
    Args:
        file: Image file (PNG, JPG, JPEG)
        
    Returns:
        PNG image with transparent background
    """
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="File must be an image (PNG, JPG, JPEG)"
        )
    
    try:
        # Read the uploaded image
        contents = await file.read()
        input_image = Image.open(io.BytesIO(contents))
        
        # Remove background
        output_image = remove(input_image)
        
        # Convert to bytes
        output_buffer = io.BytesIO()
        output_image.save(output_buffer, format="PNG")
        output_buffer.seek(0)
        
        # Return the processed image
        return StreamingResponse(
            output_buffer,
            media_type="image/png",
            headers={
                "Content-Disposition": f"attachment; filename=no-bg-{file.filename.rsplit('.', 1)[0]}.png"
            }
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing image: {str(e)}"
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
