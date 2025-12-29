# 第九章/streamlit_input_format.py
import streamlit as st

# 运用表单和表单提交按钮
with st.form('user_inputs'):
    age = st.number_input('年龄', min_value=0)
    sex = st.radio('性别', options=['男性', '女性'])
    bmi = st.number_input('BMI', min_value=0.0)

    children = st.number_input("子女数量: ", step=1, min_value=0)
    smoke = st.radio("是否吸烟", ("是", "否"))
    region = st.selectbox('区域', ('东南部', '西南部', '东北部', '西北部'))
    submitted = st.form_submit_button('预测费用')
if submitted:
    format_data = [age, sex, bmi, children, smoke, region]
    st.write('用户输入的数据是：')
    st.text(format_data)

    # 初始化数据预处理格式中岛屿相关的变量
    sex_female, sex_male = 0, 0
    # 根据用户输入的性别数据，更改对应的值
    if sex == '女性':
        sex_female = 1
    elif sex == '男性':
        sex_male = 1

    smoke_yes, smoke_no = 0, 0
    # 根据用户输入的吸烟数据，更改对应的值
    if smoke == '是':
        smoke_yes = 1
    elif smoke == '否':
        smoke_no = 1

    region_northeast, region_southeast, region_northwest, region_southwest = 0, 0, 0, 0
    # 根据用户输入的岛屿数据，更改对应的值
    if region == '东北部':
        region_northeast = 1
    elif region == '东南部':
        region_southeast = 1
    elif region == '西北部':
        region_northwest = 1
    elif region == '西南部':
        region_southwest = 1

    st.write('转换为数据预处理的格式：')
    format_data = [age, bmi, children, sex_female, sex_male,
                   smoke_no, smoke_yes,
                   region_northeast, region_southeast, region_northwest, region_southwest]
    st.text(format_data)
