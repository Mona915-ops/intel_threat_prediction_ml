from flask import Flask, request, render_template
import pandas as pd
import joblib
from utils import PortScanUtils

app = Flask(__name__)

# Load once
model = joblib.load('model.pkl')
encoder = joblib.load('label_encoder.pkl')
feature_names = joblib.load('feature_names.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Get file
        if 'file' not in request.files:
            return "No file uploaded"

        file = request.files['file']
        if file.filename == '':
            return "Empty filename"

        # 2. Read uploaded CSV
        input_df = pd.read_csv(file)
        input_df.columns = input_df.columns.str.strip()

        # 3. Extract features
        features_df = PortScanUtils.extract_features(input_df)

        # 4. Align columns
        missing_cols = set(feature_names) - set(features_df.columns)
        for col in missing_cols:
            features_df[col] = 0
        features_df = features_df[feature_names]

        # 5. Predict
        predictions = model.predict(features_df)
        labels = encoder.inverse_transform(predictions)

        # 6. Return results (as string for now)
        result = [f"Row {i+1}: {label}" for i, label in enumerate(labels)]
        return "<br>".join(result)

    except Exception as e:
        print("❌ Error in prediction:", e)
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
