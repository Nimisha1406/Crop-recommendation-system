from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get values from form
        N = float(request.form["N"])
        P = float(request.form["P"])
        K = float(request.form["K"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        # Prepare input
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

        # Prediction
        prediction = model.predict(data)[0]

        # Confidence
        probability = model.predict_proba(data)
        confidence = round(np.max(probability) * 100, 2)

        return render_template("result.html", crop=prediction, confidence=confidence)

    except Exception as e:
        return f"Error : {e}"


if __name__ == "__main__":
    app.run(debug=True)
