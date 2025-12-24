import streamlit as st
from PIL import Image
import io
import os
import urllib.request

# 设置页面配置
st.set_page_config(
    page_title="个人简历生成器",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 主体布局：左右两栏
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📝 个人信息表单")

    # 基本信息
    name = st.text_input("姓名",key="name")
    position = st.text_input("职位",key="position")
    phone = st.text_input("电话",key="phone")
    email = st.text_input("邮箱",key="email")
    birth_date = st.date_input("出生日期", value=None, key="birth_date")
    gender = st.radio("性别", ["男", "女", "其他"], index=0, key="gender")
    education = st.selectbox("学历", ["本科", "硕士", "博士"], index=0, key="education")
    
    # 语言能力（多选）
    languages = st.multiselect("语言能力", ["中文", "英语", "西班牙语","德语","法语"], key="languages")
    
    # 技能（多选）
    skills = st.multiselect("技能（可多选）", 
                           ["Java", "HTML/CSS", "机器学习", "Python", "SQL", "C++"], 
                           key="skills")
    
    # 工作经验（滑块，范围0-30年）
    work_years = st.slider("工作经验（年）", 0, 30, key="work_years")
    
    # 薪资范围（滑块，单位：元）
    salary_range = st.slider("期望薪资范围（元）", 5000, 50000, (10000, 20000), key="salary_range")
    
    # 个人简介
    bio = st.text_area("个人简介", """

""", key="bio")
    
    # 修正：每日最长联系时间
    max_online_time = st.number_input(
        "每日最长联系时间（分钟）",
        min_value=1,
        max_value=24 * 60,  
        value=120,          
        step=15,
        key="max_online_time"
    )
    
    # 头像上传
    uploaded_file = st.file_uploader("上传个人照片", type=["jpg", "jpeg", "png"], accept_multiple_files=False, key="avatar")
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="上传的头像", use_container_width=True)
        except Exception as e:
            st.error(f"图片加载失败: {str(e)}")
    else:
        # 检查本地文件是否存在，不存在则使用在线占位图
        if os.path.exists("default.png"):
            st.image("default.png", caption="默认头像", use_container_width=True) 

with col2:
    st.subheader("📄 简历实时预览")

    # 顶部姓名和头像
    st.markdown(f"<h1 style='color: #00c8ff; font-size: 28px;'>{name}</h1>", unsafe_allow_html=True)
    # 头像
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, width=120, use_container_width=False)
        except:
                pass 

    # 个人信息（两栏布局）
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("**性别**: ", gender)
        st.write("**学历**: ", education)
        st.write("**工作年限**: ", work_years, "年")
        st.write("**最佳联系时间**: ", max_online_time, "分钟")
    with col_b:
        st.write("**职位**: ", position)
        st.write("**电话**: ", phone)
        st.write("**邮箱**: ", email)
        st.write("**出生日期**: ", birth_date.strftime("%Y/%m/%d") if birth_date else "未填写")

    # 技能展示
    st.markdown("---")
    st.subheader("🛠️ 专业技能")
    for skill in skills:
        st.markdown(f"• <span style='color: #00c8ff;'>{skill}</span>", unsafe_allow_html=True)

    # 个人简介
    st.markdown("---")
    st.subheader("📝 个人简介")
    st.markdown(bio)

    # 薪资范围（带颜色提示）
    st.markdown("---")
    st.markdown(f"<p style='color: #00c8ff; font-weight: bold;'>期望薪资范围: {salary_range[0]} - {salary_range[1]} 元</p>", unsafe_allow_html=True)

    # 结尾标语
    st.markdown("<div style='text-align: right; color: #66ccff; font-style: italic; font-size: 0.9em;'>哈哈哈，你是最棒滴！ ✨</div>", unsafe_allow_html=True)
