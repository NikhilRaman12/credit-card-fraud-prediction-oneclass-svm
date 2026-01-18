import pandas as pd
import joblib
import gradio as gr

model = joblib.load("oneclass_svm_model.joblib")
scaler = joblib.load("scaler.joblib")

FEATURE_COLUMNS = [
    "Time","V1","V2","V3","V4","V5","V6","V7","V8",
    "V9","V10","V11","V12","V13","V14","V15","V16",
    "V17","V18","V19","V20","V21","V22","V23","V24",
    "V25","V26","V27","V28","Amount"
]

def predict_from_csv(file):
    df = pd.read_csv(file.name)

    X = df[FEATURE_COLUMNS]
    X_scaled = scaler.transform(X)
    preds = model.predict(X_scaled)

    df["svm_label"] = ["Normal" if p == 1 else "Anomaly" for p in preds]

    total = len(df)
    anomalies = (df["svm_label"] == "Anomaly").sum()

    summary = f"Total samples: {total}\nAnomalies detected: {anomalies}"
    preview = df[["svm_label"]].head(10).values.tolist()

    return summary, preview

with gr.Blocks() as demo:
    gr.Markdown("## Credit Card Fraud Detection (One-Class SVM)")

    file_input = gr.File(label="Upload CSV")
    summary_out = gr.Textbox(label="Summary")
    table_out = gr.Dataframe(headers=["svm_label"], datatype=["str"])

    btn = gr.Button("Run")
    btn.click(predict_from_csv, file_input, [summary_out, table_out])

demo.launch(share=True, show_api=False)
