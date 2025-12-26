import streamlit as st

st.set_page_config(page_title="视频中心")

video_arr = [
    {"url": "https://www.w3school.com.cn/example/html5/mov_bbb.mp4", "title": "还珠格格第一部-第1集"},
    {"url": "https://www.w3schools.com/html/movie.mp4", "title": "还珠格格第一部-第2集"},
    {"url": "https://media.w3.org/2010/05/sintel/trailer.mp4", "title": "还珠格格第一部-第3集"},
    {"url": "https://www.w3school.com.cn/example/html5/mov_bbb.mp4", "title": "还珠格格第二部-第4集"},
    {"url": "https://www.w3schools.com/html/movie.mp4", "title": "还珠格格第二部-第5集"},
    {"url": "https://media.w3.org/2010/05/sintel/trailer.mp4", "title": "还珠格格第二部-第6集"},
]

if "ind" not in st.session_state:
    st.session_state.ind = 0

st.title(video_arr[st.session_state.ind]["title"])

st.video(video_arr[st.session_state.ind]["url"] or None) 

def play_video(i):
    st.session_state.ind = i

for row in range(2):
    cols = st.columns(3)
    for col_idx in range(3):
        i = row * 3 + col_idx
        with cols[col_idx]:
            st.button(f"第 {i+1} 集",
                      key=f"btn{i}",
                      on_click=play_video,
                      args=(i,),
                      use_container_width=True)
