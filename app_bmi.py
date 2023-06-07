import streamlit as st
import pandas as pd
import platform
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc
import plotly.graph_objects as go
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False
sns.set(font="Malgun Gothic", 
        rc={"axes.unicode_minus":False},
        style='darkgrid')
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

def run_app_bmi() :
    tab1, tab2 = st.tabs([':page_facing_up: BMI 분석', ':bar_chart: BMI 측정'])
    with tab1:
        df=pd.read_csv('data/checkup_2020.CSV', encoding='cp949')
        df_new = df.iloc[:,3:8]
        df_new['음주여부'] = df['음주여부']
        df_new['흡연상태'] = df['흡연상태']
        df_new['식전혈당(공복혈당)'] = df['식전혈당(공복혈당)']
        df_new['수축기 혈압'] = df['수축기 혈압']
        df_new['BMI'] = round(df_new['체중(5Kg 단위)'] / (df_new['신장(5Cm단위)']/100) / (df_new['신장(5Cm단위)']/100),2)
        df_new.dropna(inplace=True)
        BMI_list=[0,1,2,3]
        bins=[0,18.5,24.9,29.9,60.0]
        df_new['BMI_bins'] = pd.cut(df_new['BMI'], bins, labels=BMI_list)
        df_new['흡연상태']=df_new['흡연상태'].replace({1:0, 2:1, 3:2}).astype(int)
        df_new['음주여부']=df_new['음주여부'].astype(int)
        df_new['식전혈당(공복혈당)']=df_new['식전혈당(공복혈당)'].astype(int)
        df_new['수축기 혈압']=df_new['수축기 혈압'].astype(int)
        df_new['성별코드']=df_new['성별코드'].replace({2:0}).astype(int)
        df_new['연령대 코드(5세단위)']=df_new['연령대 코드(5세단위)'].replace({9:0, 10:0, 11:1, 12:1, 13:2, 14:2, 15:3, 16:3, 17:4, 18:4}).astype(int)
        df_new.rename(columns={'연령대 코드(5세단위)':'연령대 코드(10세단위)'}, inplace=True)
        df_new['BMI_bins'] = df_new['BMI_bins'].astype('int64')
        df_new['허리둘레'].replace({680:df_new['허리둘레'].mean(),999:df_new['허리둘레'].mean()},inplace=True)
        df_new['허리둘레'].replace({8.7:df_new['허리둘레'].mean(),5.8:df_new['허리둘레'].mean(),8.2:df_new['허리둘레'].mean()},inplace=True)

        st.subheader('BMI 구간별 분포')
        fig2=plt.figure()
        df_1=df_new['BMI_bins'].value_counts()
        x_label = ['정상체중','과체중','비만','저체중']
        plt.pie(df_1, # 비율 값
                labels=x_label, # 라벨 값
                autopct='%.1f%%', # 부채꼴 안에 표시될 숫자 형식(소수점 1자리까지 표시)
                startangle=70, # 축이 시작되는 각도 설정
                counterclock=True, # True: 시계방향순 , False:반시계방향순
                explode=[0.05,0.05,0.05,0.05], # 중심에서 벗어나는 정도 표시
                colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0'], 
                ) 
        plt.title('BMI지수 분포', fontsize=16)
        plt.legend()
        st.pyplot(fig2)
        st.text('건강검진 데이터에 따르면 40대 이상의 40.3%가 과체중이나 비만인 것으로 나타났다.')

        st.subheader('BMI 구간별 지표분석')
        choice_list = st.selectbox('보고싶은 지표를 선택하세요.', df_new.columns)

        if choice_list == df_new.columns:
            fig3=plt.figure()
            sns.countplot(data=df_new, x='BMI_bins', hue=df_new.columns)
            st.pyplot(fig3)




    with tab2:
        st.subheader('나의 BMI 수치를 알아보자')
        a = st.number_input('키를 입력하세요.', min_value=50)
        b = st.number_input('몸무게를 입력하세요.', min_value=5)
        a=int(a)
        b=int(b)
        my_bmi = round(b/(a/100)/(a/100),2)
        st.write('나의 BMI는?',my_bmi)

        def col():
            if my_bmi<=18.5:
                return '#0099CC'
            elif 18.5<my_bmi<=24.9:
                return  '#339900'
            elif 24.9<=my_bmi<29.9:
                return '#FFCC33'
            else:
                return '#CC0000'
        
        fig2 = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = my_bmi,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "BMI"},
            gauge = {'axis': {'range': [None, 60],'tickwidth': 1,'tickcolor': '#666666'},
                    'bar': {'color': col()},
                    },
            number={'font': {'color': col()}}))
        st.plotly_chart(fig2)

        if my_bmi<=18.5:
            st.subheader('저체중의 문제점')
            st.text('문제는 근육량!! 운동으로 저체중에서 벗어나자!')

        elif 18.5<my_bmi<=24.9:
            st.subheader('정상체중 관리법')
        elif 24.9<=my_bmi<29.9:
            st.subheader('과체중 운동법')
        else:
            st.subheader('비만 관리법')

# https://www.guro.go.kr/health/contents.do?key=1385&