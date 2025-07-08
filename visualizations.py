import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd

# Load saved data
y_test = joblib.load('y_test.pkl')
y_pred = joblib.load('y_pred.pkl')
label_encoder = joblib.load('uploads/label_encoder.pkl')
class_names = label_encoder.classes_

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=class_names, yticklabels=class_names)
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.tight_layout()

plt.show()
plt.close()

# Classification Report Bar Chart
report = classification_report(y_test, y_pred, target_names=class_names, output_dict=True)
df_scores = pd.DataFrame(report).transpose().iloc[:-3]

df_scores[['precision', 'recall', 'f1-score']].plot(kind='bar', figsize=(6, 6))
plt.title("Class-wise Precision, Recall, F1-score")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.ylim(0, 2.5)
plt.tight_layout()
plt.savefig("classification_scores.png")
print("✅ Saved: classification_scores.png")
plt.show()
plt.close()

# Optional notes
top_class = df_scores['f1-score'].idxmax()
low_class = df_scores['f1-score'].idxmin()

print("✅ Done! Graphs and notes saved.")
