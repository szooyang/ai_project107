import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(
    page_title="서울 관광지 TOP10",
    page_icon="🗺️",
    layout="centered"
)

st.title("🗺️ 외국인들이 좋아하는 서울 관광지 TOP10")
st.markdown("서울의 인기 관광지를 한국어 지도로 확인해보세요! 🇰🇷")

# 관광지 데이터
tour_places = [
    {
        "name": "경복궁",
        "location": [37.5796, 126.9770],
        "description": "조선 시대의 대표 궁궐",
        "station": "경복궁역(3호선)",
        "fun": """
- 한복을 입고 궁궐 인증샷을 찍으면 정말 멋져요 👘
- 수문장 교대식을 가까이에서 볼 수 있어요.
- 근처 서촌 골목에서 감성 카페와 맛집 탐방도 가능해요.
- 야간개장 시즌에는 조명이 켜진 궁궐 풍경이 정말 아름다워요.
"""
    },
    {
        "name": "북촌한옥마을",
        "location": [37.5826, 126.9830],
        "description": "전통 한옥이 모여 있는 마을",
        "station": "안국역(3호선)",
        "fun": """
- 전통 한옥 골목을 걸으며 감성 사진을 찍기 좋아요 📸
- 한옥 공방에서 전통 소품 만들기 체험도 할 수 있어요.
- 조용한 찻집에서 전통차를 마시며 쉬기 좋아요.
- 골목 사이사이 숨은 갤러리와 공예 상점 구경도 재미있어요.
"""
    },
    {
        "name": "명동",
        "location": [37.5636, 126.9827],
        "description": "쇼핑과 먹거리의 중심지",
        "station": "명동역(4호선)",
        "fun": """
- 다양한 K-뷰티 매장에서 화장품 쇼핑을 즐길 수 있어요 💄
- 길거리 음식 먹방 코스로 유명해요.
- 밤이 되면 화려한 간판과 분위기가 정말 활기차요.
- 근처 명동성당까지 함께 둘러보는 코스도 인기예요.
"""
    },
    {
        "name": "N서울타워",
        "location": [37.5512, 126.9882],
        "description": "서울 야경 명소",
        "station": "명동역(4호선)",
        "fun": """
- 서울 전체가 보이는 야경이 정말 유명해요 🌃
- 케이블카를 타고 올라가는 재미가 있어요.
- 사랑의 자물쇠 포토존은 커플 관광객들에게 인기예요.
- 밤에 전망대 카페에서 서울 풍경을 감상하기 좋아요.
"""
    },
    {
        "name": "홍대거리",
        "location": [37.5563, 126.9220],
        "description": "젊음과 예술의 거리",
        "station": "홍대입구역(2호선)",
        "fun": """
- 거리 공연과 버스킹을 자유롭게 즐길 수 있어요 🎵
- 개성 있는 소품샵과 패션 매장이 정말 많아요.
- 디저트 카페와 포토부스 투어도 인기예요.
- 늦은 밤까지 활기찬 분위기를 느낄 수 있어요.
"""
    },
    {
        "name": "인사동",
        "location": [37.5740, 126.9865],
        "description": "전통 문화와 공예 거리",
        "station": "안국역(3호선)",
        "fun": """
- 전통 공예품과 한국 기념품을 구경하기 좋아요 🎎
- 전통 한식과 떡 디저트를 맛볼 수 있어요.
- 붓글씨 체험이나 공예 체험도 가능해요.
- 골목마다 전통 감성이 살아 있어 산책하기 좋아요.
"""
    },
    {
        "name": "롯데월드타워",
        "location": [37.5131, 127.1025],
        "description": "서울의 초고층 랜드마크",
        "station": "잠실역(2호선)",
        "fun": """
- 서울스카이 전망대에서 초고층 전망을 즐길 수 있어요 🏙️
- 대형 쇼핑몰과 아쿠아리움이 함께 있어 하루 종일 놀 수 있어요.
- 석촌호수 산책 코스도 정말 예뻐요.
- 야경 사진 명소로도 유명해요.
"""
    },
    {
        "name": "광장시장",
        "location": [37.5704, 126.9998],
        "description": "전통 음식 시장",
        "station": "종로5가역(1호선)",
        "fun": """
- 빈대떡, 마약김밥 같은 유명 먹거리를 맛볼 수 있어요 🍢
- 시장 특유의 활기찬 분위기가 재미있어요.
- 다양한 전통 길거리 음식을 한 번에 즐길 수 있어요.
- 넷플릭스 예능에 나온 맛집 찾기도 인기예요.
"""
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "location": [37.5665, 127.0092],
        "description": "현대적인 디자인 명소",
        "station": "동대문역사문화공원역(2호선)",
        "fun": """
- 미래적인 건축 디자인으로 유명한 포토 명소예요 📷
- 다양한 전시와 디자인 행사가 자주 열려요.
- 밤에는 LED 장미정원이 아름다워요.
- 근처 동대문 쇼핑타운과 함께 둘러보기 좋아요.
"""
    },
    {
        "name": "한강공원",
        "location": [37.5207, 126.9395],
        "description": "서울 시민들의 휴식 공간",
        "station": "여의나루역(5호선)",
        "fun": """
- 한강 자전거 라이딩과 피크닉을 즐기기 좋아요 🚴
- 치킨과 라면 먹방 장소로 유명해요.
- 밤에는 한강 야경과 달빛 분위기가 정말 예뻐요.
- 봄에는 벚꽃 명소로도 인기가 많아요.
"""
    }
]

# 서울 중심 좌표
seoul_center = [37.5665, 126.9780]

# 지도 생성
m = folium.Map(
    location=seoul_center,
    zoom_start=11,
    tiles="OpenStreetMap"  # 색깔 있는 지도
)

# 마커 클러스터 추가
marker_cluster = MarkerCluster().add_to(m)

# 관광지 마커 추가
for place in tour_places:
    folium.Marker(
        location=place["location"],
        popup=f"""
        <b>{place['name']}</b><br>
        {place['description']}<br>
        🚇 가까운 역: {place['station']}
        """,
        tooltip=place["name"],
        icon=folium.Icon(
            color="blue",
            icon="star"
        )
    ).add_to(marker_cluster)

# 지도 출력
st.subheader("📍 서울 관광지 지도")

# 지도 크기 60% 정도로 축소
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    st_folium(
        m,
        width=850,
        height=500
    )

# 관광지 선택
st.subheader("🎡 관광지 상세 정보")

selected_place = st.selectbox(
    "관광지를 선택하세요 👇",
    [place["name"] for place in tour_places]
)

# 선택한 관광지 정보 출력
for place in tour_places:
    if place["name"] == selected_place:
        st.markdown(f"## 📍 {place['name']}")
        st.markdown(f"### 🚇 가장 가까운 지하철역")
        st.info(place["station"])

        st.markdown("### 🎉 여기서 무엇을 할 수 있을까?")
        st.success(place["fun"])

        st.markdown("### 📝 관광지 설명")
        st.write(place["description"])
