import streamlit as st
#运用表单和表单提交按钮
with st.form('user_inputs'):
    age=st.number_input('年龄',min_value=0)
    sex=st.radio('性别',options=['男性','女性'])
    bmi=st.number_input('BMI',min_value=0.0)
    children=st.number_input("子女数量：",step=1,min_value=0)
    smoke=st.radio("是否吸烟",("是","否"))
    region=st.selectbox('区域',('东南部','西南部','东北部','西北部'))
    submitted=st.form_submit_button('预测费用')
if submitted:
    format_data=[age,sex,bmi,children,smoke,region]
    st.write('用户输入的数据是：')
    st.text(format_data)
