import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import io
import os

# -------------------------- 全局页面配置 --------------------------
st.set_page_config(
    page_title="多功能综合网站",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"  # 侧边栏默认展开
)

# -------------------------- 侧边栏导航 --------------------------
st.sidebar.title("📌 功能导航")
selected_module = st.sidebar.radio(
    "选择功能模块",
    [
        "首页",
        "南宁美食数据仪表",
        "图片切换展示",
        "个人简历生成器",
        "简易音乐播放器",
        "视频中心",
        "鹿晗个人档案"
    ]
)

# -------------------------- 各模块功能函数 --------------------------
# 1. 首页
def show_home():
    st.title("🌟 多功能综合网站")
    st.markdown("---")
    st.subheader("📋 网站功能简介")
    # 列容器展示功能分类
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("🍜 南宁美食数据仪表：展示南宁特色美食店铺、销量、价格等数据可视化")
    with col2:
        st.info("🖼️ 图片切换展示：支持上一张/下一张切换图片，查看不同素材")
    with col3:
        st.info("📝 个人简历生成器：填写信息实时生成简历预览，支持头像上传")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.info("🎶 简易音乐播放器：播放音乐，切换歌曲，展示信息")
    with col5:
        st.info("📺 视频中心：播放视频剧集，查看剧集介绍和演职人员信息")
    with col6:
        st.info("🌟 鹿晗个人档案：展示鹿晗的基础信息、能力矩阵、代表作品等")
    
    st.markdown("---")
    with st.expander("💡 使用说明（点击展开）", expanded=False):
        st.write("1. 左侧侧边栏选择需要使用的功能模块")
        st.write("2. 每个模块内按照提示操作，查看对应内容")
        st.write("3. 所有数据除公开信息外，模拟数据仅作展示使用")
        st.write("4. 上传文件仅在当前会话有效，不会存储到服务器")

# 2. 南宁美食数据仪表
def show_nanning_food():
    st.title("🍜 南宁美食数据仪表")
    # 数据准备
    restaurants_data = {
        "店名": ["复记老友粉", "舒记粉店", "邕味老友粉", "冰神糖水铺", "南铁螺蛳粉", "中山路八珍粉"],
        "地址": ["青秀区中山路", "兴宁区新民路", "江南区星光大道", "青秀区建政路", "西乡塘区南铁一街", "兴宁区中山路"],
        "评分": [4.8, 4.9, 4.7, 4.6, 4.8, 4.7],
        "人均消费(元)": [22, 25, 20, 15, 18, 23],
        "菜系": ["老友粉", "老友粉", "老友粉", "糖水", "螺蛳粉", "米粉"],
        "latitude": [22.8283, 22.8009, 22.7822, 22.8310, 22.8466, 22.8270],
        "longitude": [108.3222, 108.3786, 108.2682, 108.2408, 108.3593, 108.3230]
    }
    df_rest = pd.DataFrame(restaurants_data)

    months = [f"2024-{i+1:02d}" for i in range(12)]
    np.random.seed(42)
    price_trend = pd.DataFrame({
        "月份": months,
        "复记老友粉": [22, 22, 23, 23, 24, 24, 24, 25, 25, 25, 26, 26],
        "舒记粉店": [25, 25, 26, 26, 27, 27, 28, 28, 28, 29, 29, 30],
        "邕味老友粉": [20, 20, 21, 21, 22, 22, 22, 23, 23, 23, 24, 24],
        "冰神糖水铺": [15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19],
        "南铁螺蛳粉": [18, 18, 19, 19, 20, 20, 20, 21, 21, 21, 22, 22]
    })

    sales_data = pd.DataFrame({
        "菜系": ["老友粉", "螺蛳粉", "糖水", "米粉"],
        "月均销量(碗)": [12000, 9500, 8000, 7500]
    })

    # 选项卡分类展示
    tab1, tab2, tab3, tab4 = st.tabs(["店铺信息", "销量分析", "价格走势", "地理分布"])
    with tab1:
        st.subheader("📋 南宁特色美食店铺信息")
        st.dataframe(df_rest, use_container_width=True)
        with st.expander("评分&人均消费详情", expanded=False):
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("⭐ 店铺评分分布")
                st.area_chart(df_rest.set_index("店名")["评分"], use_container_width=True, color="#9b59b6")
            with col2:
                st.subheader("💰 人均消费对比")
                st.bar_chart(df_rest.set_index("店名")["人均消费(元)"], use_container_width=True, color="#3498db")
    
    with tab2:
        st.subheader("📈 菜系月均销量对比")
        st.bar_chart(sales_data.set_index("菜系"), use_container_width=True, color="#e67e22")
        with st.expander("销量数据说明", expanded=False):
            st.write("数据为2024年月均销量模拟值，老友粉因是南宁特色，销量领先；螺蛳粉、糖水次之。")
    
    with tab3:
        st.subheader("📊 12个月价格走势（2024）")
        st.line_chart(price_trend.set_index("月份"), use_container_width=True, 
                     color=["#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6"])
        with st.expander("价格走势分析", expanded=False):
            st.write("2024年各店铺价格整体呈缓慢上涨趋势，涨幅约5-10元，符合餐饮市场正常调价规律。")
    
    with tab4:
        st.subheader("🗺️ 店铺位置分布")
        st.map(df_rest[["latitude", "longitude"]], zoom=11)
        with st.expander("位置说明", expanded=False):
            st.write("坐标为南宁各区域大致经纬度，覆盖青秀区、兴宁区、江南区、西乡塘区等核心城区。")

    st.markdown("---")
    st.subheader("数据说明")
    st.markdown("1. 价格走势、销量数据为模拟值，仅作可视化展示；")
    st.markdown("2. 店铺坐标为南宁各区域大致经纬度；")
    st.markdown("3. 数据更新时间：2024年12月")

