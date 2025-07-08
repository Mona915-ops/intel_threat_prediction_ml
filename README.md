
# 🔐 Intel Unnati – Real-Time Threat Prediction

This project was developed as part of the Intel® Unnati Industrial Training Program. The objective is to build a real-time threat prediction system using machine learning techniques, deployed via a Flask-based web interface.

---

## 📌 Problem Statement

Build a system that can accurately classify threat types based on network data, using a trained machine learning model.

---

## 🏗️ Architecture Flow

1. Raw data collection and cleaning
2. Feature engineering and encoding
3. Model training and hyperparameter tuning
4. Real-time prediction module (Flask-based)
5. Visualization and performance evaluation

---

## 📁 Folder Structure

```
intel-threat-prediction/
├── app.py               # Flask app
├── model.py             # Model training script
├── predict_new.py       # Real-time prediction logic
├── label_encoder.pkl    # For decoding predicted labels
├── model.pkl            # Trained ML model
│
├── templates/           # HTML templates
├── static/              # CSS or frontend assets
├── uploads/             # Uploaded files for prediction
├── datasets/            # (Excluded large CSVs)
│
├── visualizations.py    # For graph plotting
├── y_test.pkl
├── y_pred.pkl
│
├── docs/                # Final report and presentation
│   ├── Intel_program_project_report.docx
│   └── AIML for networking.pptx
│
├── requirements.txt
└── README.md
```

---

## 👥 Team Contribution

| Name         | Contribution                                       |
|--------------|----------------------------------------------------|
| Mohana Priya | Real-time prediction module, Flask UI, model integration |
| Inbaa        | Data cleaning, preprocessing, feature engineering |
| Mowriya      | Model training, hyperparameter tuning             |
| Jahnavi      | Evaluation metrics, graph plotting                |
| Sangeetha    | Documentation, PPT                                |

---

## 📂 Datasets

The datasets used in this project are too large to be hosted directly on GitHub.  
You can access them from the Google Drive link below:

👉 [Download Datasets from Google Drive](https://drive.google.com/file/d/1tIXIPh4-7f9SPI3ofVoervzzW_RX4K35/view?usp=sharing)

### Contents:
- Raw Threat Logs (`~73 MB`)
- Preprocessed Data (`~56 MB`)
- Encoded Dataset (`~129 MB`)
- Labeled Dataset (`~215 MB`)

---

## ⚙️ Running the App

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/intel-threat-prediction.git
   cd intel-threat-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Open your browser and go to:  
   `http://127.0.0.1:5000/`

---

## 📈 Model Performance

- Classification Accuracy: 97%
- Model: XGBoost Classifier
- Evaluation Metrics: Confusion Matrix, Precision, Recall

(See: `visualizations.py`, `y_test.pkl`, `y_pred.pkl`)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- Intel® Unnati Industrial Training Program
- Faculty Mentors & Peer Contributors
