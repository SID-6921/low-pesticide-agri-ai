from app.models.schemas import YieldPredictionRequest


BASE_YIELD = {
    "rice": 2.8,
    "wheat": 2.4,
    "cotton": 1.8,
    "tomato": 6.0,
}


def predict_yield(req: YieldPredictionRequest) -> dict:
    base = BASE_YIELD.get(req.crop.lower(), 2.2)
    multiplier = (
        0.35 * req.weather_index
        + 0.35 * req.soil_health_index
        + 0.2 * req.bio_control_adoption
        + 0.1 * (1 - req.pest_risk_index)
    )
    tons_per_acre = round(base * (0.7 + multiplier), 2)
    total_tons = round(tons_per_acre * req.acres, 2)

    return {
        "crop": req.crop,
        "tons_per_acre": tons_per_acre,
        "estimated_total_tons": total_tons,
        "confidence": round(0.65 + 0.25 * req.weather_index, 2),
    }
