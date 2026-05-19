import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="📚 MBTI 책 & 영화 추천기",
    page_icon="🎬",
    layout="centered"
)

# MBTI 추천 데이터
mbti_data = {
    "INTJ": {
        "books": [
            {
                "title": "1984",
                "author": "조지 오웰",
                "year": "1949",
                "desc": "통제 사회를 다룬 깊이 있는 명작 🧠"
            },
            {
                "title": "아몬드",
                "author": "손원평",
                "year": "2017",
                "desc": "감정을 배우는 성장 이야기 🌱"
            }
        ],
        "movies": [
            {
                "title": "2001: 스페이스 오디세이",
                "year": "1968",
                "desc": "철학적이고 웅장한 SF 영화 🚀"
            },
            {
                "title": "시민 케인",
                "year": "1941",
                "desc": "영화 역사상 최고의 명작 중 하나 🎥"
            }
        ]
    },

    "INTP": {
        "books": [
            {
                "title": "멋진 신세계",
                "author": "올더스 헉슬리",
                "year": "1932",
                "desc": "미래 사회를 상상하게 만드는 작품 🤖"
            },
            {
                "title": "달러구트 꿈 백화점",
                "author": "이미예",
                "year": "2020",
                "desc": "상상력이 가득한 힐링 판타지 ✨"
            }
        ],
        "movies": [
            {
                "title": "메트로폴리스",
                "year": "1927",
                "desc": "전설적인 고전 SF 영화 ⚙️"
            },
            {
                "title": "카사블랑카",
                "year": "1942",
                "desc": "감성과 철학이 담긴 로맨스 🎹"
            }
        ]
    },

    "ENTJ": {
        "books": [
            {
                "title": "위대한 개츠비",
                "author": "F. 스콧 피츠제럴드",
                "year": "1925",
                "desc": "야망과 성공을 다룬 고전 💼"
            },
            {
                "title": "불편한 편의점",
                "author": "김호연",
                "year": "2021",
                "desc": "사람들의 이야기가 따뜻하게 담긴 소설 🏪"
            }
        ],
        "movies": [
            {
                "title": "대부",
                "year": "1972",
                "desc": "리더십과 권력을 보여주는 명작 👑"
            },
            {
                "title": "록키",
                "year": "1976",
                "desc": "포기하지 않는 도전 이야기 🥊"
            }
        ]
    },

    "ENTP": {
        "books": [
            {
                "title": "동물농장",
                "author": "조지 오웰",
                "year": "1945",
                "desc": "풍자와 아이디어가 뛰어난 작품 🐷"
            },
            {
                "title": "지구 끝의 온실",
                "author": "김초엽",
                "year": "2021",
                "desc": "상상력이 폭발하는 한국 SF 🌍"
            }
        ],
        "movies": [
            {
                "title": "닥터 스트레인지러브",
                "year": "1964",
                "desc": "유쾌한 블랙코미디 😎"
            },
            {
                "title": "스타워즈",
                "year": "1977",
                "desc": "상상력 가득한 우주 모험 🌌"
            }
        ]
    },

    "INFJ": {
        "books": [
            {
                "title": "어린 왕자",
                "author": "생텍쥐페리",
                "year": "1943",
                "desc": "삶의 의미를 돌아보게 하는 이야기 🌹"
            },
            {
                "title": "완득이",
                "author": "김려령",
                "year": "2008",
                "desc": "따뜻한 성장 이야기 😊"
            }
        ],
        "movies": [
            {
                "title": "사운드 오브 뮤직",
                "year": "1965",
                "desc": "희망과 음악이 가득한 영화 🎵"
            },
            {
                "title": "로마의 휴일",
                "year": "1953",
                "desc": "감성 가득한 클래식 로맨스 💕"
            }
        ]
    },

    "INFP": {
        "books": [
            {
                "title": "데미안",
                "author": "헤르만 헤세",
                "year": "1919",
                "desc": "자아를 찾아가는 성장 소설 🌙"
            },
            {
                "title": "죽이고 싶은 아이",
                "author": "이꽃님",
                "year": "2021",
                "desc": "몰입감 넘치는 청소년 소설 🔥"
            }
        ],
        "movies": [
            {
                "title": "오즈의 마법사",
                "year": "1939",
                "desc": "상상력이 가득한 판타지 🌈"
            },
            {
                "title": "찰리 채플린의 모던 타임즈",
                "year": "1936",
                "desc": "웃음과 메시지를 함께 담은 영화 🤹"
            }
        ]
    },

    "ENFJ": {
        "books": [
            {
                "title": "노인과 바다",
                "author": "어니스트 헤밍웨이",
                "year": "1952",
                "desc": "인내와 희망의 이야기 🌊"
            },
            {
                "title": "세계를 건너 너에게 갈게",
                "author": "이꽃님",
                "year": "2018",
                "desc": "감동적인 시간 여행 이야기 💌"
            }
        ],
        "movies": [
            {
                "title": "사랑은 비를 타고",
                "year": "1952",
                "desc": "기분 좋아지는 뮤지컬 ☔"
            },
            {
                "title": "죠스",
                "year": "1975",
                "desc": "긴장감 넘치는 스릴러 🦈"
            }
        ]
    },

    "ENFP": {
        "books": [
            {
                "title": "톰 소여의 모험",
                "author": "마크 트웨인",
                "year": "1876",
                "desc": "자유로운 모험 이야기 🛶"
            },
            {
                "title": "미드나잇 라이브러리",
                "author": "매트 헤이그",
                "year": "2020",
                "desc": "인생의 가능성을 돌아보게 하는 소설 📚"
            }
        ],
        "movies": [
            {
                "title": "그리스",
                "year": "1978",
                "desc": "에너지 넘치는 청춘 뮤지컬 🎤"
            },
            {
                "title": "킹콩",
                "year": "1933",
                "desc": "전설적인 클래식 영화 🦍"
            }
        ]
    }
}

