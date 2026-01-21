import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# Load stopwords once
@st.cache_resource
def load_stopwords():
    return stopwords.words('english')

stop_words = load_stopwords()

# Load model and vectorizer once
@st.cache_resource
def load_model_and_vectorizer():
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    return model, vectorizer

model, vectorizer = load_model_and_vectorizer()

# Clean text
def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

# UI
st.title("Sentiment Analysis App 💬")
st.write("Enter a sentence and I will predict its sentiment.")

user_input = st.text_area("Enter your text here:")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        cleaned = clean_text(user_input)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)[0]

        if prediction == "Positive" or prediction == 1:
            st.success("😊 Positive Sentiment")
        else:
            st.error("😠 Negative Sentiment")
