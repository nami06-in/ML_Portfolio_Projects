import numpy as np
import pandas as pd


def preprocess_input(cement, slag, ash, water,
                     superplastic, coarseagg,
                     fineagg, age):

    # =========================
    # Feature Engineering
    # =========================

    water_cement_ratio = water / cement

    total_agg = coarseagg + fineagg

    binder = cement + slag + ash

    slag_ratio = slag / binder

    ash_ratio = ash / binder

    agg_binder_ratio = total_agg / binder

    # =========================
    # Create DataFrame
    # =========================

    data = pd.DataFrame({
        'cement': [cement],
        'slag': [slag],
        'ash': [ash],
        'water': [water],
        'superplastic': [superplastic],
        'coarseagg': [coarseagg],
        'fineagg': [fineagg],
        'age': [age],
        'water_cement_ratio': [water_cement_ratio],
        'total_agg': [total_agg],
        'binder': [binder],
        'slag_ratio': [slag_ratio],
        'ash_ratio': [ash_ratio],
        'agg_binder_ratio': [agg_binder_ratio]
    })

    # =========================
    # Log Transformation
    # =========================

    skewed_features = [
        'slag',
        'ash',
        'superplastic',
        'age',
        'water_cement_ratio',
        'slag_ratio',
        'ash_ratio'
    ]

    for col in skewed_features:
        data[col] = np.log1p(data[col])

    # =========================
    # Outlier Handling
    # =========================

    fineagg_upper_limit = 969.0500000000002
    fineagg_median = 780.0

    if data['fineagg'][0] > fineagg_upper_limit:
        data['fineagg'] = fineagg_median

    return data