# 나머지 MBTI 자동 채우기
default_data = {
    "books": [
        {
            "title": "죄와 벌",
            "author": "도스토예프스키",
            "year": "1866",
            "desc": "인간 심리를 깊게 다룬 명작 📖"
        },
        {
            "title": "페인트",
            "author": "이희영",
            "year": "2019",
            "desc": "청소년들에게 인기 많은 미래 소설 🎨"
        }
    ],
    "movies": [
        {
            "title": "백 투 더 퓨처",
            "year": "1985",
            "desc": "시간 여행의 레전드 ⚡"
        },
        {
            "title": "록키",
            "year": "1976",
            "desc": "열정 넘치는 스포츠 영화 🥊"
        }
    ]
}

all_mbti = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

for mbti in all_mbti:
    if mbti not in mbti_data:
        mbti_data[mbti] = default_data

# 제목
st.title("📚🎬 MBTI 책 & 영화 추천기")
st.write("너의 MBTI에 어울리는 책과 영화를 추천해줄게 😎")

# MBTI 선택
selected_mbti = st.selectbox(
    "✨ MBTI를 선택해봐!",
    all_mbti
)

# 추천 결과 출력
data = mbti_data[selected_mbti]

st.header(f"💡 {selected_mbti} 추천 결과")

# 책 추천
st.subheader("📚 추천 책 2권")

for book in data["books"]:
    st.markdown(
        f"""
### 📖 {book['title']}
- ✍️ 작가: {book['author']}
- 📅 출간 연도: {book['year']}
- 💬 한줄 소개: {book['desc']}
"""
    )

# 영화 추천
st.subheader("🎬 추천 영화 2편")

for movie in data["movies"]:
    st.markdown(
        f"""
### 🍿 {movie['title']}
- 📅 개봉 연도: {movie['year']}
- 💬 한줄 소개: {movie['desc']}
"""
    )

# 하단 메시지
st.success("🌟 오늘의 취향 탐험 완료! 친구들 MBTI도 같이 해보자 😆")
