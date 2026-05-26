import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# -----------------------------
# 한글 폰트 설정
# -----------------------------
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="날짜별 기온분석",
    layout="wide"
)

st.title("📊 날짜별 기온분석")

# -----------------------------
# 데이터 불러오기
# -----------------------------
df = pd.read_csv("seoul.csv", encoding="cp949")

# 컬럼 이름 공백 제거
df.columns = df.columns.str.strip()

# 날짜 형식 변환
df['날짜'] = pd.to_datetime(df['날짜'], errors='coerce')

# 월 / 일 컬럼 생성
df['월'] = df['날짜'].dt.month
df['일'] = df['날짜'].dt.day
df['연도'] = df['날짜'].dt.year

# -----------------------------
# 사용자 선택
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    selected_month = st.selectbox(
        "월 선택",
        list(range(1, 13))
    )

with col2:
    selected_day = st.selectbox(
        "일 선택",
        list(range(1, 32))
    )

# -----------------------------
# 선택 날짜 데이터 필터링
# -----------------------------
filtered_df = df[
    (df['월'] == selected_month) &
    (df['일'] == selected_day)
]

# 결측치 제거
filtered_df = filtered_df.dropna(
    subset=['최고기온(℃)', '최저기온(℃)']
)

# -----------------------------
# 그래프 출력
# -----------------------------
if len(filtered_df) > 0:

    fig, ax = plt.subplots(figsize=(14, 6))

    # 최고기온 그래프
    ax.plot(
        filtered_df['연도'],
        filtered_df['최고기온(℃)'],
        color='hotpink',
        linewidth=2,
        label='최고기온'
    )

    # 최저기온 그래프
    ax.plot(
        filtered_df['연도'],
        filtered_df['최저기온(℃)'],
        color='lightblue',
        linewidth=2,
        label='최저기온'
    )

    # 제목
    ax.set_title(
        f"{selected_month}월 {selected_day}일 날짜별 기온분석",
        fontsize=18
    )

    # 축 이름
    ax.set_xlabel("연도", fontsize=13)
    ax.set_ylabel("온도(℃)", fontsize=13)

    # 범례
    ax.legend()

    # 격자
    ax.grid(alpha=0.3)

    st.pyplot(fig)

    # 데이터 표 출력
    st.subheader("📋 선택 날짜 데이터")

    st.dataframe(
        filtered_df[
            ['연도', '최고기온(℃)', '최저기온(℃)']
        ].sort_values(by='연도')
    )

else:
    st.warning("해당 날짜의 데이터가 없습니다.")
