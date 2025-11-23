from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Zylo - Compliance API",
    description="Real-time compliance validation for retail media creatives",
    version="0.1.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class ComplianceRequest(BaseModel):
    creative_data: Dict[str, Any]
    format: str

class Violation(BaseModel):
    type: str
    severity: str  # "critical" | "warning"
    message: str
    confidence: float
    element: Optional[Dict[str, Any]] = None
    suggestion: Optional[str] = None

class ComplianceResponse(BaseModel):
    score: int  # 0-100
    violations: List[Violation]
    warnings: List[Violation]
    passed: bool

# Routes
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "service": "compliance-api"}

@app.post("/validate/full", response_model=ComplianceResponse)
async def validate_full(request: ComplianceRequest):
    """
    Comprehensive compliance validation
    Validates visual elements, copy, and accessibility
    """
    violations = []
    warnings = []

    # TODO: Implement actual validation logic
    # For now, return mock data

    score = 100 - (len(violations) * 10) - (len(warnings) * 5)
    score = max(0, min(100, score))

    return ComplianceResponse(
        score=score,
        violations=violations,
        warnings=warnings,
        passed=len(violations) == 0
    )

@app.post("/validate/copy")
async def validate_copy(text: str):
    """
    NLP-powered copy compliance validation
    Detects prohibited content: T&Cs, competitions, claims, etc.
    """
    # TODO: Implement NLP validation
    return {
        "violations": [],
        "confidence": 1.0,
        "text": text
    }

@app.post("/validate/visual")
async def validate_visual(creative_data: Dict[str, Any]):
    """
    Visual compliance validation
    Checks layout, spacing, sizes, positioning
    """
    # TODO: Implement visual validation
    return {
        "violations": [],
        "layout_score": 100
    }

@app.post("/validate/accessibility")
async def validate_accessibility(creative_data: Dict[str, Any]):
    """
    Accessibility compliance (WCAG AA)
    Checks contrast ratios, font sizes, etc.
    """
    # TODO: Implement accessibility checks
    return {
        "violations": [],
        "wcag_aa_compliant": True
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
