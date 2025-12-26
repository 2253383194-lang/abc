import streamlit as st

# 页面配置
st.set_page_config(
    page_title="我的应用中心",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:
    st.title("🧭 导航菜单")
    st.markdown("---")
    
    # 定义页面列表
    pages = ["📄 数字文档", "🍜 南宁美食数据", "📸 相册", 
             "🎵 音乐播放器", "📺 视频网站", "👤 简历生成器"]
    
    # 初始化session_state（如果未设置）
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "📄 数字文档"
    
    # 生成菜单按钮
    for page_name in pages:
        # 判断当前页面是否被选中
        if st.session_state.current_page == page_name:
            # 选中状态：使用primary按钮呈现高亮
            st.button(
                page_name,
                key=f"btn_{page_name}",
                use_container_width=True,
                type="primary"
            )
        else:
            # 未选中状态：使用secondary按钮
            if st.button(
                page_name,
                key=f"btn_{page_name}",
                use_container_width=True
            ):
                # 点击后更新当前页面
                st.session_state.current_page = page_name
                st.rerun()  # 立即刷新页面
    
    st.markdown("---")


# 页面路由 - 根据当前选中的按钮显示对应内容

current_page = st.session_state.current_page
if current_page == "📄 数字文档":

    import streamlit as st
    import pandas as pd

    # 自定义CSS样式
    st.markdown("""
        <style>
        .title {
            color: #2c3e50;
            font-family: 'Consolas', monospace;
            text-shadow: 0 0 8px #3498db;
        }
        .header {
            color: #2980b9;
            font-family: 'Consolas', monospace;
            border-left: 3px solid #3498db;
            padding-left: 8px;
        }
        .stMetricDelta {
            color: #27ae60 !important;
        }
        .stCode {
            border: 1px solid #3498db !important;
        }
        .task-table {
            width: 100%;
            border-collapse: collapse;
            font-family: 'Consolas', monospace;
        }
        .task-table th, .task-table td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        .task-table th:nth-child(1), .task-table td:nth-child(1) {
            color: #1E90FF !important;
            font-weight: bold;
        }
        .task-table th:nth-child(2), .task-table td:nth-child(2) {
            color: #32CD32 !important;
        }
        .task-table th:nth-child(3), .task-table td:nth-child(3) {
            color: #FFD700 !important;
            font-weight: bold;
        }
        .task-table th:nth-child(4), .task-table td:nth-child(4) {
            color: #FF6347 !important;
        }
        .system-label {
            color: #27ae60 !important;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='title'>--- 学生 小唐and小潘 数字档案 ---</h1>", unsafe_allow_html=True)
    st.write("")

    st.markdown("<h3 class='header'>🔑基础信息</h3>", unsafe_allow_html=True)
    st.write("""
        学生ID:<span style='color:#27ae60'> 22053040222 and 22053040209 </span>
        <br>
        注册时间:<span style='color:#27ae60'> 2025-12-18 15:11:11 </span> | 精神状态: <span style='color:#27ae60'>✅正常</span>
        <br>
        当前位置: <span style='color:#e67e22'>实训楼710</span>  | 安全等级: <span style='color:#e67e22'>机密</span>
    """, unsafe_allow_html=True)
    st.write("")

    st.markdown("<h3 class='header'>📊技能矩阵</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="C++", value="95%", delta="+3%")
    with col2:
        st.metric(label="Python", value="87%", delta="-2%")
    with col3:
        st.metric(label="Java", value="68%", delta="-10%")

    st.markdown("<h3 class='header'>Streamlit课程进度</h3>", unsafe_allow_html=True)
    st.progress(40)

    st.markdown("<h3 class='header'>📅任务日志</h3>", unsafe_allow_html=True)
    task_data = {
        "日期": ["2023-10-01", "2023-10-12", "2023-10-22"],
        "任务": ["学生数字档案", "成绩管理系统", "数据可视化展示"],
        "状态": ["✅ 已完成", "🕣 进行中", "❌ 未完成"],
        "难度": ["★★☆☆☆", "★★★☆☆", "★★★★☆"]
    }
    task_df = pd.DataFrame(task_data)
    html_table = f"""
    <table class="task-table">
        <thead><tr><th>日期</th><th>任务</th><th>状态</th><th>难度</th></tr></thead>
        <tbody>
            {''.join([f'<tr><td>{row.日期}</td><td>{row.任务}</td><td>{row.状态}</td><td>{row.难度}</td></tr>' for _, row in task_df.iterrows()])}
        </tbody>
    </table>
    """
    st.markdown(html_table, unsafe_allow_html=True)

    st.markdown("<h3 class='header'>🔐最新代码成果</h3>", unsafe_allow_html=True)
    code_content = """
def check_vulnerability():
    vuln_list = []
    if detect_vulnerability1():
        vuln_list.append("ACCESS_GRANTED")
    else:
        vuln_list.append("ACCESS_DENIED")
    return vuln_list
"""
    st.code(code_content, language="python")

    st.write("")
    st.markdown("""
        <div>
            > <span class="system-label">SYSTEM MESSAGE</span>: 下一个任务已刷新信息。<br>
            > <span class="system-label">SYSTEM</span>: 请留意系统<br>
            > <span class="system-label">CONTROL</span>: 2025-12-18 16:00:58<br>
            > <span class="system-label">系统状态</span>: 在线 连接状态: 已加密
        </div>
    """, unsafe_allow_html=True)


# 页面路由 - 南宁美食数据

if current_page == "🍜 南宁美食数据":

    import streamlit as st
    import pandas as pd
    import numpy as np

    st.title("🍜 南宁美食数据仪表盘")
    st.divider()

    restaurants_data = {
        "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"],
        "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
        "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
        "人均消费(元)": [15, 20, 25, 35, 50],
        "latitude": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
        "longitude": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
    }

    months = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
    price_trend_data = {
        "月份": months * 5,
        "餐厅": ["星艺会尝不忘"]*12 + ["高峰柠檬鸭"]*12 + ["复记老友粉"]*12 + ["好友缘"]*12 + ["西冷牛排店"]*12,
        "价格(元)": [
            14,14,15,15,15,16,16,15,15,15,14,14, 19,19,20,20,21,21,21,20,20,20,19,19,
            24,24,25,25,26,26,26,25,25,25,24,24, 34,34,35,36,36,37,37,36,35,35,34,34, 48,49,50,50,51,51,52,51,50,50,49,48
        ]
    }

    sales_data = {"菜品": ["老友粉", "柠檬鸭", "粉饺", "牛杂", "牛排"], "月销量(份)": [8500, 6200, 4800, 5500, 3200]}
    area_data = {
        "月份": months,
        "中餐消费": [18,19,20,21,22,23,22,21,20,19,18,17],
        "快餐消费": [15,16,17,18,18,19,18,17,16,15,14,14],
        "西餐消费": [25,26,27,28,29,30,29,28,27,26,25,24]
    }

    df_restaurants = pd.DataFrame(restaurants_data)
    df_price = pd.DataFrame(price_trend_data)
    df_sales = pd.DataFrame(sales_data)
    df_area = pd.DataFrame(area_data)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("餐厅总数", value=len(df_restaurants))
    with col2:
        st.metric("平均评分", value=f"{df_restaurants['评分'].mean():.1f}")
    with col3:
        st.metric("平均人均消费", value=f"¥{df_restaurants['人均消费(元)'].mean():.0f}")

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📈 12个月价格走势")
        price_pivot = df_price.pivot(index="月份", columns="餐厅", values="价格(元)")
        st.line_chart(price_pivot, height=300)
    with col2:
        st.subheader("📊 特色菜品月销量")
        st.bar_chart(df_sales.set_index("菜品"), height=300)

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💰 消费类型趋势")
        st.area_chart(df_area.set_index("月份"), height=300)
    with col2:
        st.subheader("📍 餐厅位置分布")
        st.map(df_restaurants[["latitude", "longitude"]], zoom=11, height=300)


# 页面路由 - 相册

if current_page == "📸 相册":

    import streamlit as st

    image_ua = [
        {'url': 'https://pic2.zhimg.com/v2-4964c43148feaf90ea861af6714adfbe_r.jpg?source=1940ef5c ', 'text': '欧文'},
        {'url': 'https://puui.qpic.cn/vpic_cover/b35095rw9oe/b35095rw9oe_1680767368_vt.jpg/720 ', 'text': '科比'},
        {'url': 'https://n.sinaimg.cn/sinakd20118/408/w1728h1080/20211024/e166-e31f1d048665f4dd9b196b41b178f610.jpg ', 'text': '库里'}
    ]

    # 使用页面唯一标识的session_state
    if 'photo_ind' not in st.session_state:
        st.session_state['photo_ind'] = 0

    st.image(image_ua[st.session_state['photo_ind']]['url'], caption=image_ua[st.session_state['photo_ind']]['text'])

    def nextimg():
        st.session_state['photo_ind'] = (st.session_state['photo_ind'] + 1) % len(image_ua)

    def previmg():
        st.session_state['photo_ind'] = (st.session_state['photo_ind'] - 1) % len(image_ua)

    c1, c2 = st.columns(2)
    with c1:
        st.button('上一张', use_container_width=True, on_click=previmg)
    with c2:
        st.button('下一张', use_container_width=True, on_click=nextimg)


# 页面路由 - 音乐播放器

if current_page == "🎵 音乐播放器":

    import streamlit as st

    music_arr = [
        {
            'url': 'https://music.163.com/song/media/outer/url?id=3327856998.mp3 ',
            'text': '李嘉格',
            'photo': 'http://p1.music.126.net/qKSYMuy9ruRRdVRO8MsONA==/109951172418592653.jpg?param=130y130 ',
            'name': '春予你'
        },
        {
            'url': 'https://music.163.com/song/media/outer/url?id=3327534465.mp3 ',
            'text': '陈鸿宇',
            'photo': 'http://p2.music.126.net/nS7JpdNOGUPffz8-yCneGw==/109951172414465715.jpg?param=130y130 ',
            'name': '乐园'
        },
        {
            'url': 'https://music.163.com/song/media/outer/url?id=3326339191.mp3 ',
            'text': '河图',
            'photo': 'http://p2.music.126.net/6WbRoTRTkuQy_XfFhi7-5g==/109951172402244219.jpg?param=130y130 ',
            'name': '左公柳'
        }
    ]

    if 'music_idx' not in st.session_state:
        st.session_state['music_idx'] = 0

    def next_song():
        st.session_state['music_idx'] = (st.session_state['music_idx'] + 1) % len(music_arr)

    def prev_song():
        st.session_state['music_idx'] = (st.session_state['music_idx'] - 1) % len(music_arr)

    curr = music_arr[st.session_state['music_idx']]

    st.title('🎵 网易云在线播放器')
    c1, c2 = st.columns([1,2])
    with c1:
        st.image(curr['photo'], width=300)
    with c2:
        st.markdown(f"**{curr['text']}** — *《{curr['name']}》*")
        st.audio(curr['url'], format='audio/mp3')
        st.button('⏮ 上一首', use_container_width=True, on_click=prev_song)
        st.button('⏭ 下一首', use_container_width=True, on_click=next_song)


# 页面路由 - 视频网站

if current_page == "📺 视频网站":

    import streamlit as st

    video_arr = [
        {"url": "https://www.w3school.com.cn/example/html5/mov_bbb.mp4 ", "title": "还珠格格第一部-第1集"},
        {"url": "https://www.w3schools.com/html/movie.mp4 ", "title": "还珠格格第一部-第2集"},
        {"url": "https://media.w3.org/2010/05/sintel/trailer.mp4 ", "title": "还珠格格第一部-第3集"},
        {"url": "https://www.w3school.com.cn/example/html5/mov_bbb.mp4 ", "title": "还珠格格第二部-第4集"},
        {"url": "https://www.w3schools.com/html/movie.mp4 ", "title": "还珠格格第二部-第5集"},
        {"url": "https://media.w3.org/2010/05/sintel/trailer.mp4 ", "title": "还珠格格第二部-第6集"},
    ]

    if "video_ind" not in st.session_state:
        st.session_state.video_ind = 0

    st.title(video_arr[st.session_state.video_ind]["title"])
    st.video(video_arr[st.session_state.video_ind]["url"] or None) 

    def play_video(i):
        st.session_state.video_ind = i

    for row in range(2):
        cols = st.columns(3)
        for col_idx in range(3):
            i = row * 3 + col_idx
            with cols[col_idx]:
                st.button(f"第 {i+1} 集", key=f"btn{i}", on_click=play_video, args=(i,), use_container_width=True)


# 页面路由 - 简历生成器

if current_page == "👤 简历生成器":

    import streamlit as st
    from datetime import date

    st.markdown("## 📋个人简历生成器")
    st.caption("使用 Streamlit 创建您的个性化简历")

    left, right = st.columns([1, 2])

    with left:
        st.markdown("#### 个人信息表单")
        user_name   = st.text_input("姓名")
        user_gender = st.radio("性别", ["男", "女"], horizontal=True)
        user_phone  = st.text_input("电话")
        user_email  = st.text_input("邮箱")
        user_birth  = st.date_input("出生日期", value=date(2000,1,1))
        user_edu    = st.text_input("学历")
        user_job    = st.text_input("职位")
        user_exp    = st.number_input("工作经验（年）", min_value=0, max_value=50, step=1)

        c1, c2 = st.columns(2)
        with c1:
            salary_low = st.number_input("期望薪资下限（元）", min_value=0, step=1000)
        with c2:
            salary_high = st.number_input("期望薪资上限（元）", min_value=0, step=1000)

        st.write("语言能力")
        lang_cn = st.checkbox("中文")
        lang_en = st.checkbox("英语")

        skills = st.multiselect("技能（可多选）", ["Java", "Python", "机器学习"])

        user_intro = st.text_area("个人简介", height=120)
        uploaded_file = st.file_uploader("上传个人照片", type=["jpg", "jpeg", "png"])

    with right:
        st.markdown("#### 简历实时预览")
        if uploaded_file:
            st.image(uploaded_file, width=140)

        if user_name:
            st.markdown(f"**{user_name}**")

        info_parts = []
        if user_job:
            info_parts.append(f"职位：{user_job}")
        info_parts.append(f"性别：{user_gender}")
        if user_edu:
            info_parts.append(f"学历：{user_edu}")
        if info_parts:
            st.write("　|　".join(info_parts))

        if user_phone:
            st.write(f"电话：{user_phone}")
        if user_email:
            st.write(f"邮箱：{user_email}")

        st.write(f"出生日期：{user_birth}")

        if user_exp:
            st.write(f"工作经验：{user_exp} 年")

        if salary_low or salary_high:
            st.write(f"期望薪资：{salary_low or ''}-{salary_high or ''} 元".strip("-"))

        lang = []
        if lang_cn:
            lang.append("中文")
        if lang_en:
            lang.append("英语")
        if lang:
            st.write(f"语言能力：{', '.join(lang)}")

        if skills:
            st.write(f"技能：{', '.join(skills)}")

        if user_intro:
            st.write("个人简介：")
            st.write(user_intro)

        st.markdown("---")
        st.markdown("*在算法的世界里，你是最优解*")
