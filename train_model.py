import os
import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

from utils.helpers import clean_log

DATA_PATH = "data/training_logs.csv"
MODEL_DIR = "model"
MODEL_PATH = os.path.join(MODEL_DIR, "log_model.pkl")
ENCODER_PATH = os.path.join(MODEL_DIR, "label_encoder.pkl")

def train_model():
    if not os.path.exists(DATA_PATH):
        print(f"[ERROR] Training data not found: {DATA_PATH}")
        return

    df = pd.read_csv(DATA_PATH)
    if "log_message" not in df.columns or "label" not in df.columns:
        print("[ERROR] CSV must contain 'log_message' and 'label' columns.")
        return

    df["cleaned_log"] = df["log_message"].astype(str).apply(clean_log)
    X = df["cleaned_log"]
    y = df["label"]

    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )

    model_pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), max_features=3000)),
        ("clf", LogisticRegression(max_iter=1000))
    ])

    model_pipeline.fit(X_train, y_train)
    y_pred = model_pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("\n" + "=" * 60)
    print("MODEL TRAINING COMPLETED")
    print("=" * 60)
    print(f"Accuracy: {accuracy:.4f}\n")
    print("Classification Report:")
    print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(model_pipeline, MODEL_PATH)
    joblib.dump(label_encoder, ENCODER_PATH)

    print(f"[+] Model saved to: {MODEL_PATH}")
    print(f"[+] Label encoder saved to: {ENCODER_PATH}")

if __name__ == "__main__":
    train_model()
