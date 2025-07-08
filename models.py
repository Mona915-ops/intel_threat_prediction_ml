# models.py

import os
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from utils import PortScanUtils

def train_model(data_folder_path='.', model_output_path='model.pkl'):
    """
    Trains a Random Forest model on selected CICIDS2017 files and saves model, label encoder, and feature names.
    """

    # Selected CSVs from CICIDS2017
    csv_files = [
        "Datasets/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv",
        "Datasets/Wednesday-workingHours.pcap_ISCX.csv",
        "Datasets/Tuesday-WorkingHours.pcap_ISCX.csv",
        "Datasets/Friday-WorkingHours-Morning.pcap_ISCX.csv"
    ]

    dataframes = []
    for file in csv_files:
        file_path = os.path.join(data_folder_path, file)
        if os.path.exists(file_path):
            print(f"✅ Loaded {file}")
            df = pd.read_csv(file_path)
            df.columns = df.columns.str.strip()
            dataframes.append(df)
        else:
            print(f"⚠️ Warning: {file} not found and skipped.")

    if not dataframes:
        raise ValueError("❌ No valid CSV files found.")

    # Combine and filter
    df = pd.concat(dataframes, ignore_index=True)

    # Filter for required classes
    attack_types = ['BENIGN', 'PortScan', 'DoS Hulk', 'FTP-Patator']
    df = df[df['Label'].isin(attack_types)]

    # Feature extraction
    df = PortScanUtils.extract_features(df)

    # Encode labels
    le = LabelEncoder()
    df['Label'] = le.fit_transform(df['Label'])

    # Split features and label
    X = df.drop(columns=['Label'], axis=1)
    y = df['Label']

    # Save feature names
    joblib.dump(X.columns.tolist(), 'feature_names.pkl')
    print("💾 Saved feature_names.pkl")

    # Downsample
    sample_indices = np.random.choice(X.index, size=200000, replace=False)
    X_sampled = X.loc[sample_indices]
    y_sampled = y.loc[sample_indices]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_sampled, y_sampled, test_size=0.3, random_state=42, stratify=y_sampled
    )

    # Train the model
    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X_train, y_train)

    # Save model and label encoder
    joblib.dump(clf, model_output_path)
    joblib.dump(le, 'label_encoder.pkl')
    print("✅ Model and encoder saved!")

    # Evaluate
    y_pred = clf.predict(X_test)
    print("\n🎯 Classification Report:\n", classification_report(y_test, y_pred, target_names=le.classes_))
    print("🧱 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("✅ Accuracy:", accuracy_score(y_test, y_pred))

# Run training when script is executed directly
if __name__ == '__main__':
    train_model()

