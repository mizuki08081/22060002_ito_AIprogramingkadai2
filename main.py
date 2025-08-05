import streamlit as st
from logic import get_holidays, check_holiday

st.title("📅 祝日判定アプリ")

# ユーザーから日付入力を受け取る
date_input = st.date_input("調べたい日付を選んでください")

holidays = get_holidays()

date_str = date_input.isoformat()

# ボタンを押したら判定
if st.button("祝日か調べる"):
    holiday_name = check_holiday(date_str, holidays)
    if holiday_name:
        st.success(f"{date_str} は祝日です： {holiday_name}")
    else:
        st.info(f"{date_str} は祝日ではありません。")
