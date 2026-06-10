import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from src.query_parser import (
    get_brands,
    parse_query
)

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

def search_products_v3(
    query,
    vectorizer,
    tfidf_matrix,
    df,
    clean_text,
    top_n=10
):
    """
    Query-Aware Search

    Uses:
    - Brand Extraction
    - Category Extraction
    - Intent Detection
    - Candidate Filtering
    - TF-IDF Ranking
    """

    brands = get_brands(df)

    parsed = parse_query(
        query,
        brands
    )

    working_df = df.copy()

    # Brand Filter

    if parsed["brand"]:

        working_df = working_df[
            working_df["title"]
            .str.contains(
                parsed["brand"],
                case=False,
                na=False
            )
        ]

    # Category Filter

    if parsed["category"]:

        working_df = working_df[
            working_df["category"]
            .str.lower()
            ==
            parsed["category"].lower()
        ]

    # Fallback

    if len(working_df) == 0:

        working_df = df.copy()

    # Build TF-IDF scores

    query_clean = clean_text(query)

    query_vector = vectorizer.transform(
        [query_clean]
    )

    similarity_scores = cosine_similarity(
        query_vector,
        tfidf_matrix
    ).flatten()

    temp_df = df.copy()

    temp_df["similarity_score"] = similarity_scores

    # Keep only filtered candidates

    temp_df = temp_df.loc[
        working_df.index
    ]

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