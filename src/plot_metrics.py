
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import pandas as pd
import joblib

# Load data and model
df = pd.read_csv("data/iris.csv")
X = df.drop("species", axis=1)
y = df["species"]
model = joblib.load("model.joblib")

# Predict
y_pred = model.predict(X)

# Confusion matrix
cm = confusion_matrix(y, y_pred, labels=model.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot()

# Save plot
plt.savefig("metrics.png")

# Create report.md
with open("report.md", "w") as f:
    f.write("# Model Evaluation Report\n\n")
    f.write("![Confusion Matrix](metrics.png)\n")
