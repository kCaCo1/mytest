import streamlit as st
import pandas as pd

# 页面设置
st.set_page_config(page_title="南宁美食地图")
st.title("🍔 南宁美食探索")

# 介绍
st.markdown("""
探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。
""")

# 餐厅数据
restaurants = pd.DataFrame({
    "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "白妈螺狮粉"],
    "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
    "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
    "人均消费(元)": [15, 20, 25, 35, 50],
    "位置X": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
    "位置Y": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
})

# 1. 带点的地图 - 餐厅位置
st.header("📍 南宁美食地图")

# 创建简单地图
st.map(pd.DataFrame({
    "lat": restaurants["位置X"],
    "lon": restaurants["位置Y"],
    "餐厅": restaurants["餐厅"]
}))

# 2. 条形图 - 餐厅评分
st.header("⭐ 餐厅评分")
st.bar_chart(restaurants.set_index("餐厅")["评分"])

# 3. 折线图 - 价格趋势
st.header("💰 不同类型餐厅价格")
price_data = restaurants.groupby("类型")["人均消费(元)"].mean().reset_index()
st.line_chart(price_data.set_index("类型"))

# 4. 面积图 - 用餐高峰
st.header("⏱️ 用餐高峰时段")

# 创建时间数据
hours = [11, 12, 13, 17, 18, 19]
crowd_data = pd.DataFrame({
    "时间": hours,
    "星艺会尝不忘": [30, 95, 70, 40, 85, 60],
    "高峰柠檬鸭": [25, 85, 65, 35, 90, 65],
    "复记老友粉": [40, 80, 50, 45, 75, 55]
})

st.area_chart(crowd_data.set_index("时间"))

# 餐厅详情
st.header("🍽️ 餐厅详情")
selected_restaurant = st.selectbox("选择餐厅查看详情", restaurants["餐厅"])

if selected_restaurant:
    restaurant_info = restaurants[restaurants["餐厅"] == selected_restaurant].iloc[0]
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(restaurant_info["餐厅"])
        st.metric("评分", f"{restaurant_info['评分']}/5.0")
        st.metric("人均消费", f"{restaurant_info['人均消费(元)']}元")
        
    with col2:
        st.write("**推荐菜品**:")
        if restaurant_info["餐厅"] == "星艺会尝不忘":
            st.write("- 桂林米粉\n- 瘦肉粉\n- 干拌粉")
        elif restaurant_info["餐厅"] == "复记老友粉":
            st.write("- 老友牛肉\n- 老友猪肉\n- 炒粉")
        else:
            st.write("- 特色套餐\n- 地方小吃\n- 时令蔬菜")
    
    # 进度条表示拥挤程度
    st.subheader("当前拥挤程度")
    current_crowd = min(100, int(restaurant_info["评分"] * 20))  # 模拟当前拥挤度
    st.progress(current_crowd, text=f"{current_crowd}% 拥挤")

# 趣味功能
st.header("🎲 今日午餐推荐")
if st.button("帮我选午餐"):
    random_restaurant = restaurants.sample(1).iloc[0]
    st.success(f"今日推荐: {random_restaurant['餐厅']} ({random_restaurant['类型']})")
    st.image("https://img.shetu66.com/2023/06/12/1686543388597292.jpg", caption="美味午餐等着你！")
