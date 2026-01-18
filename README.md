**# Credit Card Fraud Detection using One-Class SVM and MongoDB**



**This repository implements an end-to-end anomaly detection pipeline for identifying fraudulent credit card transactions using a One-Class Support Vector Machine (SVM). The pipeline is designed to be lightweight, reproducible, and scalable, with input data loaded from MongoDB.**



**## Project Overview**



**- \*\*Objective\*\*: Detect fraudulent transactions in an imbalanced dataset using unsupervised learning.**

**- \*\*Model\*\*: One-Class SVM trained exclusively on normal transactions.**

**- \*\*Data Source\*\*: CSV file ingested into MongoDB for preprocessing and model training.**

**- \*\*Artifacts\*\*: Model and scaler are serialized using `joblib` (excluded from repo for size compliance).**



**## Pipeline Components**



**1. \*\*Data Ingestion\*\***

   **- Input CSV file is loaded into a MongoDB collection.**

   **- MongoDB is used for flexible querying and preprocessing.**



**2. \*\*Preprocessing\*\***

   **- Features are scaled using `StandardScaler`.**

   **- Only normal transactions are used for training.**



**3. \*\*Model Training\*\***

   **- One-Class SVM is trained to learn the boundary of normal behavior.**

   **- Hyperparameters are tuned for recall and precision balance.**



**4. \*\*Prediction and Evaluation\*\***

   **- Anomalies are flagged based on the decision function.**

   **- Evaluation metrics include confusion matrix, precision, recall, and F1-score.**



**## Repository Structure**

**> Note: Large files such as `creditcard\_fraud\_detection.csv`, `predictions.csv`, and model artifacts are excluded from version control. Use your own dataset or contact the author for guidance.**



**## Setup Instructions**



**1. Clone the repository:**



**Here’s a clean, professional README.md tailored for your credit card fraud detection pipeline using One-Class SVM and MongoDB. It’s structured for clarity, reproducibility, and collaboration:**



**# Credit Card Fraud Detection using One-Class SVM and MongoDB**



**This repository implements an end-to-end anomaly detection pipeline for identifying fraudulent credit card transactions using a One-Class Support Vector Machine (SVM). The pipeline is designed to be lightweight, reproducible, and scalable, with input data loaded from MongoDB.**



**## Project Overview**



**- \*\*Objective\*\*: Detect fraudulent transactions in an imbalanced dataset using unsupervised learning.**

**- \*\*Model\*\*: One-Class SVM trained exclusively on normal transactions.**

**- \*\*Data Source\*\*: CSV file ingested into MongoDB for preprocessing and model training.**

**- \*\*Artifacts\*\*: Model and scaler are serialized using `joblib` (excluded from repo for size compliance).**



**## Pipeline Components**



**1. \*\*Data Ingestion\*\***

   **- Input CSV file is loaded into a MongoDB collection.**

   **- MongoDB is used for flexible querying and preprocessing.**



**2. \*\*Preprocessing\*\***

   **- Features are scaled using `StandardScaler`.**

   **- Only normal transactions are used for training.**



**3. \*\*Model Training\*\***

   **- One-Class SVM is trained to learn the boundary of normal behavior.**

   **- Hyperparameters are tuned for recall and precision balance.**



**4. \*\*Prediction and Evaluation\*\***

   **- Anomalies are flagged based on the decision function.**

   **- Evaluation metrics include confusion matrix, precision, recall, and F1-score.**



**## Repository Structure**



****

**. ├── .gitignore              # Excludes large data and model artifacts ├── LICENSE                 # MIT License ├── README.md               # Project documentation**



**> Note: Large files such as `creditcard\_fraud\_detection.csv`, `predictions.csv`, and model artifacts are excluded from version control. Use your own dataset or contact the author for guidance.**



**## Setup Instructions**



**1. Clone the repository:**



**git clone https://github.com/NikhilRaman12/credit-card-fraud-prediction-oneclass-svm.git cd credit-card-fraud-prediction-oneclass-svm**





**2. Install dependencies:**



**3. Start MongoDB and load the dataset:**

**- Ensure MongoDB is running locally or remotely.**

**- Use a script or MongoDB Compass to import your CSV file.**



**4. Run the pipeline:**

**python train\_pipeline.py**





**## License**



**This project is licensed under the MIT License. See the LICENSE file for details.**



**## Author**



**Nikhil Raman K**  

**AI/ML Engineer | Data Scientist | Technical Product Architect**  

**\[GitHub Profile](https://github.com/NikhilRaman12)**



