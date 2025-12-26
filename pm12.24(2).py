import streamlit as st
from datetime import date

st.set_page_config(page_title="个人简历生成器", layout="wide")
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
