from flask import Flask, render_template, request

from src.predict import predict_strength


app = Flask(__name__)


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':

        cement = float(request.form['cement'])

        slag = float(request.form['slag'])

        ash = float(request.form['ash'])

        water = float(request.form['water'])

        superplastic = float(request.form['superplastic'])

        coarseagg = float(request.form['coarseagg'])

        fineagg = float(request.form['fineagg'])

        age = float(request.form['age'])

        # Predict strength

        output = predict_strength(
            cement,
            slag,
            ash,
            water,
            superplastic,
            coarseagg,
            fineagg,
            age
        )

        prediction_text = f"Predicted Concrete Strength: {output} MPa"

        return render_template(
            'index.html',
            prediction_text=prediction_text
        )

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)