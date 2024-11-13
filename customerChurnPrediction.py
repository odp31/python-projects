import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix 

# Load Dataset
df = pd.read_csv('telecom_customer_churn.csv')

# data cleaning and preprocessing
df.fillna(method='ffill', inplace = True)

# encode categorical variables 
df = pd.get_dummies(df, columns = ['Gender', 'SeniorCitizen', 'Partner, 'Dependents', 'PhoneService',
                                   'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 
                                   'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 
                                   'Contract', 'PaytemntMethod'])

# feature engineering: create new features (e.g., total charges per month)
df['TotalChargesPerMonth'] = df['TotalCharges'] / df['tenure']

# split data into features and target variable 
X = df.drop('Churn', axis=1)
y = df['Churn']

# split data into training and test sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# model building and training 
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# model evaluation
y_pred = model.predict(X_test_scaled)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
