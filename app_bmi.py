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
        df_new=pd.read_csv('data/checkup_2020.CSV', index_col=0)
        st.subheader('📍BMI 구간별 분포')
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

        st.subheader('📍BMI 히트맵')
        fig13=plt.figure()
        sns.heatmap(data=df_new.corr(numeric_only=True), fmt='.2f', annot=True, vmin=-1, vmax=1, cmap='coolwarm', linewidths=0.5) 
        st.pyplot(fig13)

        st.subheader('📍BMI 지표분석')
        col_1 = ['성별코드','연령대 코드(10세단위)','신장(5Cm단위)', '체중(5Kg 단위)', '허리둘레', '음주여부','흡연상태','식전혈당(공복혈당)','수축기 혈압']
        choice_list = st.selectbox('보고싶은 지표를 선택하세요.', col_1)

        if choice_list == '성별코드' : 
            fig3=plt.figure()
            sns.regplot(data=df_new, x='성별코드', y='BMI')
            st.pyplot(fig3)
        elif choice_list == '연령대 코드(10세단위)' : 
            fig4=plt.figure()
            sns.regplot(data=df_new, x='연령대 코드(10세단위)', y='BMI')
            st.pyplot(fig4)
        elif choice_list == '신장(5Cm단위)' : 
            fig5=plt.figure()
            sns.regplot(data=df_new, x='신장(5Cm단위)', y='BMI')
            st.pyplot(fig5)
        elif choice_list == '체중(5Kg 단위)' : 
            fig6=plt.figure()
            sns.regplot(data=df_new, x='체중(5Kg 단위)', y='BMI')
            st.pyplot(fig6)
        elif choice_list == '허리둘레' : 
            fig7=plt.figure()
            sns.regplot(data=df_new, x='허리둘레', y='BMI')
            st.pyplot(fig7)
        elif choice_list == '음주여부' : 
            fig8=plt.figure()
            sns.regplot(data=df_new, x='음주여부', y='BMI')
            st.pyplot(fig8)
        elif choice_list == '흡연상태' : 
            fig9=plt.figure()
            sns.regplot(data=df_new, x='흡연상태', y='BMI')
            st.pyplot(fig9)
        elif choice_list == '식전혈당(공복혈당)' : 
            fig11=plt.figure()
            sns.regplot(data=df_new, x='식전혈당(공복혈당)', y='BMI')
            st.pyplot(fig11)
        elif choice_list == '수축기 혈압' : 
            fig12=plt.figure()
            sns.regplot(data=df_new, x='수축기 혈압', y='BMI')
            st.pyplot(fig12)

    with tab2:
        st.subheader("📍나의 BMI 수치를 알아보자")
        a = st.number_input('키를 입력하세요.', min_value=50)
        b = st.number_input('몸무게를 입력하세요.', min_value=5)
        a=int(a)
        b=int(b)
        my_bmi = round(b/(a/100)/(a/100),2)
        st.write("나의 BMI는?",my_bmi)

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
            with st.expander('문제는 근육량!! 운동으로 저체중에서 벗어나자!'):
                st.video('https://youtu.be/OQCSA-0Cef4')
                st.text('''🏊‍♂️ 운동법 : 
운동은 살을 빼는 것뿐만 아니라 살을 찌우는데도 효과적입니다.
운동으로 기초대사량을 늘리면 자연스럽게 식욕이 올라가는데요.
저체중에서는 체지방을 태우는 유산소 운동보다 
근육량을 증가시키는 무산소 운동을 지속적으로 하는 것이 좋습니다.

🥗 식습관 : 
저체중을 건강체중으로 만들기 위해서는 1킬로그램당 2에서 10칼로리를 더 섭취하는 것이 좋은데요.
열량은 식사에서 늘려도 좋지만 식사 사이사이에 간식으로 섭취하는 것도 도움이 됩니다.
영양 불균형으로 인한 마른 몸매는 더 이상 아름다움의 상징이 아닙니다.
내 몸에 맞는 적정 체지방과 근육을 만드는 것이 탄탄하고 건강한 몸매를 만드는 비결입니다.
질병이 원인이 아닌 저체중은 대부분 생활습관 개선만으로도 정상체중으로 올릴 수 있습니다.
건강한 아름다움을 위한 첫 걸음, 지금부터 시작해 보는 것은 어떨까요?''')
                st.write('출처 : 하이닥(https://www.hidoc.co.kr/healthstory/news/C0000425948)')

        elif 18.5<my_bmi<=24.9:
            st.subheader('정상체중 유지법')
            with st.expander('더 건강하게!!'):
                st.write('유튜브에서 보기👉https://www.youtube.com/watch?v=BSM5CobhV28')
                st.write('''출처 : 용인시보건소 유튜브(https://www.youtube.com/@TheYongin)''')

        elif 24.9<=my_bmi<29.9:
            st.subheader('과체중 운동법')
            with st.expander('비만으로 가는 지름길? 과체중!!!'):
                st.video('https://youtu.be/73P74B_6nxU')
                st.text('''👉 과체중의 위험성
과체중으로 들어서게 되면 고혈압, 당뇨병, 고지혈증처럼 체중증가와 관련된 질환의 발생 가능성이 높고,
이런 위험성은 비만에 가까워 질수록 증가됩니다.
즉, 비만은 체중증가로 인해 발생한 질환으로 사망률이 높아진 상태로 생각하면 됩니다.
한번 비만하게 된 몸을 다시 정상체중으로 돌리는 일은 쉽지 않습니다. 비만을 벗어나기 위해서는
철저한 식이관리와 운동이 꾸준히 병행되어야 하는데요, 바쁜 현대인들이 이에 맞춰 생활하기란 매우 어려운 일입니다.
그래서 과체중 관리가 중요합니다.
비만으로 이행되기 전에 체중을 관리하게 되면 비만일 때보다 훨씬 부담 없이 건강한 체중으로 되돌릴 수 있습니다.

🏊‍♂️ 운동법 :
평상시 엘리베이터를 이용하는 대신 계단을 이용하여 오르내리거나 점심 또는 저녁식사 후
10분 정도의 산책 아니면 출퇴근 시 1~2개의 버스 정거장을 걸어서 이동하는 정도의 규칙적인 운동 습관은
인체에 다양한 긍정적인 변화(체지방감소, 근골격계의 기능 향상, 면역기능 향상 등)를 유도합니다.
운동을 통해 축적된 지방을 분해할 수 있다는 관점에서 비만관리에 효과적일 뿐만 아니라
비만 관련 질환의 유병률을 줄이고, 치료 및 개선에 도움을 줄 수 있습니다.

🥗 식습관 : 
대사증후군에서 인슐린 저항성 개선을 위해 가장 우선해야 할 부분이 바로 체중감량입니다.
무리한 다이어트보다 평소 칼로리 섭취량을 줄여 체중을 감량하는 것이 중요합니다.
당지수가 높은 음식은 혈당을 빨리 증가시켜 인슐린 분비와 저항성을 높이기 때문에 피해야 합니다.
지방은 칼로리가 높은 반면 포만감은 적게 줘 음식을 더 먹게 되므로 주의해야 합니다.
체중조절을 위해서는 포만감을 높이는 음식을 섭취하는 것이 좋습니다.
칼륨과 마그네슘은 고혈압을 예방하고, 칼슘은 체중감량과 인슐린 저항성 개선을,
비타민 B와 E는 심혈관 질환 감소에 도움이 됩니다.
섬유소는 당이 흡수되는 것을 지연시키고 혈액 내 콜레스테롤을 낮춰주는데 도움이 됩니다.
저염식은 그 자체로 혈압을 떨어뜨리는 효과가 있고 고혈압 치료제의 효과도 증진시켜줍니다.''')
                st.write('출처 : 구로구보건소(https://www.guro.go.kr/health/contents.do?key=1385&),\n하이닥(https://www.hidoc.co.kr/healthstory/news/C0000408150), (https://www.hidoc.co.kr/healthstory/news/C0000408156)')

        else:
            st.subheader('비만 관리법')
            with st.expander('내가 비만일리 없어!!!'):
                st.video('https://youtu.be/P6G1ykZjj88')
                st.text('''🏊‍♂️ 운동법 :
빠르게 걷기, 수영, 자전거 타기 등의 유산소 운동이 체지방 분해에 효과가 있고, 
헬스 등의 근력 운동은 근육량을 증가시켜 기초대사량을 높여주기 때문에 체중감량에 도움이 됩니다.
운동은 하루 최소 20분 이상, 일주일에 4회 이상 실시해야 효과가 있습니다.
운동 전후 스트레칭은 꼭 챙겨야 합니다.

🥗 식습관 :
체중감량의 성패를 좌우하는 가장 중요한 요소가 바로 식이조절입니다.
식이조절을 할 때는 원푸드 다이어트 식단이나 초저열량 식단은 영양 불균형을 초래해 건강을 해치므로 피해야 합니다.
건강하고 효과적인 체중감량을 위해서는 영양소가 골고루 포함되어 있는 저열량 식단을 유지하는 것이 중요합니다.
저열량 식사는 일일 800에서 1500칼로리를 섭취하는 것으로, 하루 500칼로리 감소로도 일주일에 0.5킬로그램의
체중감량 효과를 얻게 되고, 꾸준히 시행한다면 체중의 15에서 20%를 감량하는 효과를 얻을 수 있습니다.
이렇게 식이조절과 더불어 운동을 하게 되면 비만걱정은 이제 그만해도 되는 것이죠.''')
                st.write('''출처 : 하이닥(https://www.hidoc.co.kr/healthstory/news/C0000393491)''')
        st.subheader("📍추천 운동_운동별 칼로리 소모량")
        st.image('data\diet.jpg', caption='구로보건소(https://www.guro.go.kr/health/contents.do?key=1385&)')
# https://www.guro.go.kr/health/contents.do?key=1385&