from datetime import time
from config.mealtime_config import MealTimeConfig

# restaurants.json 데이터를 MealTimeConfig 객체로 변환
def parse_time_range(ranges: dict) -> MealTimeConfig:

    # 문자열 "HH:MM"을 datetime.time 객체로 변환
    # ex. "07:30" -> time(7, 30)
    def parse(t): return time.fromisoformat(t)

    breakfast = tuple(map(parse, ranges.get("breakfast", ["00:00", "00:00"])))
    lunch = tuple(map(parse, ranges.get("lunch", ["00:00", "00:00"])))
    dinner = tuple(map(parse, ranges.get("dinner", ["00:00", "00:00"])))

    return MealTimeConfig(breakfast, lunch, dinner)
