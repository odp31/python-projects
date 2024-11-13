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
models = {
  'Logistic Regression': LogisticRegression(),
  'Decision Tree': DecisionTreeClassifier(),
  'Random Forest': RandomForestClassifier()
}

for name, model in models.items():
  model.fit(X_train_scaled, y_train)
  y_pred = model.predict(X_test_scaled)

  print(f"Model: {name}")
  print(classification_report(y_test, y_pred))
  print(confusion_matrix(y_test,y_pred))


# visualizing results 
# confusion matrix visualization 
plt.figure(figsize=(10,7))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# ROC Curve 
from sklearn.metrics import roc_curve, auc 

fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba[:, 1])
roc_auc = auc(fpr, tpr)

plt.plot(fpr, tpr, color='darkorange', label= 'ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0,1], [0,1], color='navy', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.show() 