# 3. 图片切换展示
def show_image_switch():
    st.title("🖼️ 图片切换展示")
    # 图片数据
    image_list = [
        "https://gips3.baidu.com/it/u=2242344052,1569947099&fm=3074&app=3074&f=PNG?w=2560&h=1440", 
        "https://b0.bdstatic.com/ugc/3bX0D0itXngfFWB3-cLyfgba2a7a2a5b74d16a95e25db51dbe7a95.jpg@h_1280", 
        "https://img1.baidu.com/it/u=1864764111,2934688024&fm=253&app=138&f=JPEG?w=889&h=500"  
    ]
    caption_list = ["小狗", "袋鼠", "小猫"]
    
    # 初始化会话状态
    if "current_index" not in st.session_state:
        st.session_state.current_index = 0 
    
    # 居中展示图片
    col_center = st.columns([1,3,1])[1]
    with col_center:
        st.image(
            image_list[st.session_state.current_index],
            caption=caption_list[st.session_state.current_index],  
            width=700
        )
    
    # 切换按钮（列容器布局）
    col_btn1, col_btn2 = st.columns([2,2])
    with col_btn1:
        if st.button("⬅️ 上一张", use_container_width=True):
            if st.session_state.current_index > 0:
                st.session_state.current_index -= 1
    with col_btn2:
        if st.button("下一张 ➡️", use_container_width=True):
            if st.session_state.current_index < len(image_list) - 1:
                st.session_state.current_index += 1
    
    with st.expander("图片信息说明", expanded=False):
        st.write(f"当前图片：{st.session_state.current_index + 1}/{len(image_list)}")
        st.write("图片来源为网络公开素材，仅作展示使用。")

