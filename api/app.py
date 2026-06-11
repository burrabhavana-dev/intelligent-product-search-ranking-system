from fastapi import FastAPI
from pydantic import BaseModel

import pickle

from src.preprocessing import clean_text
from src.search_engine import search_products_v5

from sentence_transformers import SentenceTransformer
import pandas as pd

app = FastAPI()


class SearchRequest(BaseModel):
    query: str


df = pd.read_csv(
    "data/clean_products.csv"
)

with open("models/product_embeddings.pkl", "rb") as f:
    product_embeddings = pickle.load(f)

with open("models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("models/tfidf_matrix.pkl", "rb") as f:
    tfidf_matrix = pickle.load(f)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

@app.get("/")
def home():

    return {
        "message": "Product Search Engine API Running"
    }


@app.post("/search")
def search(request: SearchRequest):

    results = search_products_v5(
        request.query,
        vectorizer,
        tfidf_matrix,
        product_embeddings,
        model,
        df,
        clean_text
    )

    return {
        "query": request.query,
        "results": results
    }