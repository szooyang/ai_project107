# app.py

import streamlit as st
import folium
from streamlit.components.v1 import html

st.set_page_config(
    page_title="서울 관광지 TOP10 지도",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ 외국인들이 좋아하는 서울 관광지 TOP10")
st.markdown("폴리움(Folium) 지도로 서울의 인기 관광지를 살펴보세요!")

# 관광지 데이터
places = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "station": "경복궁역 (3호선)",
        "fun": "한복 체험, 궁궐 산책, 국립민속박물관 관람"
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.985302,
        "station": "명동역 (4호선)",
        "fun": "쇼핑, 길거리 음식, 화장품 투어"
    },
    {
        "name": "남산서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "station": "명동역 (4호선)",
        "fun": "야경 감상, 케이블카, 사랑의 자물쇠"
    },
    {
        "name": "홍대거리",
        "lat": 37.556350,
        "lon": 126.922672,
        "station": "홍대입구역 (2호선)",
        "fun": "버스킹 공연, 카페 탐방, 쇼핑"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.582604,
        "lon": 126.983998,
        "station": "안국역 (3호선)",
        "fun": "한옥 골목 산책, 전통문화 체험, 사진 촬영"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.512568,
        "lon": 127.102535,
        "station": "잠실역 (2호선)",
        "fun": "서울스카이 전망대, 쇼핑몰, 아쿠아리움"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.566526,
        "lon": 127.009224,
        "station": "동대문역사문화공원역 (2호선)",
        "fun": "야간 산책, 디자인 전시, 야시장"
    },
    {
        "name": "한강공원",
        "lat": 37.528856,
        "lon": 126.932651,
        "station": "여의나루역 (5호선)",
        "fun": "치킨 먹기, 자전거 타기, 피크닉"
    },
    {
        "name": "인사동",
        "lat": 37.574018,
        "lon": 126.984902,
        "station": "안국역 (3호선)",
        "fun": "전통 찻집, 기념품 쇼핑, 길거리 공연"
    },
    {
        "name": "코엑스",
        "lat": 37.511684,
        "lon": 127.059151,
        "station": "삼성역 (2호선)",
        "fun": "별마당도서관, 쇼핑, 아쿠아리움"
    }
]

# 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11,
    tiles="CartoDB positron"
)

# 마커 추가
for place in places:
    tooltip_text = f"🚇 가까운 역: {place['station']}"

    folium.Marker(
        location=[place["lat"], place["lon"]],
        tooltip=tooltip_text,
        popup=f"""
        <b>{place['name']}</b><br>
        🚇 {place['station']}<br>
        🎈 {place['fun']}
        """,
        icon=folium.Icon(
            color="orange",
            icon="star"
        )
    ).add_to(m)

# 지도 HTML 렌더링
map_html = m._repr_html_()

html(map_html, height=650)

st.markdown("---")
st.subheader("📍 관광지 & 가까운 지하철역 안내")

for idx, place in enumerate(places, start=1):
    st.markdown(
        f"""
### {idx}. {place['name']}
- 🚇 가까운 지하철역: **{place['station']}**
- 🎉 놀거리: {place['fun']}
"""
    )

st.markdown("---")
st.caption("Made with Streamlit + Folium 🗺️")
