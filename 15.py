import streamlit as st
import pandas as pd

# 页面基础配置：宽布局、折叠侧边栏、自定义标题
st.set_page_config(
    page_title="学生数字档案",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 自定义CSS样式：美化组件+表格列级颜色控制
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
    /* 任务日志表格基础样式 */
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
    /* 表格列级颜色定义 */
    .task-table th:nth-child(1), .task-table td:nth-child(1) {
        color: #1E90FF !important; /* 日期：蓝色 */
        font-weight: bold;
    }
    .task-table th:nth-child(2), .task-table td:nth-child(2) {
        color: #32CD32 !important; /* 任务：绿色 */
    }
    .task-table th:nth-child(3), .task-table td:nth-child(3) {
        color: #FFD700 !important; /* 状态：金黄色 */
        font-weight: bold;
    }
    .task-table th:nth-child(4), .task-table td:nth-child(4) {
        color: #FF6347 !important; /* 难度：番茄红 */
    }
    /* 底部系统标签绿色样式 */
    .system-label {
        color: #27ae60 !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)


# 页面主标题：科幻风格样式
st.markdown("<h1 class='title'>--- 学生 小唐and小潘 数字档案 ---</h1>", unsafe_allow_html=True)
st.write("")  # 空行分隔，优化视觉间距


# 基础信息模块：展示学生核心信息，关键内容高亮
st.markdown("<h3 class='header'>🔑基础信息</h3>", unsafe_allow_html=True)
st.write("""
    学生ID:<span style='color:#27ae60'> 22053040222 and 22053040209 </span>
    <br>
    注册时间:<span style='color:#27ae60'> 2025-12-18 15:11:11 </span> | 精神状态: <span style='color:#27ae60'>✅正常</span>
    <br>
    当前位置: <span style='color:#e67e22'>实训楼710</span>  | 安全等级: <span style='color:#e67e22'>机密</span>
""", unsafe_allow_html=True)
st.write("")


# 技能矩阵模块：三列布局展示编程语言掌握度
st.markdown("<h3 class='header'>📊技能矩阵</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)  # 分三列展示指标

with col1:
    st.metric(
        label="C++",
        value="95%",
        delta="+3%"  # 环比变化值
    )

with col2:
    st.metric(
        label="Python",
        value="87%",
        delta="-2%"
    )

with col3:
    st.metric(
        label="Java",
        value="68%",
        delta="-10%"
    )


# 课程进度模块：展示Streamlit学习进度条
st.markdown("<h3 class='header'>Streamlit课程进度</h3>", unsafe_allow_html=True)
st.progress(40)  # 进度条值：40%


# 任务日志模块：HTML表格展示任务信息，自定义列颜色
st.markdown("<h3 class='header'>📅任务日志</h3>", unsafe_allow_html=True)
# 构造任务日志数据
task_data = {
    "日期": ["2023-10-01", "2023-10-12", "2023-10-22"],
    "任务": ["学生数字档案", "成绩管理系统", "数据可视化展示"],
    "状态": ["✅ 已完成", "🕣 进行中", "❌ 未完成"],
    "难度": ["★★☆☆☆", "★★★☆☆", "★★★★☆"]
}
task_df = pd.DataFrame(task_data)

# 将DataFrame转为带自定义样式的HTML表格（解决原生表格样式覆盖问题）
html_table = f"""
<table class="task-table">
    <thead>
        <tr>
            <th>日期</th>
            <th>任务</th>
            <th>状态</th>
            <th>难度</th>
        </tr>
    </thead>
    <tbody>
        {''.join([
            f'<tr><td>{row.日期}</td><td>{row.任务}</td><td>{row.状态}</td><td>{row.难度}</td></tr>'
            for _, row in task_df.iterrows()  # 遍历DataFrame生成表格行
        ])}
    </tbody>
</table>
"""
st.markdown(html_table, unsafe_allow_html=True)


# 代码成果模块：展示核心代码片段
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
st.code(code_content, language="python")  # 语法高亮展示Python代码


# 底部系统信息：英文标签绿色高亮+强制换行
st.write("")
st.markdown("""
    <div>
        > <span class="system-label">SYSTEM MESSAGE</span>: 下一个任务已刷新信息。<br>
        > <span class="system-label">SYSTEM</span>: 请留意系统<br>
        > <span class="system-label">CONTROL</span>: 2025-12-18 16:00:58<br>
        > <span class="system-label">系统状态</span>: 在线 连接状态: 已加密
    </div>
""", unsafe_allow_html=True)
