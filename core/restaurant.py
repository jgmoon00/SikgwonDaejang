from datetime import datetime
from typing import List

from config.mealtime_config import MealTimeConfig
from core.menu import Menu

class Restaurant:
    def __init__(self, code: str, name: str, menus: List["Menu"], meal_time_config: MealTimeConfig):
        self.code = code
        self.name = name
        self.menus = menus
        self.meal_time_config = meal_time_config

    def supports_meal(self, now: datetime) -> bool:
        return self.meal_time_config.get_current_meal_type(now) != "none"

    def get_current_meal_type(self, now: datetime) -> str:
        return self.meal_time_config.get_current_meal_type(now)
