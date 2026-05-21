from app.models.schemas import PestDetectionRequest, PestDetectionResponse


PEST_BY_CROP = {
    "rice": "brown_planthopper",
    "cotton": "bollworm",
    "tomato": "leafminer",
    "wheat": "aphid",
}


def detect_pest(req: PestDetectionRequest) -> PestDetectionResponse:
    pest = PEST_BY_CROP.get(req.crop.lower(), "unknown_pest")
    confidence = 0.78 if pest != "unknown_pest" else 0.52
    severity = 0.64 if pest != "unknown_pest" else 0.35
    return PestDetectionResponse(
        image_id=req.image_id,
        pest_type=pest,
        severity=severity,
        confidence=confidence,
    )