# 4. 个人简历生成器
def show_resume_builder():
    st.title("📝 个人简历生成器")
    # 左右列布局
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("📝 个人信息表单")
        # 基础信息录入
        name = st.text_input("姓名", key="name")
        position = st.text_input("职位", key="position")
        phone = st.text_input("电话", key="phone")
        email = st.text_input("邮箱", key="email")
        birth_date = st.date_input("出生日期", value=None, key="birth_date")
        gender = st.radio("性别", ["男", "女", "其他"], index=0, key="gender")
        education = st.selectbox("学历", ["本科", "硕士", "博士"], index=0, key="education")
        
        languages = st.multiselect("语言能力", ["中文", "英语", "西班牙语","德语","法语"], key="languages")
        skills = st.multiselect("技能（可多选）", 
                               ["Java", "HTML/CSS", "机器学习", "Python", "SQL", "C++"], 
                               key="skills")
        work_years = st.slider("工作经验（年）", 0, 30, key="work_years")
        salary_range = st.slider("期望薪资范围（元）", 5000, 50000, (10000, 20000), key="salary_range")
        bio = st.text_area("个人简介", key="bio")
        max_online_time = st.number_input(
            "每日最长联系时间（分钟）",
            min_value=1, max_value=24*60, value=120, step=15, key="max_online_time"
        )
        
        # 头像上传
        uploaded_file = st.file_uploader("上传个人照片", type=["jpg", "jpeg", "png"], key="avatar")
        if uploaded_file is not None:
            try:
                image = Image.open(uploaded_file)
                st.image(image, caption="上传的头像", use_container_width=True)
            except Exception as e:
                st.error(f"图片加载失败: {str(e)}")
        else:
            # 在线默认头像（避免本地文件依赖）
            default_avatar = "https://via.placeholder.com/150/CCCCCC/FFFFFF?text=默认头像"
            st.image(default_avatar, caption="默认头像", use_container_width=True)

    with col2:
        st.subheader("📄 简历实时预览")
        with st.expander("展开简历预览", expanded=True):
            # 姓名
            st.markdown(f"<h1 style='color: #00c8ff; font-size: 28px;'>{name if name else '请填写姓名'}</h1>", unsafe_allow_html=True)
            
            # 头像
            if uploaded_file is not None:
                try:
                    image = Image.open(uploaded_file)
                    st.image(image, width=120, use_container_width=False)
                except:
                    pass 
            else:
                st.image("https://via.placeholder.com/120/CCCCCC/FFFFFF?text=头像", width=120)

            # 个人信息子列
            col_a, col_b = st.columns(2)
            with col_a:
                st.write("**性别**: ", gender)
                st.write("**学历**: ", education)
                st.write("**工作年限**: ", work_years, "年")
                st.write("**最佳联系时间**: ", max_online_time, "分钟")
            with col_b:
                st.write("**职位**: ", position if position else "未填写")
                st.write("**电话**: ", phone if phone else "未填写")
                st.write("**邮箱**: ", email if email else "未填写")
                st.write("**出生日期**: ", birth_date.strftime("%Y/%m/%d") if birth_date else "未填写")

            # 技能展示
            st.markdown("---")
            st.subheader("🛠️ 专业技能")
            if skills:
                for skill in skills:
                    st.markdown(f"• <span style='color: #00c8ff;'>{skill}</span>", unsafe_allow_html=True)
            else:
                st.write("未填写技能信息")

            # 个人简介
            st.markdown("---")
            st.subheader("📝 个人简介")
            st.markdown(bio if bio else "未填写个人简介")

            # 薪资范围
            st.markdown("---")
            st.markdown(f"<p style='color: #00c8ff; font-weight: bold;'>期望薪资范围: {salary_range[0]} - {salary_range[1]} 元</p>", unsafe_allow_html=True)

            # 结尾标语
            st.markdown("<div style='text-align: right; color: #66ccff; font-style: italic; font-size: 0.9em;'>你是最棒滴！ ✨</div>", unsafe_allow_html=True)

# 5. 简易音乐播放器
def show_music_player():
    st.title("🎶 简易音乐播放器")
    st.caption("支持歌曲切换，展示专辑封面/歌手/歌名")
    
    # 音乐数据
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

    # 初始化会话状态
    if "current_idx" not in st.session_state:
        st.session_state.current_idx=0

    # 切换函数
    def prev_music():
        st.session_state.current_idx = (st.session_state.current_idx - 1) % total_musics
    def next_music():
        st.session_state.current_idx = (st.session_state.current_idx + 1) % total_musics

    # 当前音乐信息
    current_music = music_data[st.session_state.current_idx]

    # 列布局展示封面+播放区
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(current_music["cover_img"], caption="专辑封面", width=200)
        with st.expander("歌曲详情", expanded=False):
            st.write(f"歌曲：{current_music['song_name']}")
            st.write(f"歌手：{current_music['singer']}")
            st.write(f"进度：{st.session_state.current_idx + 1}/{total_musics}")
    with col2:
        st.subheader(current_music["song_name"])
        st.write(f"**歌手**：{current_music['singer']}")
        st.audio(current_music["audio_url"], format="audio/mp3")
        # 切换按钮
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            st.button("⏮︎ 上一首",use_container_width=True,on_click=prev_music)
        with btn_col2:
            st.button("⏭︎ 下一首",use_container_width=True,on_click=next_music)

# 6. 视频中心
def show_video_center():
    st.title("📺 视频中心")
    # 初始化会话状态
    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0

    # 视频数据
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

    # 切换函数
    def play_video(index):
        st.session_state['ind'] = index

    # 选项卡分播放区和信息区
    tab1, tab2 = st.tabs(["视频播放", "剧集信息"])
    with tab1:
        st.subheader(video_data[st.session_state['ind']]["title"])
        st.video(video_data[st.session_state['ind']]["url"], format="video/mp4")
        # 集数按钮
        cols=st.columns(len(video_data))
        for idx, col in enumerate(cols):
            with col:
                st.button(
                label=f"第{idx + 1}集",
                on_click=play_video,
                args=(idx,),
                use_container_width=True
                )
    with tab2:
        st.subheader("剧集详情")
        with st.expander(f"《{video_data[st.session_state['ind']]['title']}》介绍", expanded=True):
            st.write(video_data[st.session_state['ind']]["intro"])
        with st.expander("演职人员", expanded=False):
            for actor in video_data[st.session_state['ind']]["cast"]:
                st.write(actor)
        st.subheader("全部剧集")
        for i, vid in enumerate(video_data):
            st.write(f"{i+1}. {vid['title']}")

