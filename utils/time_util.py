from datetime import datetime

# ex. now: 2025-06-30 16:58:26.502894
# ex. now_format: 1658
def get_hour_min() -> int:
    now = datetime.now()
    now_format = now.hour * 100 + now.minute
    return now_format
