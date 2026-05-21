from app.models.schemas import SprayPlanRequest


def optimize_spray(req: SprayPlanRequest) -> dict:
    high_risk = [p for p in req.patches if p.pest_pressure >= 0.6]
    low_risk = [p for p in req.patches if p.pest_pressure < 0.6]

    targeted_area_ratio = len(high_risk) / max(1, len(req.patches))
    estimated_reduction = round((1.0 - targeted_area_ratio) * 0.9, 2)

    return {
        "farm_id": req.farm_id,
        "target_patch_ids": [p.id for p in high_risk],
        "skip_patch_ids": [p.id for p in low_risk],
        "targeted_area_ratio": round(targeted_area_ratio, 2),
        "estimated_pesticide_reduction": estimated_reduction,
    }
