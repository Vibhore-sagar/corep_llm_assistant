import streamlit as st
import requests

st.title("📊 COREP Regulatory Assistant")

query = st.text_area(
    "Describe the reporting scenario:"
)

if st.button("Generate COREP"):

    response = requests.get(
        "http://127.0.0.1:8000/generate_corep",
        params={"query": query}
    )

    data = response.json()

    st.subheader("COREP Fields")

    for field in data["fields"]:
        st.write(field)

    if data["missing_data"]:
        st.warning(f"Missing Data: {data['missing_data']}")

    if data["validation_errors"]:
        st.error(data["validation_errors"])
