"""
Query Understanding Module

Extracts:
1. Brand
2. Category
3. Intent

from a user search query.
"""

# Category Synonyms

CATEGORY_SYNONYMS = {
    "Mobile": [
        "mobile",
        "phone",
        "smartphone",
        "cell phone"
    ],

    "Laptop": [
        "laptop",
        "notebook"
    ],

    "Earbuds": [
        "earbuds",
        "earphones",
        "headphones",
        "buds"
    ],

    "Watch": [
        "watch",
        "smartwatch"
    ]
}
BRAND_ALIASES = {
    # Apple
    "iphone": "Apple",
    "ipad": "Apple",
    "macbook": "Apple",
    "airpods": "Apple",

    # Samsung
    "galaxy": "Samsung",

    # HP
    "victus": "HP",

    # Lenovo
    "thinkpad": "Lenovo",

    # Dell
    "inspiron": "Dell",
    "xps": "Dell",

    # Asus
    "rog": "Asus",
    "zenbook": "Asus",

    # Acer
    "aspire": "Acer",
    "predator": "Acer"
}

def get_brands(df):
    """
    Extract unique brands from dataframe.
    """

    brands = (
        df["brand"]
        .dropna()
        .unique()
        .tolist()
    )

    return brands


def extract_brand(query, brands):
    """
    Extract brand from query.
    Supports aliases like:
    iphone -> Apple
    galaxy -> Samsung
    """

    query = query.lower()

    # Alias Matching First

    for alias, brand in BRAND_ALIASES.items():

        if alias in query:
            return brand

    # Direct Brand Matching

    for brand in brands:

        if str(brand).lower() in query:
            return brand

    return None

def extract_category(query):
    """
    Extract category using synonym matching.
    """

    query = query.lower()

    for category, synonyms in CATEGORY_SYNONYMS.items():

        for synonym in synonyms:

            if synonym in query:
                return category

    return None


def detect_intent(query):
    """
    Detect search intent.
    """

    query = query.lower()

    # Cheapest Intent

    if any(
        word in query
        for word in [
            "cheap",
            "cheapest",
            "lowest price",
            "low price"
        ]
    ):
        return "cheapest"

    # Budget Intent

    if any(
        word in query
        for word in [
            "budget",
            "affordable",
            "economical"
        ]
    ):
        return "budget"

    # Quality Intent

    if any(
        word in query
        for word in [
            "best",
            "top",
            "highest rated",
            "premium"
        ]
    ):
        return "quality"

    return "general"


def parse_query(query, brands):
    """
    Parse query and return structured information.

    Example:
    --------
    Input:
        budget samsung mobile

    Output:
        {
            "brand": "Samsung",
            "category": "Mobile",
            "intent": "budget"
        }
    """

    return {
        "brand": extract_brand(query, brands),
        "category": extract_category(query),
        "intent": detect_intent(query)
    }