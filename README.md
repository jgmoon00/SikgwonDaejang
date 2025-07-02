# 식권대장

## 소개
법틀에서 사용하는 식권 관리 및 점심 추천 서비스<br>
**식당 메뉴 기반 식권 안내 기능**과 **랜덤 점심 추천 웹사이트** 두 가지 핵심 기능을 제공합니다.

현재 `랜덤 점심 추천 웹사이트`사이트는 GitHub Pages로 공개되어 있습니다:  
[**점심 정하러 가기 →**](https://jgmoon00.github.io/SikgwonDaejang/)

---

## 핵심 기능

| 구분 | 기능 | 설명 |
|---|------|------|
| 1️ | **식권 정보 안내** | 사용자별로 이용 가능한 식당, 메뉴, 금액 정보를 제공하는 콘솔 기반 서비스 (`main.py`) |
| 2 | **점심 뽑기 웹사이트** | 점심 식당을 랜덤으로 추천 |

---

## 기능 상세

### 1. 식권 정보 안내 (콘솔 기반)

- 로그인 방식: `accounts.json`에 등록된 사용자명 입력
- 제공 정보: 사용자의 이용 가능한 식당 / 메뉴 / 가격 정보
- 실행 방법:
  ```bash
  python main.py
  
### 2. 점심 뽑기 웹사이트
- `뽑기` 버튼 클릭 시 랜덤 식당 이름이 화면에 표시됩니다.

![Image](https://github.com/user-attachments/assets/2e1a6554-85ad-4bcb-af8e-e33ed0363daf)

---

## 파일 구조
```
SikgwonDaejang/
├── config/
│   └── mealtime_config.py       # 식사 시간 범위를 설정하는 설정 파일
│
├── core/                        # 핵심 도메인 로직을 담당하는 모듈
│   ├── account.py               
│   ├── company.py               
│   ├── menu.py                  
│   └── restaurant.py            
│
├── data/                        # JSON 데이터 저장소
│   ├── accounts.json            # 사용자 계정 정보 (로그인용)
│   └── restaurants.json         # 식당 및 메뉴 정보
│
├── docs/                        # 정적 웹사이트 (GitHub Pages용)
│   ├── index.html               # 점심 식당 뽑기 메인 페이지
│   ├── script.js                # 뽑기 기능 로직이 포함된 JavaScript
│   ├── style.css                # 웹사이트 스타일 정의
│   └── data/                    # 웹에서 사용하는 JSON 등 정적 데이터 디렉토리
│
├── utils/                       # 공통 유틸 함수 모음
│   ├── parse_time_range.py      # 시간 문자열을 파싱
│   └── time_util.py             # 시간 관련 유틸 (현재 시간)
│
└── main.py                      # 콘솔 앱 실행 (유저 → 식당 → 메뉴 추천 기능)
```

---

## 기여 방법(How to Contribute)

### 1. 랜덤 추천용 식당 추가
- `random_restaurants.json` 파일을 수정하여 새로운 맛집을 추가하거나 잘못된 정보를 정정해 주세요.
- 없어진 식당도 제보해 주세요.
```
// random_restaurants.json
[
  {
    "id": 1,
    "name": "1's 카츠곳간",
    "category": "일식"
  },
  {
    "id": 2,
    "name": "24시전주명가콩나물국밥",
    "category": "한식"
  }
]
  
```

### 2. 사용자 및 메뉴 정보 추가
- `accounts.json` 또는 `restaurants.json` 파일을 수정하여 유저/식당/메뉴 데이터를 수정해 주세요.
- json 형식을 유지해 주세요.

---
