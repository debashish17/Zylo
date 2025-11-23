from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="TescoCreate AI - Creative API",
    description="AI-powered creative generation using LLMs",
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

# Models
class HeadlineRequest(BaseModel):
    product: str
    audience: str
    tone: str
    count: int = 5
    tier: str = "free"  # "free" or "premium"

class CreativeVariantRequest(BaseModel):
    description: str
    count: int = 3
    tier: str = "free"

# Routes
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    has_gemini = bool(os.getenv("GEMINI_API_KEY"))
    has_nvidia = bool(os.getenv("NVIDIA_API_KEY"))

    return {
        "status": "ok",
        "service": "creative-api",
        "providers": {
            "gemini": has_gemini,
            "nvidia": has_nvidia
        }
    }

@app.post("/generate/headlines")
async def generate_headlines(request: HeadlineRequest):
    """
    Generate compliant headline options
    Uses Gemini (free) or GPT-4 (premium)
    """
    try:
        if request.tier == "free":
            headlines = await generate_with_gemini(request)
        else:
            headlines = await generate_with_gpt4(request)

        return {
            "headlines": headlines,
            "tier": request.tier,
            "cost": "free" if request.tier == "free" else "premium"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate/variants")
async def generate_variants(request: CreativeVariantRequest):
    """
    Generate creative layout variants
    """
    try:
        # TODO: Implement variant generation
        return {
            "variants": [],
            "count": 0,
            "tier": request.tier
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Helper functions
async def generate_with_gemini(request: HeadlineRequest) -> List[str]:
    """Generate headlines using Gemini (free)"""

    gemini_key = os.getenv("GEMINI_API_KEY")
    if not gemini_key:
        # Return template-based headlines as fallback
        return generate_template_headlines(request)

    try:
        import google.generativeai as genai

        genai.configure(api_key=gemini_key)
        model = genai.GenerativeModel('gemini-2.0-flash-exp')

        prompt = f"""
        You are a retail marketing copywriter for Tesco.

        Generate {request.count} compelling headlines for:
        - Product: {request.product}
        - Target Audience: {request.audience}
        - Tone: {request.tone}

        STRICT RULES:
        - NO asterisks or T&Cs
        - NO competition language (win, prize, enter)
        - NO sustainability claims (eco, green, sustainable)
        - NO money-back guarantees
        - Keep under 50 characters

        Format: Return only the headlines, one per line.
        """

        response = model.generate_content(prompt)
        headlines = [line.strip() for line in response.text.strip().split('\n') if line.strip()]

        return headlines[:request.count]

    except Exception as e:
        print(f"Gemini error: {e}")
        return generate_template_headlines(request)

async def generate_with_gpt4(request: HeadlineRequest) -> List[str]:
    """Generate headlines using GPT-4 (premium)"""
    # TODO: Implement GPT-4 generation
    return generate_template_headlines(request)

def generate_template_headlines(request: HeadlineRequest) -> List[str]:
    """Fallback: Template-based headline generation"""
    templates = [
        f"Discover {request.product}",
        f"{request.product} Your {request.audience} Will Love",
        f"Try Our Premium {request.product}",
        f"Delicious {request.product} Available Now",
        f"Experience {request.product} Today",
    ]
    return templates[:request.count]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
