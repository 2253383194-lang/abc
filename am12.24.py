# streamlit_app.py
import streamlit as st

st.set_page_config(page_title='网易云在线播放器', page_icon='🎵')

# 三首歌外链（第三首已换成河图《左公柳》）
music_arr = [
    {
        'url': 'https://music.163.com/song/media/outer/url?id=3327856998.mp3',  # 李嘉格-春予你
        'text': '李嘉格',
        'photo': 'http://p1.music.126.net/qKSYMuy9ruRRdVRO8MsONA==/109951172418592653.jpg?param=130y130',
        'name': '春予你'
    },
    {
        'url': 'https://music.163.com/song/media/outer/url?id=3327534465.mp3',  # 陈鸿宇-乐园
        'text': '陈鸿宇',
        'photo': 'http://p2.music.126.net/nS7JpdNOGUPffz8-yCneGw==/109951172414465715.jpg?param=130y130',
        'name': '乐园'
    },
    {
        'url': 'https://music.163.com/song/media/outer/url?id=3326339191.mp3',  # 河图-左公柳
        'text': '河图',
        'photo': 'http://p2.music.126.net/6WbRoTRTkuQy_XfFhi7-5g==/109951172402244219.jpg?param=130y130',
        'name': '左公柳'
    }
]

# session_state
if 'idx' not in st.session_state:
    st.session_state.idx = 0

def next_song():
    st.session_state.idx = (st.session_state.idx + 1) % len(music_arr)

def prev_song():
    st.session_state.idx = (st.session_state.idx - 1) % len(music_arr)

# 当前歌曲
curr = music_arr[st.session_state.idx]

# 页面
st.title('🎵 网易云在线播放器')


c1, c2 = st.columns([1,2])
with c1:
    st.image(curr['photo'], width=300)
with c2:
    st.markdown(f"**{curr['text']}** — *《{curr['name']}》*")
    st.audio(curr['url'], format='audio/mp3')
    st.button('⏮ 上一首', use_container_width=True, on_click=prev_song)
    st.button('⏭ 下一首', use_container_width=True, on_click=next_song)
