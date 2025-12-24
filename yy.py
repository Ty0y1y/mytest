import streamlit as st

# 页面配置
st.set_page_config(page_title='简易音乐播放器', page_icon='🎵')

# 定义音乐数据（至少3首，包含音频链接、专辑封面、歌手、歌名）
music_data = [
{
"audio_url": "https://music.163.com/song/media/outer/url?id=5257138.mp3",
"cover_img": "https://p2.music.126.net/KiaSCEUjHb24zCc8ZOBzdw==/109951169869988111.jpg?param=130y130",
"singer": "周杰伦",
"song_name": "晴天"
},
{
"audio_url": "https://music.163.com/song/media/outer/url?id=1998109608.mp3",
"cover_img": "http://p1.music.126.net/UWzjTT2yGFz2tMY474Ogmg==/109951166656538970.jpg?param=120y120",
"singer": "陈伟霆",
"song_name": "Love U 2"
},
{
"audio_url": "https://music.163.com/song/media/outer/url?id=3330453731.mp3",
"cover_img": "https://p1.music.126.net/QQHZbNHk24nB6y4MijTL8Q==/109951169839449483.jpg?param=200y200",
"singer": "汪苏泷",
"song_name": "晴（live）"
}
]
total_musics = len(music_data)

# 初始化session_state，记录当前播放的音乐索引
if "current_idx" not in st.session_state:st.session_state.current_idx=0

# 定义“上一首”按钮逻辑
def prev_music():st.session_state.current_idx = (st.session_state.current_idx - 1) % total_musics

# 定义“下一首”按钮逻辑
def next_music():st.session_state.current_idx = (st.session_state.current_idx + 1) % total_musics

# 获取当前播放的音乐信息
current_music = music_data[st.session_state.current_idx]

# 页面标题
st.title("🎶 简易音乐播放器")
st.caption("支持歌曲切换，展示专辑封面/歌手/歌名")

# 布局：专辑封面 + 歌曲信息
col1, col2 = st.columns([1, 2])
with col1:st.image(current_music["cover_img"], caption="专辑封面", width=200)
with col2:st.subheader(current_music["song_name"])
st.write(f"**歌手**：{current_music['singer']}")

# 音频播放器
st.audio(current_music["audio_url"], format="audio/mp3")

# 切换按钮（彻底删除参数间的全角空格，直接用=连接）
btn_col1, btn_col2 = st.columns(2)
with btn_col1:st.button("⏮︎ 上一首",use_container_width=True,on_click=prev_music)
with btn_col2:st.button("⏭︎ 下一首",use_container_width=True,on_click=next_music)
