
# 🧠 Churn Prediction App

🔗 [Live Demo](https://churn-prediction-mfujxgftnlsoin3gkdpyfd.streamlit.app/)

A simple and interactive Streamlit web application that predicts customer churn based on user inputs such as age, tenure, monthly charges, and service details. It uses a machine learning model trained on customer behavior data to determine whether a customer is likely to churn or not.

## 📌 Project Overview

This project includes:
- A **Streamlit-based frontend app** (`app.py`) for customer churn prediction.
- A **Jupyter Notebook** (`notebook.ipynb`) that handles model training, evaluation, and exporting the model and scaler.

The ML model is trained using customer data including demographic and service usage details to predict if a customer will leave the service.

## 🚀 Live App Features

- Accepts inputs like:
  - Age
  - Gender (Male/Female)
  - Tenure (in months)
  - Monthly Charges
  - Contract Type (Month-to-Month, One-Year, Two-Year)
  - Internet Service (Fiber Optic, DSL)
  - Tech Support (Yes/No)
- Displays prediction (`Yes` / `No`) indicating churn risk.
- Uses a pre-trained model and scaler (`model.pkl` and `scaler.pkl`).

## 🧪 Model Training

The training is done in the `notebook.ipynb`:
- Data preprocessing (label encoding, feature selection)
- Model training using classification algorithm (likely Logistic Regression or similar)
- Model evaluation using accuracy/precision/recall metrics
- Final model and scaler are exported using `joblib`

## 📁 File Structure


├── app.py              # Streamlit application  
├── notebook.ipynb      # Jupyter Notebook for training and evaluation  
├── model.pkl           # Trained ML model (required for app.py)  
├── scaler.pkl          # Fitted scaler object (required for app.py)  

## ⚙️ Installation

1. Clone the repository:
   git clone <your-repo-url>
   cd <project-folder>

2. Install dependencies:
   pip install -r requirements.txt

   If `requirements.txt` is not available, install manually:
   pip install streamlit joblib scikit-learn numpy pandas

3. Run the app:
   streamlit run app.py

## 💡 Example Input

| Field             | Value Example |
|------------------|------------------|
| Age              | 30               |
| Gender           | Female           |
| Tenure           | 12               |
| Monthly Charges  | 70               |
| Contract Type    | One-Year         |
| Internet Service | DSL              |
| Tech Support     | Yes              |

Prediction: No (i.e., customer likely to stay)


## 📝 Notes

- The model expects the inputs in a specific order:  
  [Age, Gender (0/1), Tenure, MonthlyCharges, ContractType (0/1/2), InternetService (0/1), TechSupport (0/1)]

- Ensure `model.pkl` and `scaler.pkl` are present in the same directory as `app.py` before running the app.
