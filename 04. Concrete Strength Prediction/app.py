from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open('model/xgboost_model.pkl', 'rb'))

# Home page
@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


# Prediction route
@app.route('/predict', methods=['POST'])
def predict():

    # prediction code comes here

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)