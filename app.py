import streamlit as st
import joblib
from gemini_helper import generate_idea


# load model
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
le = joblib.load("label_encoder.pkl")


def predict_product_type(text):
    text_vec = vectorizer.transform([text])
    pred = model.predict(text_vec)
    label = le.inverse_transform(pred)
    return label[0]


st.title("AI Waste to Product Generator")

waste = st.text_input("Enter waste items")

if st.button("Generate"):

    if waste:

        product_type = predict_product_type(waste)

        st.write("Predicted type:", product_type)

        idea = generate_idea(waste, product_type)

        st.write(idea)

 
        