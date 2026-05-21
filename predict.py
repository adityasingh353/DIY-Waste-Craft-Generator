import joblib
from gemini_helper import generate_idea

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
le = joblib.load("label_encoder.pkl")


def predict_product_type(text):
    text_vec = vectorizer.transform([text])
    pred = model.predict(text_vec)
    label = le.inverse_transform(pred)
    return label[0]


if __name__ == "__main__":

    waste = input("Enter waste items: ")

    product_type = predict_product_type(waste)

    print("Predicted type:", product_type)

    idea = generate_idea(waste, product_type)

    print("\nGemini Idea:\n")
    print(idea)