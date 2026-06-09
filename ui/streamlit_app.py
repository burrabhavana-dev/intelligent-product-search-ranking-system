import streamlit as st
import requests

st.set_page_config(
    page_title="Product Search Engine",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Intelligent Product Search Engine")

query = st.text_input(
    "Search Product",
    placeholder="Example: iphone 128gb"
)

if st.button("Search"):

    response = requests.post(
        "http://127.0.0.1:8000/search",
        json={
            "query": query
        }
    )

    results = response.json()["results"]

    st.subheader("Results")

    for product in results:

        st.write("---")

        st.write(
            f"### {product['title']}"
        )

        st.write(
            f"Brand: {product['brand']}"
        )

        st.write(
            f"Rating: {product['average_rating']}"
        )

        st.write(
            f"Reviews: {product['num_ratings']}"
        )

        st.write(
            f"Final Score: {round(product['final_score'], 4)}"
        )