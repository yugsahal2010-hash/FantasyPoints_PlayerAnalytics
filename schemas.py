from pydantic import BaseModel, Field
from typing import List
from enum import Enum

class PlayerRole(str, Enum):
    batter = "batter"
    bowler = "bowler"
    all_rounder = "all_rounder"

class MatchPerformance(BaseModel):
    runs: float
    wickets: float
    catches: float

class FantasyPointsRequest(BaseModel):
    player_id: str
    player_name: str
    role: PlayerRole = Field(
        ...,
        description="Player role: batter, bowler, or all_rounder"
    )
    matches: List[MatchPerformance]

    batting_points_per_run: float = 1.0
    bowling_points_per_wicket: float = 25.0
    fielding_points_per_catch: float = 8.0


class DerivedMetrics(BaseModel):
    expected_runs: float
    expected_wickets: float
    expected_catches: float

    batting_points: float
    bowling_points: float
    fielding_points: float

    weighted_batting_points: float
    weighted_bowling_points: float
    weighted_fielding_points: float


class FantasyPointsResponse(BaseModel):
    player_id: str
    player_name: str
    role: PlayerRole

    expected_fantasy_points: float
    selection_rating: str

    derived_metrics: DerivedMetrics
    interpretation: str
