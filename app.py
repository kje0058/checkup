import streamlit as st
from app_home import run_app_home
from app_eda import run_app_eda
from app_bmi import run_app_bmi

def main():

    st.title(':woman-running:건강 Dream 행복 Dream:man-running:')

    menu = ['🏠Home', '📝EDA', '👗BMI']

    st.sidebar.header('건강한 하루되세요:muscle:')
    choice = st.sidebar.selectbox('📌메뉴', menu)
    st.sidebar.image("https://img.freepik.com/free-vector/patient-taking-a-medical-examination-in-a-clinic_52683-57136.jpg?w=826&t=st=1686098847~exp=1686099447~hmac=efc82849049c1abbcacf4d2eb917926b6ba87b8ab36c2dc2d41f562adb792467", use_column_width=True, caption='작가 pikisuperstar 출처 Freepik')

    if choice == menu[0] :
        run_app_home()
    elif choice == menu[1] :
        run_app_eda()
    else :
        run_app_bmi()

if __name__ == '__main__':
    main()