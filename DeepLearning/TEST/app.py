import streamlit as st
import pickle
from keras.preprocessing.sequence import pad_sequences
from keras.datasets import imdb

# Load the pre-trained model from pickle
with open('sentiment_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load IMDb word index
word_index = imdb.get_word_index()

def preprocess_text(text):
    # Preprocess input text by converting words to integers
    text = text.lower().split()
    text = [word_index.get(word, 0) for word in text]
    text = pad_sequences([text], maxlen=500)
    return text

# Streamlit Interface
st.title("Movie Review Sentiment Analysis")
review = st.text_area("Enter a movie review")

if st.button("Predict Sentiment"):
    if review:
        preprocessed_review = preprocess_text(review)
        prediction = model.predict(preprocessed_review)
        sentiment = "Positive" if prediction >= 0.5 else "Negative"
        st.write(f"Sentiment: {sentiment}")
    else:
        st.write("Please enter a review.")