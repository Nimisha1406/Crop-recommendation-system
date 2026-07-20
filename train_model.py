import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ==========================
# Load Dataset
# ==========================

print("Loading dataset...")

df = pd.read_csv("crop_recommendation.csv")

print("Dataset Loaded Successfully!")
print(df.head())


# ==========================
# Features and Target
# ==========================

X = df.drop("label", axis=1)
y = df["label"]


# ==========================
# Train-Test Split
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


# ==========================
# Random Forest Model
# ==========================

print("\nTraining Random Forest Model...")

model = RandomForestClassifier(
    n_estimators=200, random_state=42, max_depth=None, criterion="gini"
)

model.fit(X_train, y_train)


# ==========================
# Prediction
# ==========================

y_pred = model.predict(X_test)


# ==========================
# Accuracy
# ==========================

accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print(f"Accuracy : {accuracy*100:.2f}%")
print("==============================")

print("\nClassification Report\n")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix\n")
print(confusion_matrix(y_test, y_pred))


# ==========================
# Save Model
# ==========================

joblib.dump(model, "model.pkl")

print("\nModel Saved Successfully!")
print("Filename : model.pkl")


# ==========================
# Feature Importance
# ==========================

importance = pd.DataFrame(
    {"Feature": X.columns, "Importance": model.feature_importances_}
)

importance = importance.sort_values(by="Importance", ascending=False)

print("\nFeature Importance\n")
print(importance)


print("\nTraining Completed Successfully.")
