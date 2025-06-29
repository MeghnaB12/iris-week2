import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_model():
    # Load the data
    df = pd.read_csv("data/iris.csv")
    X = df.drop("species", axis=1)
    y = df["species"]

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    # Predict
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print("Accuracy:", acc)

    # Save model and metrics
    joblib.dump(clf, "model.joblib")
    with open("metrics.csv", "w") as f:
        f.write(f"accuracy,{acc}\n")

    return clf, acc

if __name__ == "__main__":
    train_model()

