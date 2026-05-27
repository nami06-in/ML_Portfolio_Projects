import pickle

from src.preprocess import preprocess_input


# Load model
model = pickle.load(open('model/xgboost_model.pkl', 'rb'))

# # Load scaler
# scaler = pickle.load(open('model/scaler.pkl', 'rb'))


def predict_strength(cement, slag, ash, water,
                     superplastic, coarseagg,
                     fineagg, age):

    # Preprocess input
    data = preprocess_input(
        cement,
        slag,
        ash,
        water,
        superplastic,
        coarseagg,
        fineagg,
        age
    )

    # # Scale input
    # scaled_data = scaler.transform(data)

    # Predict
    prediction = model.predict(data)

    return round(prediction[0], 2)