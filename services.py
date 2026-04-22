from schemas import FantasyPointsRequest, FantasyPointsResponse, DerivedMetrics
from utils import weighted_average, classify_selection, get_role_weights

def compute_expected_fantasy_points(payload: FantasyPointsRequest) -> FantasyPointsResponse:
    if len(payload.matches) == 0:
        raise ValueError("At least one match is required")

    runs_list = [m.runs for m in payload.matches]
    wickets_list = [m.wickets for m in payload.matches]
    catches_list = [m.catches for m in payload.matches]

    expected_runs = weighted_average(runs_list)
    expected_wickets = weighted_average(wickets_list)
    expected_catches = weighted_average(catches_list)

    batting_points = expected_runs * payload.batting_points_per_run
    bowling_points = expected_wickets * payload.bowling_points_per_wicket
    fielding_points = expected_catches * payload.fielding_points_per_catch

    bat_w, bowl_w, field_w = get_role_weights(payload.role.value)

    weighted_batting_points = batting_points * bat_w
    weighted_bowling_points = bowling_points * bowl_w
    weighted_fielding_points = fielding_points * field_w

    expected_fantasy_points = (
        weighted_batting_points +
        weighted_bowling_points +
        weighted_fielding_points
    )

    selection_rating = classify_selection(expected_fantasy_points)

    interpretation = (
        f"{payload.player_name} is projected to score "
        f"{round(expected_fantasy_points,2)} fantasy points as a "
        f"{payload.role.value}, rated as {selection_rating.lower()}."
    )

    return FantasyPointsResponse(
        player_id=payload.player_id,
        player_name=payload.player_name,
        role=payload.role,
        expected_fantasy_points=round(expected_fantasy_points, 2),
        selection_rating=selection_rating,
        derived_metrics=DerivedMetrics(
            expected_runs=round(expected_runs, 2),
            expected_wickets=round(expected_wickets, 2),
            expected_catches=round(expected_catches, 2),
            batting_points=round(batting_points, 2),
            bowling_points=round(bowling_points, 2),
            fielding_points=round(fielding_points, 2),
            weighted_batting_points=round(weighted_batting_points, 2),
            weighted_bowling_points=round(weighted_bowling_points, 2),
            weighted_fielding_points=round(weighted_fielding_points, 2),
        ),
        interpretation=interpretation
    )
