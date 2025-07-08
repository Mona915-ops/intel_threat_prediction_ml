from flask import Flask, render_template, request
import pandas as pd
import joblib
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load saved files from uploads folder
model = joblib.load("uploads/model.pkl")
encoder = joblib.load("uploads/label_encoder.pkl")
feature_names = joblib.load("uploads/feature_names.pkl")

@app.route('/')
def index():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("POST /predict route hit")

        if 'file' not in request.files:
            return render_template('index.html', prediction="No file part in request")

        uploaded_file = request.files['file']
        if uploaded_file.filename == '':
            return render_template('index.html', prediction="No file selected")

        filename = secure_filename(uploaded_file.filename)
        filepath = os.path.join("uploads", filename)
        uploaded_file.save(filepath)

        print(f"File received: {filename}")
        df = pd.read_csv(filepath)
        print(f"CSV loaded. Shape: {df.shape}")

        # Ensure feature alignment
        missing_cols = set(feature_names) - set(df.columns)
        for col in missing_cols:
            df[col] = 0
        df = df[feature_names]
        print("Features aligned")

        # Predict
        predictions = model.predict(df)
        decoded_labels = encoder.inverse_transform(predictions)
        print("Raw predictions:", predictions)
        print("Decoded labels:", decoded_labels)

        # Only returning first row's prediction since we expect one-row input
        return render_template('index.html', prediction=decoded_labels[0])

    except Exception as e:
        print("Error during prediction:", str(e))
        return render_template('index.html', prediction="Error during prediction")

if __name__ == '__main__':
    app.run(debug=True)
