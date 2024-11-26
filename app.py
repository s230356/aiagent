# 예측 모델 웹앱 만들기
import streamlit as st

# 1.기계학습 모델 파일 로드
import joblib
model = joblib.load('logistic_regression_model__1_.pkl')

# 2.모델 설명
st.title('당뇨병 예측 에이전트')
st.subheader('당뇨병을 예측해줌')
st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
st.write(' - 학습 데이터 출처 :https://www.kaggle.com/code/sarahyoun/heart-failure-prediction')
st.write(' - 훈련    데이터 : 210건')
st.write(' - 테스트 데이터 : 90건')
st.write(' - 인공지능 모델 정확도 : ***')

# 3.데이터 시각화
col1, col2, col3, col4, col5 = st.columns(5)  
with col1:
      st.subheader('데이터시각화1')
      st.image('시각화1.PNG' )   
with col2:
      st.subheader('데이터시각화2')
      st.image('시각화2.PNG' )  
with col3:
      st.subheader('데이터시각화3')
      st.image('시각화3.PNG')
with col4:
      st.subheader('데이터시각화4')
      st.image('시각화4.PNG')
with col5:
      st.subheader('데이터시각화5')
      st.image('시각화5.PNG')

# 4.모델 활용
st.subheader('모델 활용')
st.write(' 인공지능이 당신의 당뇨병 여부를 알려드립니다! 목적 외엔 개인정보를 사용하지 않습니다.')

a = st.number_input(' 혈소판 수', value=0)     
b = st.number_input(' 크레아틴카나제 검사 결과 ', value=0 )     
c = st.number_input(' 박출계수  ', value=0 ) 
d = st.number_input(' 고혈압 여부( 정상:0 당뇨병 :1) ', value=0) 
e = st.number_input(' 혈중 크레아틴 레벨 ', value=0.0 ) 
f = st.number_input(' 혈중 나트륨 레벨 ', value=0 ) 
g = st.number_input(' 성별 (여:0, 남:1)', value=0) 
h = st.number_input('흡연 여부 (비흡연:0, 흡연:1) ', value=0) 
i = st.number_input('나이 ', value=0 ) 
j = st.selectbox('개인정보 수집에 동의하나요?(동의한다:0, 동의하지않는다:1)', [0,1])
                                                            

if st.button('진단결과'):           
        input_data = [[a,b,c,d,e,f,g,h,i]]    
        p = model.predict(input_data)         
        st.write('인공지능의 진단결과는', p)
