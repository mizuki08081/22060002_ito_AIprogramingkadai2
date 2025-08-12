import requests
from datetime import datetime, timedelta

# API取得
def get_holidays():
    url = "https://holidays-jp.github.io/api/v1/date.json"
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        else:
            return {}
    except:
        return {}

# 日付が祝日か判定
def check_holiday(date_str, holidays):
    return holidays.get(date_str, "")

# 指定日からdays_ahead日以内の祝日一覧
def get_upcoming_holidays(holidays, start_date=None, days_ahead=30):
    if start_date is None:
        start_date = datetime.today().date()
    end_date = start_date + timedelta(days=days_ahead)

    result = []
    for date_str, name in holidays.items():
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
        if start_date <= date_obj <= end_date:
            result.append((date_obj, name))
    return sorted(result, key=lambda x: x[0])

# 指定日以降で一番近い祝日
def get_next_holiday(holidays, start_date=None):
    if start_date is None:
        start_date = datetime.today().date()

    future_holidays = [
        (datetime.strptime(d, "%Y-%m-%d").date(), name)
        for d, name in holidays.items()
        if datetime.strptime(d, "%Y-%m-%d").date() >= start_date
    ]
    if not future_holidays:
        return None
    return min(future_holidays, key=lambda x: x[0])
