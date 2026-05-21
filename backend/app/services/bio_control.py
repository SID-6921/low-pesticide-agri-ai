from app.models.schemas import BioControlRequest


BIO_LIBRARY = {
    "brown_planthopper": {
        "agent": "Anagrus spp.",
        "bio_pesticide": "Beauveria bassiana",
    },
    "bollworm": {
        "agent": "Trichogramma chilonis",
        "bio_pesticide": "Bacillus thuringiensis",
    },
    "leafminer": {
        "agent": "Diglyphus isaea",
        "bio_pesticide": "Neem extract",
    },
    "aphid": {
        "agent": "Ladybird beetles",
        "bio_pesticide": "Metarhizium anisopliae",
    },
}


def recommend_bio_control(req: BioControlRequest) -> dict:
    item = BIO_LIBRARY.get(
        req.pest_type,
        {"agent": "General predator mix", "bio_pesticide": "Neem extract"},
    )
    spray_reduction_target = min(0.9, 0.4 + req.severity * 0.6)
    return {
        "crop": req.crop,
        "pest_type": req.pest_type,
        "biological_agent": item["agent"],
        "bio_pesticide": item["bio_pesticide"],
        "estimated_pesticide_reduction": round(spray_reduction_target, 2),
        "notes": "Use threshold-based intervention and release beneficials at dusk.",
    }
