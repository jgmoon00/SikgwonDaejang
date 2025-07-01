from datetime import time
from config.mealtime_config import MealTimeConfig

def parse_time_range(ranges: dict) -> MealTimeConfig:
    def parse(t): return time.fromisoformat(t)

    breakfast = tuple(map(parse, ranges.get("breakfast", ["00:00", "00:00"])))
    lunch = tuple(map(parse, ranges.get("lunch", ["00:00", "00:00"])))
    dinner = tuple(map(parse, ranges.get("dinner", ["00:00", "00:00"])))

    return MealTimeConfig(breakfast, lunch, dinner)
