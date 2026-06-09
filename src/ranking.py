import numpy as np
from sklearn.preprocessing import MinMaxScaler


def create_ranking_features(df):

    scaler = MinMaxScaler()

    df["rating_score"] = scaler.fit_transform(
        df[["average_rating"]]
    )

    df["popularity_score"] = np.log1p(
        df["num_ratings"]
    )

    scaler = MinMaxScaler()

    df["popularity_score"] = scaler.fit_transform(
        df[["popularity_score"]]
    )

    return df