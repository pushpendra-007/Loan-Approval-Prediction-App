import streamlit as st
import pandas as pd
import pickle as pk

model = pk.load(open('model.pk1','rb'))
scaler = pk.load(open('scaler.pk1','rb'))

st.header('Lone Predcition App')

Couple = st.selectbox('Choose  Married ',["Married","Un Married"])

grad = st.selectbox('Choose Education ',['Graduated','Not Graduated'])

Loan_Amount_Term = st.selectbox('Choose Loan_Amount_Term ',['Two years', 'Five Years'])

Applicant_Income = st.slider('Choose Applicant_Income ', 0, 100000)
 
Coapplicant_Income = st.slider('Choose Coapplicant_Income ',1000, 100000)

Loan_Amount = st.slider('Choose Loan_Amount ',1000, 500000)

if grad == 'Graduated':
    grad_s = 0
else:
    grad_s = 1

if Couple == 'Married':
    Couple_s = 0
else:
    Couple_s = 1

if st.button("Predict"):


    pred_data = pd.DataFrame([['1','1',Applicant_Income,Coapplicant_Income ,Loan_Amount,'240']],columns = ['Married' ,'Education' ,'ApplicantIncome' ,'CoapplicantIncome' , 'LoanAmount' , 'Loan_Amount_Term']) 
    pred_data = scaler.transform(pred_data)
    predict = model.predict(pred_data)
    if predict[0] == 1:
        st.markdown('Loan is Approved')
    else:
        st.markdown('Loan is Rejected')