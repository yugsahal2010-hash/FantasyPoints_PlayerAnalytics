# Expected Fantasy Points API

## Objective
Estimate a player's expected fantasy points using recent raw match data. Recent performances are weighted more heavily using exponential decay, and expected batting, bowling, and fielding contributions are adjusted based on player role.

## Scientific Principle
Exponentially Weighted Expected Value:

E[X] = Σ(wᵢXᵢ) / Σ(wᵢ)

Recent matches get higher weight using decay = 0.85.

Role-based weighting adjusts expected fantasy contributions for batters, bowlers, and all-rounders.

## Inputs
- player_id: string
- player_name: string
- role: batter | bowler | all_rounder
- matches: list of match performances

Each match includes:
- runs
- wickets
- catches

## Outputs
- expected_fantasy_points
- selection_rating
- derived_metrics
- interpretation

## Run
uvicorn main:app --reload
