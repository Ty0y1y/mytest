import streamlit as st

# 页面基础配置
st.set_page_config(page_title="视频中心", page_icon='📺')

# 初始化会话状态，用于记录当前播放集数索引
if 'ind' not in st.session_state:st.session_state['ind'] = 0

# 视频数据配置
video_data = [
{
"url": "https://www.w3school.com.cn/example/html5/mov_bbb.mp4",
"title": "还珠格格第一部-第1集",
"intro": "清朝乾隆年间，山东济南府有一位名叫夏紫薇的女子，为了寻找生父乾隆，带着丫鬟金锁远赴北京，途中结识了性格爽朗的小燕子，两人结为姐妹。小燕子为帮紫薇闯宫，却阴差阳错被乾隆认作义女，封为还珠格格。",
"cast": ["赵薇 饰 小燕子", "林心如 饰 夏紫薇", "苏有朋 饰 五阿哥永琪", "周杰 饰 福尔康"]
},
{
"url": "https://www.w3schools.com/html/movie.mp4",
"title": "还珠格格第一部-第2集",
"intro": "小燕子入宫后，因不懂宫中规矩闹出不少笑话，也与皇后等人产生矛盾。紫薇则在宫外焦急等待，尔康和永琪得知真相后，决定帮助紫薇认父。",
"cast": ["赵薇 饰 小燕子", "林心如 饰 夏紫薇", "苏有朋 饰 五阿哥永琪", "周杰 饰 福尔康"]
},
{
"url": "https://media.w3.org/2010/05/sintel/trailer.mp4",
"title": "还珠格格第一部-第3集",
"intro": "乾隆欲为小燕子指婚，小燕子情急之下说出真相，乾隆震怒。紫薇身份逐渐浮出水面，众人陷入危机，尔康等人设法帮助紫薇和小燕子化解危机。",
"cast": ["赵薇 饰 小燕子", "林心如 饰 夏紫薇", "苏有朋 饰 五阿哥永琪", "周杰 饰 福尔康"]
}
]

# 定义集数切换函数
def play_video(index):st.session_state['ind'] = index

# 页面标题
st.title(video_data[st.session_state['ind']]["title"])

# 视频播放区域
st.video(video_data[st.session_state['ind']]["url"], format="video/mp4")

# 剧集信息展示
with st.expander("剧集介绍", expanded=True):
    st.write(video_data[st.session_state['ind']]["intro"])
with st.expander("演职人员", expanded=False
):
    for actor in video_data[st.session_state['ind']]["cast"]:st.write(actor)

# 集数按钮
cols=st.columns(len(video_data))
for idx, col in enumerate(cols):
    with col:st.button(
label=f"第{idx + 1}集",
on_click=play_video,
args=(idx,),
use_container_width=True
)
