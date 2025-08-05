from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('linear_regression_model.pkl')

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        engine_size = float(request.form.get('engine_size'))
        prediction = model.predict(np.array([[engine_size]]))[0]
        return render_template('index.html', prediction=prediction, engine_size=engine_size)
    except Exception as e:
        return render_template('index.html', prediction="Error: " + str(e), engine_size=None)

if __name__ == "__main__":
    app.run(debug=True)