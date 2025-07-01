# app.py
import streamlit as st
import pandas as pd
import numpy as np
import cloudpickle

# ✅ Load the saved pipeline
with open('C:/Users/Abhishek Mohan/Documents/cltv_app/cltv_best_model.pkl', 'rb') as f:
    model = cloudpickle.load(f) 

# ✅ Page title
st.title("Customer Lifetime Value (CLTV) Predictor")

st.write("""
Use this tool to predict the future value of a customer and segment them into tiers.
""")

# ✅ Inputs: must match your features
recency = st.number_input('Recency (days since last purchase)', value=30)
customer_age = st.number_input('Customer Age in dataset (days)', value=200)
frequency = st.number_input('Frequency (number of purchases)', value=5)
total_quantity = st.number_input('Total Quantity Purchased', value=20)
monetary = st.number_input('Total Monetary (£)', value=500)
avg_unit_price = st.number_input('Average Unit Price (£)', value=25)
avg_basket_size = st.number_input('Average Basket Size', value=4)
avg_days_between = st.number_input('Average Days Between Purchases', value=40)
country = st.selectbox('Country', ['United Kingdom', 'Germany', 'France', 'EIRE', 'Spain'])

# ✅ Predict button
if st.button('Predict CLTV'):
    X_new = pd.DataFrame([{
        'Recency': recency,
        'Customer_Age': customer_age,
        'Frequency': frequency,
        'Total_Quantity': total_quantity,
        'Monetary': monetary,
        'Avg_Unit_Price': avg_unit_price,
        'Avg_Basket_Size': avg_basket_size,
        'Avg_Days_Between_Purchases': avg_days_between,
        'Country': country
    }])

    pred_log = model.predict(X_new)
    pred_cltv = np.expm1(pred_log)[0]  # back-transform

    if pred_cltv < 500:
        segment = 'Low'
    elif pred_cltv < 1000:
        segment = 'Medium'
    else:
        segment = 'High'

    st.success(f"✅ Predicted CLTV: £{pred_cltv:.2f}")
    st.info(f"📊 Customer Segment: {segment}")
