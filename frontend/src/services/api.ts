const API_BASE = "http://localhost:8000/api";

async function callApi(path: string, payload: unknown) {
  const res = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  if (!res.ok) {
    throw new Error(`API error: ${res.status}`);
  }
  return res.json();
}

export const api = {
  detectPest: () => callApi("/detect-pest", { image_id: "img-01", crop: "rice", region: "delta" }),
  bioControl: () => callApi("/bio-control", { crop: "rice", pest_type: "brown_planthopper", severity: 0.7 }),
  sprayPlan: () =>
    callApi("/spray-plan", {
      farm_id: "farm-001",
      patches: [
        { id: "p1", crop: "rice", pest_pressure: 0.82, soil_moisture: 0.44 },
        { id: "p2", crop: "rice", pest_pressure: 0.28, soil_moisture: 0.57 },
        { id: "p3", crop: "rice", pest_pressure: 0.69, soil_moisture: 0.51 },
      ],
    }),
  iotFusion: () => callApi("/iot-fusion", { temperature_c: 31, humidity: 0.74, rainfall_mm: 1.2, wind_kph: 11, soil_ph: 6.4, nitrogen_ppm: 55 }),
  robotPath: () => callApi("/robot-path", { rows: 8, cols: 8, start: [0, 0], goal: [7, 7], blocked: [[1, 1], [2, 1], [3, 1], [4, 4], [5, 4]] }),
  yieldPrediction: () => callApi("/yield-prediction", { crop: "rice", acres: 12, weather_index: 0.72, pest_risk_index: 0.3, soil_health_index: 0.68, bio_control_adoption: 0.85 }),
};
