import json
from datetime import datetime

from config.mealtime_config import MealTimeConfig
from core.account import Account
from core.company import Company
from core.menu import Menu
from core.restaurant import Restaurant
from utils.parse_time_range import parse_time_range


def load_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)

class MainService:
    def __init__(self):
        self.accounts = []
        self.restaurants = []
        self.mealtime_config = MealTimeConfig()

    def load_data(self):
        account_data = load_json('data/accounts.json')
        company_dict = {}  # 회사별 객체 재사용

        for acc in account_data:
            company_name = acc["company"]
            if company_name not in company_dict:
                company_dict[company_name] = Company(company_name)
            account = Account(acc["userId"], acc["name"], company_dict[company_name])
            self.accounts.append(account)

        restaurant_data = load_json('data/restaurants.json')
        for res in restaurant_data:
            menus = [Menu(m["name"], m["price"]) for m in res["menus"]]
            meal_time_config = parse_time_range(res["mealTimeRanges"])
            restaurant = Restaurant(res["code"], res["name"], menus, meal_time_config)
            self.restaurants.append(restaurant)

    def find_account(self, user_id):
        for acc in self.accounts:
            if acc.userId == user_id:
                return acc
        return None

    def start(self):
        self.load_data()

        user_id = input("사용자 아이디를 입력하세요: ")
        account = self.find_account(user_id)
        if not account:
            print("존재하지 않는 사용자입니다.")
            return

        now = datetime.now()
        # meal_type = self.mealtime_config.get_current_meal_type(now)
        # if meal_type != 'none':
        #     print(f"\n[{account.name}]님의 {meal_type} 식사입니다.\n")
        # else:
        #     print(f"\n{account.name}님 안녕하세요.")

        available_restaurants = [
            r for r in self.restaurants if r.supports_meal(now)
        ]

        if not available_restaurants:
            print(f"현재 시각({now.strftime('%H:%M')})에는 운영 중인 식당이 없습니다.\n")

            print("📅 식당 운영 시간 안내 📅")
            for r in self.restaurants:
                config = r.meal_time_config

                time_noti = []
                if config.breakfast[0] < config.breakfast[1]:
                    time_noti.append(f"아침 {config.breakfast[0].strftime('%H:%M')}~{config.breakfast[1].strftime('%H:%M')}")
                if config.lunch[0] < config.lunch[1]:
                    time_noti.append(f"점심 {config.lunch[0].strftime('%H:%M')}~{config.lunch[1].strftime('%H:%M')}")
                if config.dinner[0] < config.dinner[1]:
                    time_noti.append(f"저녁 {config.dinner[0].strftime('%H:%M')}~{config.dinner[1].strftime('%H:%M')}")

                print(f"- {r.name} : {' / '.join(time_noti) if time_noti else '운영 시간 없음'}")
            return

        print("\n이용 가능한 식당 목록:")
        for idx, r in enumerate(available_restaurants):
            print(f"{idx + 1}. {r.name}")

        try:
            choice = int(input(f"\n{account.name}님, 식당을 선택해 주세요 (번호 입력): ")) - 1
            if choice < 0 or choice >= len(available_restaurants):
                print("해당 식당은 없습니다.")
                return
        except ValueError:
            print("숫자만 입력해 주세요.")
            return

        selected_restaurant = available_restaurants[choice]

        if not selected_restaurant.menus:
            print("해당 식당은 메뉴를 제공하지 않습니다.")
            return

        print("\n메뉴 목록:")
        for idx, m in enumerate(selected_restaurant.menus):
            print(f"{idx + 1}. {m.name} - {m.price}원")

        try:
            menu_choice = int(input("메뉴를 선택하세요 (번호 입력): ")) - 1
            if menu_choice < 0 or menu_choice >= len(selected_restaurant.menus):
                print("해당 메뉴는 없습니다.")
                return
        except ValueError:
            print("숫자만 입력해 주세요.")
            return

        selected_menu = selected_restaurant.menus[menu_choice]

        print(f"\n{selected_menu.price}원이 결제되었습니다. 맛있게 드세요!")


# 프로그램 시작
if __name__ == "__main__":
    service = MainService()
    service.start()
