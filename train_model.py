# train_model.py

import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Load dataset
df = pd.read_csv("loans.csv")

print("Dataset Loaded Successfully!")
print("Dataset Shape:", df.shape)

# 2. Separate input features and target
X = df[
    ["income", "credit_score", "loan_amount", "employment_years"]
]

y = df["loan_status"]

# 3. Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))

# 4. Create and train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

print("\nModel Training Completed!")

# 5. Make predictions
y_pred = model.predict(X_test)

# 6. Evaluate model
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 7. Save trained model
os.makedirs("models", exist_ok=True)

with open("models/loan_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved successfully!")
print("Path: models/loan_model.pkl")