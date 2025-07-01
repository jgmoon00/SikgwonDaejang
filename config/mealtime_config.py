from datetime import datetime, time

class MealTimeConfig:
    def __init__(self, breakfast=None, lunch=None, dinner=None):
        self.breakfast = breakfast or (time.min, time.min)
        self.lunch = lunch or (time.min, time.min)
        self.dinner = dinner or (time.min, time.min)

    def get_current_meal_type(self, now: datetime) -> str:
        current = now.time()
        if self.breakfast[0] <= current <= self.breakfast[1]:
            return "아침"
        elif self.lunch[0] <= current <= self.lunch[1]:
            return "점심"
        elif self.dinner[0] <= current <= self.dinner[1]:
            return "저녁"
        return "none"
