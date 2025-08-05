import requests

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

def check_holiday(date_str, holidays):
    """
    日付文字列（'YYYY-MM-DD'）が祝日かどうか判定し、
    祝日名を返す。祝日でなければ空文字。
    """
    return holidays.get(date_str, "")
