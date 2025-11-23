from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from PIL import Image
import io
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Zylo - Image API",
    description="AI-powered image processing for creative assets",
    version="0.1.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "ok",
        "service": "image-api",
        "gpu_available": False,  # Will check torch.cuda.is_available() later
    }

@app.post("/remove-background")
async def remove_background(
    file: UploadFile = File(...),
    method: str = Form(default="auto")
):
    """
    Remove background from image
    Methods: auto, fast (U2-Net), quality (BiRefNet)
    """
    try:
        # Read image
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))

        # TODO: Implement actual background removal with REMBG
        # For now, return original image
        output = image

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        output.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        return StreamingResponse(img_byte_arr, media_type="image/png")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/smart-crop")
async def smart_crop(
    file: UploadFile = File(...),
    width: int = Form(default=1080),
    height: int = Form(default=1080)
):
    """
    Content-aware cropping
    Identifies focal points and crops intelligently
    """
    try:
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))

        # TODO: Implement smart cropping with CLIP/DETR
        # For now, center crop
        output = image.resize((width, height), Image.Resampling.LANCZOS)

        img_byte_arr = io.BytesIO()
        output.save(img_byte_arr, format='JPEG', quality=95)
        img_byte_arr.seek(0)

        return StreamingResponse(img_byte_arr, media_type="image/jpeg")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    """
    Analyze image content using CLIP
    Returns: detected objects, colors, style
    """
    try:
        # TODO: Implement CLIP analysis
        return {
            "categories": [],
            "dominant_colors": [],
            "style": "unknown"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/extract-colors")
async def extract_colors(
    file: UploadFile = File(...),
    count: int = Form(default=5)
):
    """
    Extract dominant colors from image
    """
    try:
        from colorthief import ColorThief
        import tempfile

        # Save to temporary file (ColorThief needs file path)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        # Extract colors
        color_thief = ColorThief(tmp_path)
        palette = color_thief.get_palette(color_count=count, quality=1)

        # Convert RGB tuples to hex
        hex_colors = ['#{:02x}{:02x}{:02x}'.format(r, g, b) for r, g, b in palette]

        # Cleanup
        os.unlink(tmp_path)

        return {
            "colors": hex_colors,
            "count": len(hex_colors)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
