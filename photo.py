import streamlit as st

st.set_page_config(page_title='动物图鉴', page_icon='🦝')

# 在内存中初始化一个ind,当内存中没有'ind'的时候，才初始化
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 图片数组-装很多的图片

image_obj = [{
        'url': 'https://mindfulspirituallife.com/wp-content/uploads/2023/12/cat.jpg',
        'title': '猫'
    }, {
        'url': 'https://www.allaboutbirds.org/news/wp-content/uploads/2020/07/STanager-Shapiro-ML.jpg',
        'title': '鸟'
    }, {
        'url': 'https://a-z-animals.com/media/2023/02/shutterstock_2152176495.jpg',
        'title': '鱼'
    }]


st.image(image_obj[st.session_state['ind']]['url'], caption=image_obj[st.session_state['ind']]['title'])

def prevImg():
    # 点击上一张按钮要做的事
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(image_obj)

def nextImg():
    # 点击下一张按钮要做的事
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(image_obj)

c1, c2 = st.columns(2)

with c1:
    st.button('上一张', onclick=prevImg, use_container_width=True)

with c2:
    st.button('下一张', on_click=nextImg, use_container_width=True)
