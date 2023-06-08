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
    df=pd.read_csv('data/checkup_2020.CSV', encoding='cp949')
    df=df.sample(n=10000, random_state=42)
    st.subheader(':round_pushpin:데이터 보기')
    st.write('데이터 출처 : 공공데이터포털(https://www.data.go.kr/data/15007122/fileData.do)')
    st.dataframe(df)
    st.write('데이터의 양이 너무 많아 1만건만 랜덤으로 추출하여 분석하였습니다.')
    with st.expander('건강검진 데이터 지표 설명'):
        st.write('총 34개의 변수로 가입자 일렬번호와 ① 수진자 기본정보 : 성, 연령, 거주지 시도코드와 같은 기본정보 ② 건강검진결과 및 문진정보 : 신체, 몸무게, 허리둘레 등 신체사이즈 정보와 혈압, 혈당, 콜레스테롤, 요단백, 감마지피티와 같은 병리검사결과 시력과 청력, 구강검사와 같은 진단검사결과 그 외 음주와 흡연 여부에 대한 문진결과로 구성되어있다.')

    st.subheader(':round_pushpin:데이터 전처리')
    st.text('필요한 컬럼을 가져와 레이블인코딩을 통해 value값을 수정하고 결측치를 확인하여 제거하였습니다. \n또한 키와 몸무게를 통하여 새로운 BMI 컬럼을 만들고 구간을 설정하여 BMI_bins 컬럼도 추가했습니다.')
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
    st.dataframe(df_new)
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