import google.generativeai as genai

API_KEY = "Your_gemini_api_key_here"  

genai.configure(api_key="Your_gemini_api_key_here")

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
