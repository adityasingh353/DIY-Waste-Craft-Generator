import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()   # <-- ye missing tha

API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_idea(waste, product_type):
    prompt = f"""
    Waste items: {waste}
    Product type: {product_type}

    Suggest a DIY product that can be made.
    Give:
    - product name
    - items required
    - steps
    - difficulty
    """

    response = model.generate_content(prompt)
    return response.text