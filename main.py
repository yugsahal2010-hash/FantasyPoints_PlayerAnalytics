from fastapi import FastAPI, HTTPException
from schemas import FantasyPointsRequest, FantasyPointsResponse
from services import compute_expected_fantasy_points

app = FastAPI(title="Expected Fantasy Points API", version="1.0")

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/api/v1/expected-fantasy-points", response_model=FantasyPointsResponse)
def expected_fantasy_points(payload: FantasyPointsRequest):
    try:
        return compute_expected_fantasy_points(payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
