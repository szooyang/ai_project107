import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 진로 추천 🌈",
    page_icon="✨",
    layout="centered"
)

# MBTI별 진로 데이터
mbti_data = {
    "INTJ": {
        "nickname": "전략가 🧠",
        "jobs": [
            {
                "name": "데이터 사이언티스트 💻",
                "major": "컴퓨터공학과, 인공지능학과, 통계학과",
                "personality": "논리적이고 문제 해결을 좋아하는 사람",
                "salary": "평균 연봉 약 6,500만 원"
            },
            {
                "name": "건축가 🏢",
                "major": "건축학과, 실내건축학과",
                "personality": "창의적이면서 계획 세우기를 좋아하는 사람",
                "salary": "평균 연봉 약 5,500만 원"
            }
        ]
    },

    "INTP": {
        "nickname": "사색가 🔍",
        "jobs": [
            {
                "name": "프로그래머 👨‍💻",
                "major": "소프트웨어학과, 컴퓨터공학과",
                "personality": "호기심이 많고 새로운 것을 탐구하는 사람",
                "salary": "평균 연봉 약 5,800만 원"
            },
            {
                "name": "연구원 🧪",
                "major": "물리학과, 화학과, 생명과학과",
                "personality": "깊게 생각하고 분석하는 걸 좋아하는 사람",
                "salary": "평균 연봉 약 5,200만 원"
            }
        ]
    },

    "ENTJ": {
        "nickname": "통솔자 👑",
        "jobs": [
            {
                "name": "기업 CEO 📈",
                "major": "경영학과, 경제학과",
                "personality": "리더십이 강하고 목표 지향적인 사람",
                "salary": "평균 연봉 약 8,000만 원 이상"
            },
            {
                "name": "변호사 ⚖️",
                "major": "법학과",
                "personality": "논리적이고 설득력이 좋은 사람",
                "salary": "평균 연봉 약 7,000만 원"
            }
        ]
    },

    "ENTP": {
        "nickname": "발명가 🚀",
        "jobs": [
            {
                "name": "마케팅 기획자 📢",
                "major": "광고홍보학과, 경영학과",
                "personality": "아이디어가 많고 사람과 소통을 좋아하는 사람",
                "salary": "평균 연봉 약 5,000만 원"
            },
            {
                "name": "스타트업 창업가 💡",
                "major": "경영학과, 창업학과",
                "personality": "도전을 즐기고 창의적인 사람",
                "salary": "평균 연봉 약 6,000만 원 이상"
            }
        ]
    },

    "INFJ": {
        "nickname": "옹호자 🌿",
        "jobs": [
            {
                "name": "심리상담사 💚",
                "major": "심리학과, 상담학과",
                "personality": "공감 능력이 뛰어나고 배려심이 많은 사람",
                "salary": "평균 연봉 약 4,500만 원"
            },
            {
                "name": "작가 ✍️",
                "major": "문예창작과, 국어국문학과",
                "personality": "상상력이 풍부하고 감수성이 깊은 사람",
                "salary": "평균 연봉 약 4,000만 원"
            }
        ]
    },

    "INFP": {
        "nickname": "중재자 🎨",
        "jobs": [
            {
                "name": "웹툰 작가 🖌️",
                "major": "애니메이션학과, 만화콘텐츠학과",
                "personality": "창의적이고 감성이 풍부한 사람",
                "salary": "평균 연봉 약 4,200만 원"
            },
            {
                "name": "사회복지사 🤝",
                "major": "사회복지학과",
                "personality": "따뜻하고 사람을 돕는 걸 좋아하는 사람",
                "salary": "평균 연봉 약 3,800만 원"
            }
        ]
    },

    "ENFJ": {
        "nickname": "선도자 🌟",
        "jobs": [
            {
                "name": "교사 🍎",
                "major": "교육학과, 국어교육과, 수학교육과",
                "personality": "사람을 이끌고 도와주는 걸 좋아하는 사람",
                "salary": "평균 연봉 약 5,000만 원"
            },
            {
                "name": "아나운서 🎤",
                "major": "언론정보학과, 방송연예과",
                "personality": "말하는 걸 좋아하고 밝은 사람",
                "salary": "평균 연봉 약 5,500만 원"
            }
        ]
    },

    "ENFP": {
        "nickname": "활동가 🎈",
        "jobs": [
            {
                "name": "유튜버 📹",
                "major": "미디어학과, 방송영상학과",
                "personality": "에너지가 넘치고 창의적인 사람",
                "salary": "평균 연봉은 활동 규모에 따라 다양함"
            },
            {
                "name": "여행 가이드 ✈️",
                "major": "관광학과",
                "personality": "사람 만나는 걸 좋아하고 활발한 사람",
                "salary": "평균 연봉 약 4,000만 원"
            }
        ]
    },

    "ISTJ": {
        "nickname": "현실주의자 📚",
        "jobs": [
            {
                "name": "공무원 🏛️",
                "major": "행정학과, 법학과",
                "personality": "책임감이 강하고 꼼꼼한 사람",
                "salary": "평균 연봉 약 5,000만 원"
            },
            {
                "name": "회계사 🧾",
                "major": "회계학과, 경영학과",
                "personality": "계획적이고 정확한 걸 좋아하는 사람",
                "salary": "평균 연봉 약 7,000만 원"
            }
        ]
    },

    "ISFJ": {
        "nickname": "수호자 🛡️",
        "jobs": [
            {
                "name": "간호사 🏥",
                "major": "간호학과",
                "personality": "배려심이 많고 책임감 있는 사람",
                "salary": "평균 연봉 약 5,000만 원"
            },
            {
                "name": "초등교사 📖",
                "major": "초등교육과",
                "personality": "아이들을 좋아하고 성실한 사람",
                "salary": "평균 연봉 약 5,200만 원"
            }
        ]
    },

    "ESTJ": {
        "nickname": "경영자 📊",
        "jobs": [
            {
                "name": "경찰관 🚓",
                "major": "경찰행정학과",
                "personality": "책임감이 강하고 원칙을 중요하게 생각하는 사람",
                "salary": "평균 연봉 약 5,000만 원"
            },
            {
                "name": "프로젝트 매니저 📋",
                "major": "경영학과",
                "personality": "조직 관리와 계획을 잘하는 사람",
                "salary": "평균 연봉 약 6,000만 원"
            }
        ]
    },

    "ESFJ": {
        "nickname": "친선도모자 🎉",
        "jobs": [
            {
                "name": "호텔리어 🏨",
                "major": "호텔관광학과",
                "personality": "친절하고 서비스 정신이 좋은 사람",
                "salary": "평균 연봉 약 4,500만 원"
            },
            {
                "name": "승무원 ✈️",
                "major": "항공서비스학과",
                "personality": "사람과 소통하는 걸 좋아하는 사람",
                "salary": "평균 연봉 약 5,500만 원"
            }
        ]
    },

    "ISTP": {
        "nickname": "장인 🔧",
        "jobs": [
            {
                "name": "자동차 엔지니어 🚗",
                "major": "기계공학과, 자동차공학과",
                "personality": "손으로 만드는 걸 좋아하고 분석적인 사람",
                "salary": "평균 연봉 약 6,000만 원"
            },
            {
                "name": "파일럿 🛫",
                "major": "항공운항학과",
                "personality": "침착하고 집중력이 좋은 사람",
                "salary": "평균 연봉 약 8,000만 원"
            }
        ]
    },

    "ISFP": {
        "nickname": "예술가 🎵",
        "jobs": [
            {
                "name": "디자이너 🎨",
                "major": "시각디자인학과, 산업디자인학과",
                "personality": "감각적이고 창의적인 사람",
                "salary": "평균 연봉 약 4,800만 원"
            },
            {
                "name": "플로리스트 🌸",
                "major": "원예학과",
                "personality": "섬세하고 감성이 풍부한 사람",
                "salary": "평균 연봉 약 3,800만 원"
            }
        ]
    },

    "ESTP": {
        "nickname": "사업가 🔥",
        "jobs": [
            {
                "name": "영업 전문가 💼",
                "major": "경영학과",
                "personality": "도전적이고 말솜씨가 좋은 사람",
                "salary": "평균 연봉 약 5,500만 원"
            },
            {
                "name": "스포츠 코치 ⚽",
                "major": "체육학과",
                "personality": "활동적이고 에너지가 넘치는 사람",
                "salary": "평균 연봉 약 4,500만 원"
            }
        ]
    },

    "ESFP": {
        "nickname": "연예인 🌈",
        "jobs": [
            {
                "name": "배우 🎬",
                "major": "연극영화과",
                "personality": "표현력이 좋고 사람들 앞에 서는 걸 좋아하는 사람",
                "salary": "평균 연봉은 활동에 따라 다양함"
            },
            {
                "name": "이벤트 플래너 🎊",
                "major": "이벤트학과, 관광학과",
                "personality": "분위기를 즐기고 활발한 사람",
                "salary": "평균 연봉 약 4,500만 원"
            }
        ]
    }
}

# 제목
st.title("✨ MBTI 진로 추천 프로그램")
st.write("나의 MBTI에 어울리는 진로를 알아보자! 😆")

# MBTI 선택
selected_mbti = st.selectbox(
    "👇 MBTI를 선택해봐!",
    list(mbti_data.keys())
)

# 결과 출력
if selected_mbti:
    info = mbti_data[selected_mbti]

    st.header(f"{selected_mbti} - {info['nickname']}")

    st.success("🎯 추천 진로 2가지를 소개할게!")

    for idx, job in enumerate(info["jobs"], start=1):
        st.subheader(f"{idx}. {job['name']}")

        st.write(f"📚 **추천 학과**")
        st.write(job["major"])

        st.write(f"😊 **어울리는 성격**")
        st.write(job["personality"])

        st.write(f"💰 **평균 연봉**")
        st.write(job["salary"])

        st.divider()

# 하단 문구
st.caption("※ 연봉 정보는 평균적인 예시이며 실제와 차이가 있을 수 있어요 🙂")
