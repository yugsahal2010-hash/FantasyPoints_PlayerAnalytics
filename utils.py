def weighted_average(values, decay=0.85):
    n = len(values)
    weights = [decay ** (n - i - 1) for i in range(n)]
    total_weight = sum(weights)
    return sum(v * w for v, w in zip(values, weights)) / total_weight


def classify_selection(points):
    if points >= 80:
        return "Elite"
    elif points >= 55:
        return "Strong"
    elif points >= 35:
        return "Average"
    elif points >= 20:
        return "Below Average"
    return "Poor"


def get_role_weights(role):
    role_weights = {
        "batter": (1.0, 0.2, 0.3),
        "bowler": (0.4, 1.0, 0.3),
        "all_rounder": (1.0, 1.0, 0.5)
    }
    return role_weights[role]
