from fastapi import APIRouter

from app.models.schemas import (
    BioControlRequest,
    PathPlanRequest,
    PestDetectionRequest,
    SprayPlanRequest,
    WeatherSoilInput,
    YieldPredictionRequest,
)
from app.services.bio_control import recommend_bio_control
from app.services.iot_fusion import fuse_weather_soil
from app.services.pest_detection import detect_pest
from app.services.robotics import plan_path
from app.services.spray_planner import optimize_spray
from app.services.yield_prediction import predict_yield

router = APIRouter(prefix="/api", tags=["agri-ai"])


@router.post("/detect-pest")
def detect_pest_route(req: PestDetectionRequest) -> dict:
    result = detect_pest(req)
    return result.model_dump()


@router.post("/bio-control")
def bio_control_route(req: BioControlRequest) -> dict:
    return recommend_bio_control(req)


@router.post("/spray-plan")
def spray_plan_route(req: SprayPlanRequest) -> dict:
    return optimize_spray(req)


@router.post("/iot-fusion")
def iot_fusion_route(req: WeatherSoilInput) -> dict:
    return fuse_weather_soil(req)


@router.post("/robot-path")
def robot_path_route(req: PathPlanRequest) -> dict:
    return plan_path(req)


@router.post("/yield-prediction")
def yield_prediction_route(req: YieldPredictionRequest) -> dict:
    return predict_yield(req)
