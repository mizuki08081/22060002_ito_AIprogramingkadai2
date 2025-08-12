import streamlit as st
import pandas as pd
from datetime import date
from logic import get_holidays, check_holiday, get_upcoming_holidays, get_next_holiday

st.title("📆祝日判定アプリ")

# 祝日データ取得
holidays = get_holidays()
today = date.today()

# --- 入力フォーム ---
date_input = st.date_input("調べたい日付を選んでください", today)
date_str = date_input.isoformat()

# --- 判定ボタン ---
if st.button("祝日か調べる"):
    holiday_name = check_holiday(date_str, holidays)
    if holiday_name:
        st.success(f"{date_str} は祝日です： {holiday_name}")
    else:
        st.info(f"{date_str} は祝日ではありません。")

st.markdown("---")

# --- ① 次の祝日カウントダウン ---
next_holiday = get_next_holiday(holidays, today)
if next_holiday:
    h_date, h_name = next_holiday
    days_left = (h_date - today).days
    st.subheader("⏳ 次の祝日までのカウントダウン")
    st.success(f"{h_name} まであと {days_left} 日！（{h_date}）")

# 今日基準
st.subheader("🚩３０日以内の祝日") 

upcoming_today = get_upcoming_holidays(holidays, today, 30)
if upcoming_today:
    df_today = pd.DataFrame(upcoming_today, columns=["日付", "祝日名"])
    df_today.index = range(1, len(df_today) + 1)  # 1から始まるインデックス
    st.table(df_today)
else:
    st.write("30日以内に祝日はありません。")

# 入力日基準
upcoming_input = get_upcoming_holidays(holidays, date_input, 30)
if upcoming_input:
    df_input = pd.DataFrame(upcoming_input, columns=["日付", "祝日名"])
    df_input.index = range(1, len(df_input) + 1)  # 1から始まるインデックス
    st.table(df_input)
else:
    st.write(f"{date_str} から30日以内に祝日はありません。")

