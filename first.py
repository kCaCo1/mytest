import streamlit as st
import random
import time
from PIL import Image
import base64

# ======================
# 音乐播放器实现
# ======================
def music_player():
    st.subheader("🎵 动态音乐播放器", divider="rainbow")
    
    # 音乐库 (实际使用时替换为真实文件路径)
    music_library = [
        {"title": "Bohemian Rhapsody", "artist": "Queen", "cover": "queen.jpg", "file": "queen.mp3"},
        {"title": "Blinding Lights", "artist": "The Weeknd", "cover": "weeknd.jpg", "file": "weeknd.mp3"},
        {"title": "Shape of You", "artist": "Ed Sheeran", "cover": "ed.jpg", "file": "ed.mp3"},
        {"title": "Dynamite", "artist": "BTS", "cover": "bts.jpg", "file": "bts.mp3"}
    ]
    
    # 初始化session状态
    if 'current_song' not in st.session_state:
        st.session_state.current_song = 0
    if 'playback_time' not in st.session_state:
        st.session_state.playback_time = 0
    
    # 切歌函数
    def next_song():
        st.session_state.current_song = (st.session_state.current_song + 1) % len(music_library)
        st.session_state.playback_time = 0
    
    def prev_song():
        st.session_state.current_song = (st.session_state.current_song - 1) % len(music_library)
        st.session_state.playback_time = 0
    
    def random_song():
        new_song = st.session_state.current_song
        while new_song == st.session_state.current_song:
            new_song = random.randint(0, len(music_library)-1)
        st.session_state.current_song = new_song
        st.session_state.playback_time = 0
    
    # 自定义CSS动画
    st.markdown("""
    <style>
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .pulse-animation {
        animation: pulse 0.5s ease-in-out;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # 获取当前歌曲信息
    current = st.session_state.current_song
    song = music_library[current]
    
    # 创建布局
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # 专辑封面 (带动画效果)
        album_art = st.empty()
        album_art.image(
            song["cover"], 
            caption=f"当前播放: {song['title']}", 
            use_column_width=True
        )
        st.markdown(
            f"<script>document.querySelector('.stImage').parentElement.classList.add('pulse-animation')</script>",
            unsafe_allow_html=True
        )
    
    with col2:
        # 歌曲信息
        st.header(song["title"])
        st.subheader(f"歌手: {song['artist']}")
        st.progress((st.session_state.playback_time % 10) / 10)
        
        # 音频播放器
        audio_placeholder = st.empty()
        audio_bytes = open(f"./media/{song['file']}", "rb").read()
        audio_placeholder.audio(audio_bytes, start_time=int(st.session_state.playback_time))
        
        # 控制按钮
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        with col_btn1:
            st.button("⏮ 上一首", on_click=prev_song, use_container_width=True)
        with col_btn2:
            st.button("▶️ 播放/暂停", key="play_pause", use_container_width=True)
        with col_btn3:
            st.button("⏭ 下一首", on_click=next_song, use_container_width=True)
        
        # 随机播放按钮
        if st.button("🎲 随机播放", on_click=random_song, use_container_width=True):
            st.balloons()
        
        # 音量控制
        volume = st.slider("音量", 0, 100, 80, key="volume")
    
    # 模拟播放进度
    if "play_pause" in st.session_state and not st.session_state.get("paused", False):
        st.session_state.playback_time += 0.5
        time.sleep(0.5)
        st.rerun()

# ======================
# MV视频播放器实现
# ======================
def video_player():
    st.subheader("🎬 MV视频播放器", divider="rainbow")
    
    # 视频库 (实际使用时替换为真实文件路径)
    video_library = {
        "Dynamite - BTS": {"file": "bts.mp4", "duration": "3:45", "director": "YongSeok"},
        "Bad Guy - Billie Eilish": {"file": "billie.mp4", "duration": "3:32", "director": "Dave Meyers"},
        "Kill This Love - BLACKPINK": {"file": "blackpink.mp4", "duration": "3:33", "director": "Seo Hyun"},
        "Uptown Funk - Mark Ronson": {"file": "uptown.mp4", "duration": "4:22", "director": "Bruno Mars"}
    }
    
    # 彩蛋视频
    easter_egg = {"file": "easter_egg.mp4", "duration": "0:30", "director": "神秘人"}
    
    # 选择视频
    selected = st.selectbox(
        "选择MV视频", 
        list(video_library.keys()),
        index=0,
        key="video_select"
    )
    
    # 获取视频信息
    video_info = video_library[selected]
    
    # 视频播放器
    st.video(f"./media/{video_info['file']}")
    
    # 视频信息卡片
    st.info(f"""
    **视频信息**  
    🎬 标题: {selected}  
    ⏱️ 时长: {video_info['duration']}  
    🎥 导演: {video_info['director']}
    """)
    
    # 彩蛋模式
    with st.expander("🎁 彩蛋模式"):
        code = st.text_input("输入神秘代码解锁隐藏视频", type="password")
        if code == "STREAMLIT_ROCKS":
            st.success("🎉 恭喜解锁隐藏视频!")
            st.video("./media/easter_egg.mp4")
            st.balloons()
        elif code != "":
            st.error("❌ 密码错误，再试试吧!")
    
    # 歌词同步功能
    if selected.startswith("Dynamite"):
        lyrics = [
            (0, 5, "'Cause I-I-I'm in the stars tonight"),
            (6, 11, "So watch me bring the fire and set the night alight"),
            (12, 17, "Shoes on, get up in the morn'"),
            (18, 23, "Cup of milk, let's rock and roll")
        ]
        
        st.caption("🎤 动态歌词")
        lyric_display = st.empty()
        current_time = time.time() % 24
        
        for start, end, text in lyrics:
            if start <= current_time < end:
                lyric_display.markdown(f"### 🎶 {text}")
                break
        else:
            lyric_display.markdown("### 🎵 音乐间隙...")

# ======================
# 主应用界面
# ======================
st.title("🎧 Python多媒体播放器实验室")
st.caption("Streamlit多媒体展示实战练习")

# 创建选项卡
tab1, tab2 = st.tabs(["音乐播放器", "MV视频播放器"])

with tab1:
    music_player()

with tab2:
    video_player()

# 侧边栏说明
with st.sidebar:
    st.header("课堂练习说明")
    st.markdown("""
    ### 练习目标
    1. 实现交互式音乐播放器
    2. 创建MV视频播放器
    3. 掌握Streamlit多媒体组件使用
    
    ### 创新功能
    - 专辑封面动画效果
    - 随机播放/切歌功能
    - 动态歌词同步
    - 彩蛋隐藏视频
    - 播放进度模拟
    
    ### 使用说明
    1. 创建`media`文件夹存放多媒体文件
    2. 替换代码中的示例文件名
    3. 彩蛋密码: `STREAMLIT_ROCKS`
    """)
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)