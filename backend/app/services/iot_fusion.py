from app.models.schemas import WeatherSoilInput


def fuse_weather_soil(data: WeatherSoilInput) -> dict:
    stress = (
        abs(data.temperature_c - 26) / 20
        + data.humidity * 0.2
        + min(data.wind_kph / 40, 1.0) * 0.2
        + max((7.5 - data.soil_ph) / 3.5, 0.0) * 0.2
        + max((60 - data.nitrogen_ppm) / 60, 0.0) * 0.2
    )
    stress_index = min(round(stress, 2), 1.0)
    return {
        "stress_index": stress_index,
        "spray_window": "safe" if data.wind_kph < 14 and data.rainfall_mm < 2 else "avoid",
        "advice": "Irrigate lightly and deploy biological controls first." if stress_index > 0.6 else "Maintain current integrated pest management plan.",
    }
