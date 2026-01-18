import pandas as pd
from pymongo import MongoClient
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler
import joblib
import pickle

# 1. Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ml_pipeline"]
collection = db["raw_data"]   

# 2. Load data into pandas
df = pd.DataFrame(list(collection.find()))

# 3. Prepare features and labels
X = df.drop(columns=["_id", "Class"])   
y = df["Class"]

# 4. Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 5. Train One-Class SVM
svm = OneClassSVM(
    nu=0.05,
    kernel="rbf",
    gamma="scale"
)

svm.fit(X_scaled)

print(" One-Class SVM trained successfully")

import joblib

joblib.dump(svm, "oneclass_svm_model.joblib")
joblib.dump(scaler, "scaler.joblib")

print(" Model and scaler saved")

