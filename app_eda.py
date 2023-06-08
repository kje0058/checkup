import streamlit as st
import pandas as pd
import platform
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False
sns.set(font="Malgun Gothic", 
        rc={"axes.unicode_minus":False},
        style='darkgrid')
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

def run_app_eda():
    df_new=pd.read_csv('data/checkup_2020.CSV',index_col=0)
    st.subheader(':round_pushpin:데이터 보기')
    st.write('데이터 출처 : 공공데이터포털(https://www.data.go.kr/data/15007122/fileData.do)')
    st.dataframe(df_new)
    st.write('데이터의 양이 너무 많아 1만건만 랜덤으로 추출하여 분석하였습니다.')
    with st.expander('데이터 지표 설명'):
        st.text('''성별코드 : 0(여자), 1(남자)
연령대코드(10세단위) : 0(40대), 1(50대), 2(60대), 3(70대), 4(80대 이상)
신장(5Cm단위) : ex) 100~104CM -> 100CM
체중(5Kg 단위) : ex) 25~29KG -> 25KG
허리둘레 : 검진자의 허리둘레
음주여부 : 0(마시지 않는다), 1(마신다)
흡연상태 : 0(피우지 않는다), 1(이전에 피웠으나 끊었다), 2(현재도 피우고 있다)
식전혈당(공복혈당) : 식사 전 혈당(혈액 100ml당 함유 되어 있는 포도당의 농도) 수치
수축기혈압 : 최고 혈압으로 심장이 수축해서 강한 힘으로 혈액을 동맥에 보낼 때의 혈관 내압
BMI : 체질량지수, 몸무게(kg) / 키(m) / 키(m)
BMI_bins : 0(18.5 미만 : 저체중), 1(18.5~24.9 : 정상체중),
        2(24.9~29.9 : 과체중), 3(29.9 이상 : 비만)''')
        
    st.subheader(':round_pushpin:최대/최소 데이터 확인하기')
    column = st.selectbox('최대/최소 데이터를 확인할 컬럼을 선택하세요.', df_new.columns)

    st.text('최대 데이터')
    st.dataframe(df_new.loc[df_new[column]==df_new[column].max(),])
    st.text('최소 데이터')
    st.dataframe(df_new.loc[df_new[column]==df_new[column].min(),])

    st.subheader(':round_pushpin:컬럼 별 히스토그램')
    column = st.selectbox('히스토그램을 확인할 컬럼을 선택하세요.', df_new.columns)
    fig=plt.figure()
    df_new[column].hist(grid=False, bins=10)
    plt.title(column + ' Histogram')
    plt.xlabel(column)
    plt.ylabel('count')
    st.pyplot(fig)