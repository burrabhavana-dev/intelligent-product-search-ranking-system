# Intelligent Product Search & Ranking System

## Overview

An AI-powered product search and ranking system built using:

- TF-IDF Vectorization
- Cosine Similarity
- Product Ranking
- FastAPI

The system returns relevant products based on search queries and ranks them using relevance, ratings, and popularity.

---

## Features

- Product Search
- TF-IDF Retrieval
- Ranking Engine
- FastAPI Backend
- Swagger Documentation

---

## Project Structure

```text
api/
data/
models/
src/
notebooks/
```

---

## Run Locally

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start API

```bash
python -m uvicorn api.app:app --reload
```

### Open Swagger

```text
http://127.0.0.1:8000/docs
```

---

## Example Request

```json
{
  "query": "iphone 128gb"
}
```

---

## Author

Bhavana Burra
M.Tech Software Engineering