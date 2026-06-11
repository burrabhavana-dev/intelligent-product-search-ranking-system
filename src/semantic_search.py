from sklearn.metrics.pairwise import cosine_similarity


def get_semantic_scores(
    query_embedding,
    candidate_embeddings
):
    """
    Compute semantic similarity scores.
    """

    scores = cosine_similarity(
        query_embedding,
        candidate_embeddings
    ).flatten()

    return scores