import streamlit as st

def run_app_home():

    st.text('40대 이상의 건강검진정보를 통해 BMI(체질량지수)를 구해보고, 유저의 키, 몸무게를 입력하면 \nBMI를 구해주고 건강한 삶을 유지하는 법!을 알려줍니다.')
    st.image('https://img.freepik.com/free-vector/preventive-medicine-flat-set-with-people-having-medical-check-up-getting-test-results-isolated-vector-illustration_1284-74254.jpg?w=1380&t=st=1686100980~exp=1686101580~hmac=2b2267246178047bfbb2d08268c10017e21e5edfe9553d92bb9c556fc889391c', use_column_width=True,caption='작가 macrovector 출처 Freepik')
    st.subheader(':round_pushpin:건강검진정보란?')
    st.text('건강검진정보란 국민건강보험의 직장가입자와 40세 이상의 피부양자, 세대주인 지역가입자와 \n40세 이상의 지역가입자의 「일반검강검진」 결과와 이들 일반건강검진 대상자 중에 \n만 40세와 만 66세에 도달한 이들이 받게 되는「생애전환기건강진단」의 결과입니다.\n이 앱에서는 2020년도의 건강검진정보를 사용하였습니다.')
    with st.expander('건강검진이란?'):
        st.text('건강상태 확인과 질병의 예방 및 조기발견을 목적으로 건강검진기관을 통하여 \n진찰 및 상단, 이학적 검사, 진단검사, 병리검사, 영상의학 검사 등 의학적인 검진을 시행하는 것\n(건강검진기본법 제3조(정의) 제1호)')