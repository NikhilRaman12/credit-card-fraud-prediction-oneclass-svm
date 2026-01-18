import joblib
import pandas as pd

print("Starting One-Class SVM prediction...")

# 1. Load model and scaler
model = joblib.load("oneclass_svm_model.joblib")
scaler = joblib.load("scaler.joblib")

print("Model and scaler loaded")

# 2. Load data
data = pd.read_csv("creditcard_fraud_detection.csv")
print(f"Loaded dataset with shape: {data.shape}")

# 3. Drop target column ONLY if present
if "Class" in data.columns:
    X = data.drop(columns=["Class"])
else:
    X = data.copy()

print(f"Feature matrix shape before scaling: {X.shape}")

# 4. Scale using trained scaler
X_scaled = scaler.transform(X)

# 5. Predict
predictions = model.predict(X_scaled)

# 6. Convert predictions
data["svm_prediction"] = predictions
data["svm_label"] = data["svm_prediction"].map(
    {1: "Normal", -1: "Anomaly"}
)

# 7. Summary
total = len(data)
anomalies = (data["svm_prediction"] == -1).sum()

print("Prediction completed")
print(f"Total samples   : {total}")
print(f"Anomalies found : {anomalies}")

# 8. Show sample output
print(data[["svm_prediction", "svm_label"]].head(10))

# 9. Save results
data.to_csv("predictions.csv", index=False)
print("Predictions saved to predictions.csv")

