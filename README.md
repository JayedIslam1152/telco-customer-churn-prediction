# 📊 Telco Customer Churn Prediction

An end-to-end Machine Learning practice project that predicts whether a telecom customer is likely to churn based on customer demographics, account information, and subscribed services. The project covers data preprocessing, exploratory data analysis (EDA), model training, evaluation, feature importance analysis, model serialization using Joblib, and deployment with Streamlit.

## 🚀 Live Demo

**Streamlit App:** https://telco-customer-churn-prediction-practice.streamlit.app

---

## 📌 Project Overview

Customer churn prediction is a common classification problem in the telecom industry. This project explores the complete Machine Learning workflow, from data preprocessing and visualization to model training, evaluation, and deployment.

---

## 🎯 Objectives

* Explore and understand the dataset
* Perform data preprocessing and feature encoding
* Conduct Exploratory Data Analysis (EDA)
* Train and compare multiple Machine Learning models
* Evaluate model performance using classification metrics
* Analyze feature importance
* Save the best-performing model using Joblib
* Deploy the trained model using Streamlit

---

## 📂 Dataset

**Dataset:** IBM Telco Customer Churn Dataset

### Features

* Gender
* Senior Citizen
* Partner
* Dependents
* Tenure
* Phone Service
* Multiple Lines
* Internet Service
* Online Security
* Online Backup
* Device Protection
* Tech Support
* Streaming TV
* Streaming Movies
* Contract
* Paperless Billing
* Payment Method
* Monthly Charges
* Total Charges

### Target Variable

* **Churn**

  * Yes
  * No

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* Joblib
* Streamlit

---

## 📊 Exploratory Data Analysis

The following analyses were performed:

* Data Cleaning
* Missing Value Handling
* Label Encoding
* Correlation Analysis
* Data Visualization
* Feature Relationship Analysis

---

## 🤖 Machine Learning Models

The following classification models were trained and compared:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Decision Tree Classifier
* Random Forest Classifier
* XGBoost Classifier

---

## 📈 Model Evaluation

Models were evaluated using the following metrics:

* Accuracy Score
* Precision Score
* Recall Score
* F1 Score
* Confusion Matrix
* Classification Report

### Best Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 79%   |
| Precision | 62%   |
| Recall    | 49%   |
| F1 Score  | 55%   |

> **Note:** Performance may vary depending on the selected model and train-test split.

---

## 🌟 Feature Importance

Feature importance analysis was performed using:

* Decision Tree Classifier
* Random Forest Classifier
* XGBoost Classifier

This analysis highlights the features that contribute most to customer churn prediction.

---

## 🚀 Deployment

The best-performing model was:

* Saved using **Joblib**
* Deployed using **Streamlit**

The application allows users to enter customer information and receive an instant prediction indicating whether the customer is likely to churn.

---

## 📁 Project Structure

```text
telco-customer-churn-prediction/
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── notebooks/
│   └── Customer_Churn_Prediction.ipynb
│
├── app.py
├── random_forest_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/jayedislam1152/telco-customer-churn-prediction.git
```

Navigate to the project directory:

```bash
cd telco-customer-churn-prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 💡 Key Insights

* Customers with **month-to-month contracts** are more likely to churn.
* Customers with **longer tenure** are less likely to churn.
* **Contract Type** is one of the strongest predictors of customer churn.
* Customers using **Online Security** and **Tech Support** tend to have lower churn rates.
* Higher **Monthly Charges** are associated with a higher likelihood of churn.

---

## 👨‍💻 Author

**Jayed**

Data Sciencetist

* GitHub: https://github.com/jayedislam1152
* Linkedin: https://linkedin.com/in/jayedbinislam

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star on GitHub!

