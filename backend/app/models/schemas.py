from pydantic import BaseModel, Field


class FarmPatch(BaseModel):
    id: str
    crop: str
    pest_pressure: float = Field(ge=0.0, le=1.0)
    soil_moisture: float = Field(ge=0.0, le=1.0)


class PestDetectionRequest(BaseModel):
    image_id: str
    crop: str
    region: str


class PestDetectionResponse(BaseModel):
    image_id: str
    pest_type: str
    severity: float
    confidence: float


class BioControlRequest(BaseModel):
    crop: str
    pest_type: str
    severity: float = Field(ge=0.0, le=1.0)


class SprayPlanRequest(BaseModel):
    farm_id: str
    patches: list[FarmPatch]


class WeatherSoilInput(BaseModel):
    temperature_c: float
    humidity: float = Field(ge=0.0, le=1.0)
    rainfall_mm: float
    wind_kph: float
    soil_ph: float
    nitrogen_ppm: float


class PathPlanRequest(BaseModel):
    rows: int = Field(gt=1, le=100)
    cols: int = Field(gt=1, le=100)
    start: tuple[int, int]
    goal: tuple[int, int]
    blocked: list[tuple[int, int]]


class YieldPredictionRequest(BaseModel):
    crop: str
    acres: float = Field(gt=0)
    weather_index: float = Field(ge=0.0, le=1.0)
    pest_risk_index: float = Field(ge=0.0, le=1.0)
    soil_health_index: float = Field(ge=0.0, le=1.0)
    bio_control_adoption: float = Field(ge=0.0, le=1.0)
