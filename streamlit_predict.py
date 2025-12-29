# 第九章/streamlit_predict.py
import streamlit as st
import pickle
import pandas as pd

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
    format_data = [age, sex, bmi, bmi, children, smoke, region]

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

    format_data = [age, bmi, children, sex_female, sex_male,
                   smoke_no, smoke_yes,
                   region_northeast, region_southeast, region_northwest, region_southwest]

# 使用pickle的load方法从磁盘文件反序列化加载一个之前保存的随机森林回归模型
with open('rfr_model.pkl', 'rb') as f:
    rfr_model = pickle.load(f)

if submitted:
    format_data_df = pd.DataFrame(data=[format_data], columns=rfr_model.feature_names_in_)

    # 使用模型对格式化后的数据format_data进行预测,返回预测的医疗费用
    predict_result = rfr_model.predict(format_data_df)[0]

    st.write('根据您输入的数据，预测该客户的医疗费用是：', round(predict_result, 2))
