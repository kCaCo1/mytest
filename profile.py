import streamlit as st
import base64
from datetime import date, time

# 页面设置
st.set_page_config(
    page_title="个人简历生成器",
    page_icon="📝",
    layout="wide"
)

# 初始化session状态
if 'resume_data' not in st.session_state:
    st.session_state.resume_data = {
        "name": "",
        "job_title": "",
        "phone": "",
        "email": "",
        "birth_date": date(1990, 1, 1),
        "gender": "男",
        "education": "本科",
        "languages": [],
        "skills": [],
        "experience": 0,
        "salary_range": [10000, 20000],
        "about": "",
        "photo": None,
        "contact_time": time(9, 0),
    }

# 更新简历数据
def update_resume_data():
    st.session_state.resume_data = {
        "name": st.session_state.name,
        "job_title": st.session_state.job_title,
        "phone": st.session_state.phone,
        "email": st.session_state.email,
        "birth_date": st.session_state.birth_date,
        "gender": st.session_state.gender,
        "education": st.session_state.education,
        "languages": st.session_state.languages,
        "skills": st.session_state.skills,
        "experience": st.session_state.experience,
        "salary_range": st.session_state.salary_range,
        "about": st.session_state.about,
        "photo": st.session_state.photo,
        "contact_time": st.session_state.contact_time
    }

# 生成个性化标语
def generate_tagline():
    taglines = [
        "代码改变世界，你改变代码",
        "数据驱动决策，你驱动数据",
        "在算法的世界里，你是最优解",
        "从Bug中学习，在代码中成长",
        "不止是开发者，更是问题解决者"
    ]
    return random.choice(taglines)

# 主应用
def main():
    st.title("🎨 个人简历生成器")
    st.caption("使用Streamlit创建您的个性化简历")
    
    # 使用两列布局
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("个人信息表单", divider="blue")
        
        # 单行文本输入框 - 姓名
        st.text_input("姓名", key="name", on_change=update_resume_data)
        
        # 单行文本输入框 - 职位
        st.text_input("职位", key="job_title", on_change=update_resume_data)
        
        # 数字输入框 - 电话
        st.text_input("电话", key="phone", on_change=update_resume_data)
        
        # 单行文本输入框 - 邮箱
        st.text_input("邮箱", key="email", on_change=update_resume_data)
        
        # 日期选择 - 出生日期
        st.date_input("出生日期", key="birth_date", on_change=update_resume_data)
        
        # 单选按钮 - 性别
        st.radio("性别", ["男", "女", "其他"], key="gender", on_change=update_resume_data, horizontal=True)
        
        # 下拉按钮 - 学历
        st.selectbox("学历", ["高中", "专科", "本科", "硕士", "博士"], key="education", on_change=update_resume_data)
        
        # 多选下拉按钮 - 语言能力
        st.multiselect("语言能力", ["中文", "英语", "日语", "法语", "德语", "西班牙语"], 
                      key="languages", on_change=update_resume_data)
        
        # 复选框 - 技能
        skills = st.multiselect("技能（可多选）", 
                               ["Python", "Java", "JavaScript", "HTML/CSS", "SQL", 
                                "数据分析", "机器学习", "深度学习", "项目管理", "UI/UX设计"],
                               key="skills", on_change=update_resume_data)
        
        # 数值滑块 - 工作经验
        st.slider("工作经验（年）", 0, 30, key="experience", on_change=update_resume_data)
        
        # 范围选择滑块 - 期望薪资
        st.slider("期望薪资范围（元）", 5000, 50000, (10000, 20000), key="salary_range", on_change=update_resume_data)
        
        # 多行文本输入框 - 个人简介
        st.text_area("个人简介", height=150, key="about", on_change=update_resume_data,
                    placeholder="请简要介绍您的专业背景、职业目标和个人特点...")
        
        # 时间选择 - 最佳联系时间
        st.time_input("每日最佳联系时间段", key="contact_time", on_change=update_resume_data)
        
        # 文件上传 - 个人照片
        st.file_uploader("上传个人照片", type=["jpg", "jpeg", "png"], key="photo", on_change=update_resume_data)

    
    with col2:
        st.subheader("简历实时预览", divider="blue")
        
        # 显示简历预览
        resume_data = st.session_state.resume_data

        # 简历标题
        st.markdown(f'<h1 class="resume-title">{resume_data["name"]}</h1>', unsafe_allow_html=True)
        
        # 基本信息
        col_info1, col_info2 = st.columns([1, 1])
        
        with col_info1:
            # 显示照片
            if resume_data["photo"]:
                st.image(resume_data["photo"], width=200, output_format="JPEG")
            
            st.markdown(f'**职位**: {resume_data["job_title"]}')
            st.markdown(f'**电话**: {resume_data["phone"]}')
            st.markdown(f'**邮箱**: {resume_data["email"]}')
            st.markdown(f'**出生日期**: {resume_data["birth_date"].strftime("%Y/%m/%d")}')
        
        with col_info2:
            st.markdown(f'**性别**: {resume_data["gender"]}')
            st.markdown(f'**学历**: {resume_data["education"]}')
            st.markdown(f'**工作经验**: {resume_data["experience"]}年')
            st.markdown(f'**期望薪资**: {resume_data["salary_range"][0]} - {resume_data["salary_range"][1]}元')
            st.markdown(f'**最佳联系时间**: {resume_data["contact_time"].strftime("%H:%M")}')
            st.markdown(f'**语言能力**: {", ".join(resume_data["languages"])}')
        
        # 分隔线
        st.markdown("---")
        
        # 个人简介
        st.markdown('<div class="resume-section">', unsafe_allow_html=True)
        st.markdown('<h3 class="section-title">个人简介</h3>', unsafe_allow_html=True)
        st.markdown(f'<p>{resume_data["about"] or "这个人很神秘，没有留下任何介绍..."}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # 技能展示
        if resume_data["skills"]:
            st.markdown('<h3 class="section-title">专业技能</h3>', unsafe_allow_html=True)
            
            for skill in resume_data["skills"]:
                st.markdown(f'<div><strong>{skill}</strong></div>', unsafe_allow_html=True)

            
            st.markdown('</div>', unsafe_allow_html=True)

# 运行应用
if __name__ == "__main__":
    main()
