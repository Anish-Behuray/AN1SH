import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open('rf21.pkl','rb'))

EmploymentType = ['Unemployed',
                  'Full-time',
                  'Self-employed',
                  'Part-time']

HasCoSigner = ['Yes',
               'No']

st.title('Predicting Loan Apporval')

col3,col4,col5 = st.columns(3)

with col3:
    Age = st.number_input('Age')
with col4:
    Income = st.number_input('What is your Income')
with col5:
    MonthsEmployed = st.number_input('For how many months your employed')


col10, col7, col8 = st.columns(3)
with col7:
    LoanAmount = st.number_input('what is the amount of loan you want')
with col8:
    CreditScore = st.number_input('What is your credit score')
with col10:
    InterestRate = st.number_input('what is the interest rate')


col1, col9 = st.columns(2)

with col1:
    employments = st.selectbox('Select your current Employment Type',sorted(EmploymentType))
with col9:
    co_signers = st.selectbox('Is there any co-signer',sorted(HasCoSigner))



if employments == 'Full-time':
    employment = 0
elif employments == 'Part-time':
    employment = 1
elif employments == 'Self-employed':
    employment = 2
else:
    employment = 3

if co_signers == 'Yes':
    co_signer = 1
else:
    co_signer = 0

if st.button('Predict'):

    input_df = pd.DataFrame(
        {'Age': [Age], 'Income': [Income], 'LoanAmount': [LoanAmount], 'CreditScore': [CreditScore],
         'MonthsEmployed': [MonthsEmployed], 'InterestRate': [InterestRate],
          'EmploymentType': [employment], 'HasCoSigner': [co_signer]})
    result = pipe.predict(input_df)
    st.header("Will you get your loan apporved - " + str("No" if int(result[0]) == 0 else "Yes"))
