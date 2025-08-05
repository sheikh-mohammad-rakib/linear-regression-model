# Linear Regression Model

This project is a simple web application that demonstrates a linear regression model using Python, Flask, and scikit-learn. The app allows users to input data and receive predictions based on a pre-trained linear regression model.

## Features
- Web interface for making predictions
- Pre-trained linear regression model (`linear_regression_model.pkl`)
- User-friendly UI with HTML and CSS

## Project Structure

```
linear-regression-model/
├── app.py                   # Main Flask application
├── linear_regression_model.pkl  # Serialized linear regression model
├── requirements.txt         # Python dependencies
├── static/
│   └── style.css            # CSS for styling
├── templates/
│   └── index.html           # HTML template
└── README.md                # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd linear-regression-model
   ```


2. **Create a virtual environment (optional but recommended):**
   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **Linux/macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**
   - **Windows:**
     ```bash
     pip install -r requirements.txt
     ```
   - **Linux/macOS:**
     ```bash
     pip3 install -r requirements.txt
     ```

4. **Run the application:**
   - **Windows:**
     ```bash
     python app.py
     ```
   - **Linux/macOS:**
     ```bash
     python3 app.py
     ```

5. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000/
   ```

## Usage

1. Enter the required input values in the web form.
2. Click the "Predict" button to get the model's prediction.
3. The result will be displayed on the page.

## Requirements

- Python 3.7+
- Flask
- scikit-learn
- (See `requirements.txt` for the full list)

## Model Training

The file `linear_regression_model.pkl` contains a pre-trained linear regression model. If you wish to retrain the model, update the training script (not included here) and re-save the model using `joblib` or `pickle`.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [scikit-learn](https://scikit-learn.org/)