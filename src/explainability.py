def generate_explanation(
    product,
    parsed_query
):

    reasons = []

    # Brand

    if parsed_query["brand"]:

        reasons.append(
            f"{parsed_query['brand']} brand match"
        )

    # Category

    if parsed_query["category"]:

        reasons.append(
            f"{parsed_query['category']} category match"
        )

    # Intent

    if parsed_query["intent"] != "general":

        reasons.append(
            f"{parsed_query['intent']} intent detected"
        )

    # Semantic relevance

    if product["semantic_score"] > 0.50:

        reasons.append(
            "High semantic relevance"
        )

    # Rating

    if product["average_rating"] >= 4:

        reasons.append(
            "Highly rated product"
        )

    # Popularity

    if product["num_ratings"] >= 50:

        reasons.append(
            "Popular among users"
        )

    return reasons