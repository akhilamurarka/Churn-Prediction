# Gender -> 1 Female    0 Male
# Churn ->  1 Yes       0 No
# scaler -> scaler.pkl
# model -> model.pkl
# Order of X -> Age	Gender	Tenure	MonthlyCharges	ContractType	InternetService	TechSupport
import streamlit as st
import joblib
import numpy as np

scaler=joblib.load("scaler.pkl")
model=joblib.load("model.pkl")

st.title("Churn Prediction App")

st.divider()

st.write("Please enter the values and hit the predict button for getting a prediction")

st.divider()

age=st.number_input("Enter Age",min_value=10, max_value=100,value=30)
tenure=st.number_input("Enter Tenure",min_value=0, max_value=130,value=5)
monthly_charge=st.number_input("Enter Monthly Charges",min_value=20, max_value=150,value=40)
gender=st.selectbox("Enter the Gender",["Male","Female"])
contract_type=st.selectbox("Enter the Contract Type",["Month-to-Month","One-Year","Two-Year"])
internet_service=st.selectbox("Enter the Internet Service",["Fiber Optic","DSL"])
tech_support=st.selectbox("Enter the Tech Support",["Yes","No"])

st.divider()

predictButton=st.button("Predict")

st.divider()

if predictButton:
  
  gender_selected=1 if gender=="Female" else 0
  
  if contract_type == "Month-to-Month":
    contract_selected=0
  elif contract_type == "One-Year":
    contract_selected=1
  else:
    contract_selected=2
    
  tech_selected=1 if tech_support=="Yes" else 0
  
  internet_selected=1 if internet_service=="Fiber Optic" else 0

  X=[age,gender_selected,tenure,monthly_charge,contract_selected,internet_selected,tech_selected]
  X1=np.array(X)
  
  X_array=scaler.transform([X1])
  prediction=model.predict(X_array)[0]
  
  predicted="Yes" if prediction==1 else "No"
  
  st.balloons()
  
  st.write(f"Prediction: {predicted}")

else:
  st.write("Please enter the values and use predict button")