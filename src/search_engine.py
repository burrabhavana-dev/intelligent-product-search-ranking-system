import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def search_products_v2(
    query,
    vectorizer,
    tfidf_matrix,
    df,
    clean_text,
    top_n=10
):

    query = clean_text(query)

    query_vector = vectorizer.transform([query])

    similarity_scores = cosine_similarity(
        query_vector,
        tfidf_matrix
    ).flatten()

    temp_df = df.copy()

    temp_df["similarity_score"] = similarity_scores

    candidate_df = temp_df.nlargest(
        100,
        "similarity_score"
    )

    candidate_df["final_score"] = (
        0.90 * candidate_df["similarity_score"]
        + 0.07 * candidate_df["rating_score"]
        + 0.03 * candidate_df["popularity_score"]
    )

    results = candidate_df.sort_values(
        "final_score",
        ascending=False
    )

    output = results[
        [
            "title",
            "brand",
            "category",
            "average_rating",
            "num_ratings",
            "similarity_score",
            "final_score"
        ]
    ].head(top_n)

    output = output.replace(
        [np.inf, -np.inf],
        0
    )

    output = output.fillna("")

    return output.to_dict(
        orient="records"
    )