# 7. 鹿晗个人档案
def show_luhan_profile():
    st.title("🌟 鹿晗 - 个人档案")
    
    # 列布局展示信息+头像
    col_info, col_avatar = st.columns([2, 1])  
    with col_info:
        st.header("📝 基础信息")
        with st.expander("展开完整信息", expanded=True):
            st.text("姓名：鹿晗")
            st.text("昵称：小鹿、晗晗")
            st.text("出生日期：1990年4月20日（白羊座）")
            st.text("出生地：北京市海淀区")
            st.text("毕业院校：首尔艺术大学实用音乐艺术系（休学）")
            st.text("职业：中国内地男歌手、演员、音乐制作人")
            st.text("出道节点：2012年以EXO/EXO-M成员身份正式出道")
            st.text("核心标签：歌手 | 演员 | 足球爱好者 | 音乐制作人")
            st.text("当前状态：活跃 🟢")

    with col_avatar:
        avatar_url = "https://img2.baidu.com/it/u=403208745,1674665629&fm=253&app=138&f=JPEG?w=800&h=1200"
        st.image(avatar_url, width=180)
        with st.expander("头像说明", expanded=False):
            st.write("图片来源为网络公开素材，仅作展示使用。")

    # 核心能力矩阵（列布局）
    st.header("📊 核心能力矩阵")
    col1, col2, col3 = st.columns(3)  
    with col1:
        st.metric(label="音乐创作/演唱", value="95%", delta="↑3%")
        with st.expander("能力说明", expanded=False):
            st.write("鹿晗的音乐作品风格多样，演唱功底扎实，创作能力持续提升。")
    with col2:
        st.metric(label="影视表演", value="80%", delta="↑1%")
        with st.expander("能力说明", expanded=False):
            st.write("从早期作品到《穿越火线》等，演技逐步打磨，角色塑造能力提升。")
    with col3:
        st.metric(label="足球技能", value="90%", delta="→0%")
        with st.expander("能力说明", expanded=False):
            st.write("资深足球爱好者，曾担任青少年足球发展推广大使，球技稳定。")

    # 近期任务日志
    st.header("📅 近期任务日志")
    task_data = {
        "日期": ["2025-01-10", "2025-04-20", "2025-07-05"],
        "任务名称": ["鹿晗2025巡演·北京站", "35岁生日音乐会", "全新个人专辑制作"],
        "状态": ["🟢 已完成", "🟡 进行中", "🔴 待启动"],
        "难度评级": ["★★★★★", "★★★☆☆", "★★★★☆"]
    }
    task_df = pd.DataFrame(task_data)
    st.table(task_df)
    with st.expander("任务说明", expanded=False):
        st.write("任务日志为2025年规划模拟数据，仅作展示使用。")

    # 代表作品与成就
    st.header("🏆 代表作品与关键成就")
    work_achievement = """
# 代表作品（音乐/影视）
1. 音乐作品：
   - 专辑：《Reloaded》《Xplore》《π-volume.1》
   - 单曲：《勋章》《致爱Your Song》《我们的明天》《慢慢》
2. 影视作品：
   - 电视剧：《择天记》《穿越火线》《在劫难逃》
   - 电影：《重返20岁》《我是证人》《长城》《上海堡垒》
3. 综艺：《奔跑吧》（常驻）、《创造营2020》（导师）

# 关键成就
1. 2014年：第22届MTV欧洲音乐奖 最佳中国艺人
2. 2016年：亚洲音乐盛典 年度最佳男歌手
3. 2017年：全球华语歌曲排行榜 最佳全能艺人
4. 2019年：微博之夜 年度全能艺人
5. 2023-2025年：连续担任中国青少年足球发展推广大使
    """
    st.code(work_achievement, language="plaintext")

    st.markdown("---")
    st.markdown("🖥️ 系统提示：鹿晗2025巡演·上海站门票预售信息已同步至云端")
    st.markdown("⏰ 数据更新时间：2025-12-18 17:30:00")
    st.markdown("当前状态：在线 | 数据已备份")

# -------------------------- 主逻辑：根据选择调用对应模块 --------------------------
if selected_module == "首页":
    show_home()
elif selected_module == "南宁美食数据仪表":
    show_nanning_food()
elif selected_module == "图片切换展示":
    show_image_switch()
elif selected_module == "个人简历生成器":
    show_resume_builder()
elif selected_module == "简易音乐播放器":
    show_music_player()
elif selected_module == "视频中心":
    show_video_center()
elif selected_module == "鹿晗个人档案":
    show_luhan_profile()
