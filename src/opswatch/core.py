from collections.abc import Mapping


def status(metrics: Mapping[str, float], thresholds: Mapping[str, float]) -> dict[str, str]:
    """Classify metrics as ok or alert using explicit thresholds."""
    result: dict[str, str] = {}
    for name, value in metrics.items():
        if name not in thresholds:
            result[str(name)] = "unknown"
            continue
        result[str(name)] = "alert" if float(value) >= float(thresholds[name]) else "ok"
    return dict(sorted(result.items()))
