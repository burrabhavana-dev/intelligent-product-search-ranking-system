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
        json={"query": query}
    )


    data = response.json()

    results = data["results"]

    st.subheader(f"Results ({len(results)})")

    for idx, product in enumerate(results, start=1):

        st.markdown("---")

        st.markdown(
            f"""
        ### 🏆 Rank #{idx}

        ## {product['title']}

        🏷 **Brand:** {product['brand']}

        📦 **Category:** {product['category']}

        ⭐ **Rating:** {product['average_rating']}

        👥 **Reviews:** {product['num_ratings']}

        🎯 **Score:** {round(product['final_score'],4)}
        """
        )

        if "explanation" in product:

            st.markdown("### 🧠 Why this result?")

            for reason in product["explanation"]:

                st.markdown(f"✅ {reason}")