import streamlit as st

st.set_page_config(page_title='相册网站', page_icon='🏀')

image_ua = [
    {
        'url': 'https://pic2.zhimg.com/v2-4964c43148feaf90ea861af6714adfbe_r.jpg?source=1940ef5c',
        'text': '欧文'
    },
    {
        'url': 'https://puui.qpic.cn/vpic_cover/b35095rw9oe/b35095rw9oe_1680767368_vt.jpg/720',
        'text': '科比'
    },
    {
        'url': 'https://n.sinaimg.cn/sinakd20118/408/w1728h1080/20211024/e166-e31f1d048665f4dd9b196b41b178f610.jpg',
        'text': '库里'
    }
]

# 初始化session_state中的ind（当前图片索引）
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 显示当前图片
st.image(image_ua[st.session_state['ind']]['url'], caption=image_ua[st.session_state['ind']]['text'])

# 分栏容器
c1, c2 = st.columns(2)

# 下一张的逻辑
def nextimg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(image_ua)

# 上一张的逻辑（新增）
def previmg():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(image_ua)  # 取模实现循环切换


with c1:
    # 绑定上一张的函数到按钮
    st.button('上一张', use_container_width=True, on_click=previmg)

with c2:
    st.button('下一张', use_container_width=True, on_click=nextimg)
