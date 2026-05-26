import streamlit as st
import random

# 앱 제목 설정
st.title("🎰 777777 잭팟 시뮬레이터")
st.write("모든 숫자가 7이 나올 때까지 무한 도전합니다!")

# 세션 상태 초기화 (카운트 저장용)
if 'count' not in st.session_state:
    st.session_state.count = 0

# 시작 버튼
if st.button("시뮬레이션 시작"):
    # 결과를 실시간으로 보여줄 빈 공간 생성
    status_text = st.empty()
    numbers_text = st.empty()
    
    while True:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        c = random.randint(1, 9)
        d = random.randint(1, 9)
        e = random.randint(1, 9)
        f = random.randint(1, 9)
        
        st.session_state.count += 1
        
        # 성능과 시각적 효과를 위해 10,000번마다 한 번씩 화면에 진행 상황 표시
        if st.session_state.count % 10000 == 0:
            status_text.text(f"현재 시도 횟수: {st.session_state.count:,}번")
            numbers_text.text(f"최근 뽑힌 숫자: [{a}, {b}, {c}, {d}, {e}, {f}]")
        
        # 조건 체크 (모두 7인 경우)
        if a == 7 and b == 7 and c == 7 and d == 7 and e == 7 and f == 7:
            st.balloons() # 잭팟 축하 효과 🎉
            st.success(f"🎉 잭팟! {st.session_state.count:,}번째 만에 성공했습니다!")
            break

# 초기화 버튼
if st.button("카운트 초기화"):
    st.session_state.count = 0
    st.rerun()