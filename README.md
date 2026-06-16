# Intelligent Product Search and Ranking System

## Overview

The Intelligent Product Search and Ranking System is an AI-powered product retrieval application that combines traditional information retrieval techniques with modern semantic search methods.

The system is designed to improve product discovery by understanding user intent, extracting structured information from search queries, and ranking products using multiple relevance signals.

Unlike traditional keyword-based search systems, this project incorporates semantic understanding, query parsing, hybrid ranking, and explainable search results.

---

## Objectives

The primary objectives of this project are:

- Improve search relevance beyond exact keyword matching.
- Understand user intent from natural language queries.
- Combine semantic search with traditional retrieval methods.
- Rank products using multiple relevance signals.
- Provide explanations for why products appear in search results.
- Deliver search functionality through a REST API and web interface.

---

## Key Features

### 1. Keyword-Based Search

The system uses TF-IDF vectorization and cosine similarity to retrieve products based on keyword relevance.

Features:

- Text preprocessing
- TF-IDF vectorization
- Cosine similarity scoring
- Efficient retrieval

---

### 2. Semantic Search

Semantic search is implemented using Sentence Transformers.

Features:

- Dense vector embeddings
- Semantic similarity computation
- Context-aware retrieval
- Improved handling of natural language queries

Example:

Query:

```text
best apple phone
```

The system understands the semantic relationship between:

```text
Apple Phone → iPhone
```

and retrieves relevant products.

---

### 3. Query Understanding

The query parser extracts structured information from user queries.

The system identifies:

- Brand
- Category
- Search Intent

Example:

Query:

```text
budget samsung mobile
```

Parsed Output:

```python
{
    "brand": "Samsung",
    "category": "Mobile",
    "intent": "budget"
}
```

---

### 4. Brand Alias Recognition

The system supports common brand aliases and product family names.

Examples:

Alias-Brand 
iphone-Apple
ipad-Apple 
macbook-Apple 
galaxy-Samsung 
thinkpad-Lenovo 
victus-HP

This improves retrieval quality for real-world user queries.

---

### 5. Candidate Filtering

Before ranking, the system narrows the search space using extracted query information.

Example:

Total Products:

```text
1666
```

Query:

```text
budget samsung mobile
```

After filtering:

```text
64 Samsung Mobile Products
```

This improves both efficiency and relevance.

---

### 6. Hybrid Ranking

Product ranking is based on a weighted combination of multiple signals.

Ranking Components:

- Semantic Similarity
- TF-IDF Similarity
- Product Rating
- Product Popularity

Final Ranking Formula:

```python
Final Score =
0.55 * Semantic Score +
0.25 * TF-IDF Score +
0.15 * Rating Score +
0.05 * Popularity Score
```

---

### 7. Explainable Search Results

The system provides explanations for ranked products.

Example:

```text
Apple brand match
Mobile category match
High semantic relevance
Highly rated product
Popular among users
```

This increases transparency and user trust.

---

## System Architecture

```text
User Query
      │
      ▼
Query Understanding
      │
      ├── Brand Detection
      ├── Category Detection
      └── Intent Detection
      │
      ▼
Candidate Filtering
      │
      ▼
TF-IDF Search
      │
      ▼
Semantic Search
      │
      ▼
Hybrid Ranking
      │
      ▼
Explainability Layer
      │
      ▼
FastAPI Backend
      │
      ▼
Streamlit Frontend
```

---

## Project Structure

```text
product-search-ranking/
│
├── api/
│   └── app.py
│
├── data/
│   └── clean_products.csv
│
├── models/
│   ├── vectorizer.pkl
│   ├── tfidf_matrix.pkl
│   └── product_embeddings.pkl
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── semantic_search.ipynb
│   ├── hybrid_search.ipynb
│   └── query_understanding.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── query_parser.py
│   ├── search_engine.py
│   ├── ranking.py
│   └── explainability.py
│
├── ui/
│   └── streamlit_app.py
│
├── requirements.txt
└── README.md
```

---

## Search Workflow

### User Query

```text
best thinkpad laptop
```

### Query Understanding

```python
{
    "brand": "Lenovo",
    "category": "Laptop",
    "intent": "quality"
}
```

### Candidate Filtering

```text
1666 Products
↓
Lenovo Laptop Products
```

### Retrieval

- TF-IDF Search
- Semantic Search

### Ranking

Products are ranked using:

- Semantic similarity
- Keyword similarity
- Ratings
- Popularity

### Output

```text
Lenovo ThinkPad E15 Gen 4 Laptop
```

### Explanation

```text
Lenovo brand match
Laptop category match
High semantic relevance
Highly rated product
```

---

## REST API

### Endpoint

```http
POST /search
```

### Request

```json
{
  "query": "best iphone"
}
```

### Response

```json
{
  "query": "best iphone",
  "results": [
    {
      "title": "Apple iPhone 11",
      "category": "Mobile",
      "average_rating": 5,
      "semantic_score": 0.53,
      "final_score": 0.55,
      "explanation": [
        "Apple brand match",
        "Mobile category match",
        "High semantic relevance",
        "Highly rated product"
      ]
    }
  ]
}
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Sentence Transformers
- FastAPI
- Streamlit
- Uvicorn
- Git
- GitHub

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/product-search-ranking.git

cd product-search-ranking
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Start the FastAPI Server

```bash
uvicorn api.app:app --reload
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

### Start the Streamlit Application

```bash
streamlit run ui/streamlit_app.py
```

Application URL:

```text
http://localhost:8501
```

---

## Results

The system successfully integrates:

- Keyword-based retrieval
- Semantic search
- Query understanding
- Brand alias recognition
- Candidate filtering
- Hybrid ranking
- Explainable AI
- REST API deployment
- Interactive web interface

---

## Future Enhancements

Potential improvements include:

- Advanced filtering options
- Query auto-completion
- Personalized recommendations
- Vector database integration
- Large Language Model (LLM) query rewriting
- Conversational product search

---

## Author

Bhavana Burra
