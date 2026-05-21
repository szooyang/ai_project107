import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="🌍 국가별 MBTI 분석",
    page_icon="🌎",
    layout="wide"
)

# -----------------------------
# 제목
# -----------------------------
st.title("🌍 국가별 MBTI 비율 분석")
st.markdown("국가를 선택하면 MBTI 16유형 비율을 인터랙티브 그래프로 확인할 수 있어요!")

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types(2).csv")
    return df

df = load_data()

# -----------------------------
# MBTI 컬럼 추출
# -----------------------------
mbti_columns = [col for col in df.columns if col != "Country"]

# -----------------------------
# 국가 선택
# -----------------------------
country = st.selectbox(
    "🌏 국가를 선택하세요",
    sorted(df["Country"].unique())
)

# -----------------------------
# 선택 국가 데이터
# -----------------------------
country_data = df[df["Country"] == country].iloc[0]

mbti_values = country_data[mbti_columns].sort_values(ascending=False)

# -----------------------------
# 색상 설정
# 1등은 빨간색
# 나머지는 파란색 그라데이션
# -----------------------------
blue_scale = px.colors.sequential.Blues

colors = ["red"]

for i in range(1, len(mbti_values)):
    idx = int((i / len(mbti_values)) * (len(blue_scale) - 1))
    colors.append(blue_scale[idx])

# -----------------------------
# 그래프 생성
# -----------------------------
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=mbti_values.index,
        y=mbti_values.values,
        marker_color=colors,
        text=[f"{v:.2f}%" for v in mbti_values.values],
        textposition="outside",
        hovertemplate=
        "<b>%{x}</b><br>" +
        "비율: %{y:.2f}%<extra></extra>"
    )
)

# -----------------------------
# 그래프 레이아웃
# -----------------------------
fig.update_layout(
    title=f"📊 {country}의 MBTI 비율",
    xaxis_title="MBTI 유형",
    yaxis_title="비율 (%)",
    template="plotly_white",
    height=650,
    font=dict(size=15),
    hoverlabel=dict(font_size=15),
)

# -----------------------------
# 그래프 출력
# -----------------------------
st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# TOP 3 출력
# -----------------------------
st.subheader("🏆 TOP 3 MBTI")

top3 = mbti_values.head(3)

col1, col2, col3 = st.columns(3)

for idx, (mbti, value) in enumerate(top3.items()):
    with [col1, col2, col3][idx]:
        st.metric(
            label=mbti,
            value=f"{value:.2f}%"
        )

# -----------------------------
# 데이터 테이블
# -----------------------------
st.subheader("📋 전체 데이터")

table_df = pd.DataFrame({
    "MBTI": mbti_values.index,
    "비율(%)": mbti_values.values.round(2)
})

st.dataframe(
    table_df,
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# 푸터
# -----------------------------
st.markdown("---")
st.caption("📌 Streamlit + Plotly 기반 MBTI 데이터 시각화")
