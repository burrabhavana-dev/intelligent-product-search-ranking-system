from fastapi import FastAPI
from pydantic import BaseModel

import pickle

from src.preprocessing import clean_text
from src.search_engine import search_products_v2

app = FastAPI()


class SearchRequest(BaseModel):
    query: str


with open("models/products.pkl", "rb") as f:
    df = pickle.load(f)

with open("models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("models/tfidf_matrix.pkl", "rb") as f:
    tfidf_matrix = pickle.load(f)


@app.get("/")
def home():

    return {
        "message": "Product Search Engine API Running"
    }


@app.post("/search")
def search(request: SearchRequest):

    results = search_products_v2(
        request.query,
        vectorizer,
        tfidf_matrix,
        df,
        clean_text
    )

    return {
        "query": request.query,
        "results": results
    }