import streamlit as st

# 1. 页面基础配置
st.set_page_config(page_title="图片切换展示", layout="centered")

# 2. 页面内标题
st.title("图片切换展示")

# 3. 准备图片资源
image_list = [
    "https://gips3.baidu.com/it/u=2242344052,1569947099&fm=3074&app=3074&f=PNG?w=2560&h=1440", 
    "https://b0.bdstatic.com/ugc/3bX0D0itXngfFWB3-cLyfgba2a7a2a5b74d16a95e25db51dbe7a95.jpg@h_1280", 
    "https://img1.baidu.com/it/u=1864764111,2934688024&fm=253&app=138&f=JPEG?w=889&h=500"  
]
# 对应每张图片的标注文本（图片下方的“标题”）
caption_list = ["小狗", "袋鼠", "小猫"]

# 4. 初始化会话状态
if "current_index" not in st.session_state:
    st.session_state.current_index = 0 

# 5. 展示图片
st.image(
    image_list[st.session_state.current_index],
    caption=caption_list[st.session_state.current_index],  
    width=700
)

# 6. 切换按钮
col1, col2 = st.columns(2)
with col1:
    if st.button("上一张",use_container_width=True):
        if st.session_state.current_index > 0:
            st.session_state.current_index -= 1
with col2:
    if st.button("下一张",use_container_width=True):
        if st.session_state.current_index < len(image_list) - 1:
            st.session_state.current_index += 1
