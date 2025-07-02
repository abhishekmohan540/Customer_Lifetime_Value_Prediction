# 📊 Customer Lifetime Value (CLTV) Predictor

This is a Streamlit app that predicts the **future value of a customer** using an ML model trained on historical retail data.  
It helps marketing or sales teams **segment customers** and make better decisions for targeting, retention, and growth.

---

## ✅ **Features**

- Predicts CLTV based on:
  - Recency, Frequency, Monetary Value
  - Average basket size
  - Average days between purchases
  - Average unit price
  - Total quantity purchased
  - Country
- Segments customers as **Low**, **Medium**, or **High** value
- Easy to use via web interface

---

## ⚙️ **Tech Stack**

- Python, Streamlit
- scikit-learn, XGBoost, cloudpickle
- Pandas, NumPy

---

## 🚀 **How to Run Locally**

1. **Clone this repo**
   git clone https://github.com/yourusername/cltv_app.git
   cd cltv_app

2. **Create & activate a virtual environment**
python -m venv venv

Windows:
venv\Scripts\activate

macOS/Linux:
source venv/bin/activate

3. **Install dependencies**
pip install -r requirements.txt

4. **Run the app**
streamlit run app.py

5. **Application Link**
https://cltv-predictor.streamlit.app/
