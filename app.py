import streamlit as st
import pandas as pd
import random

# Load Igala numbers from CSV
vocabulary_df = pd.read_csv('igala_numbers.csv')
vocabulary = dict(zip(vocabulary_df['Igala'], vocabulary_df['English']))

# Function to get a random word
def get_word_of_the_day():
    igala_word = random.choice(list(vocabulary.keys()))
    english_word = vocabulary[igala_word]
    return igala_word, english_word

# Set page configuration
st.set_page_config(page_title="Igala to English Translator", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    body {
        background-color: #f0f4f8;
        color: #2c3e50;
        font-family: 'Arial', sans-serif;
    }
    .header {
        background-color: #2980b9;
        color: #ffffff;
        padding: 20px;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .stButton {
        background-color: #3498db;
        color: #ffffff;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton:hover {
        background-color: #2980b9;
    }
    .stTextArea {
        border-radius: 5px;
        border: 1px solid #bdc3c7;
        padding: 10px;
        font-size: 16px;
    }
    h1, h2 {
        font-family: 'Arial', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# Main App
def main():
    st.markdown("<div class='header'><h1>Igala to English Translator</h1></div>", unsafe_allow_html=True)
    
    # Word of the Day
    igala_word, english_word = get_word_of_the_day()
    st.subheader("Word of the Day")
    st.write(f"**Igala**: {igala_word}  |  **English**: {english_word}")

    st.subheader("Enter Igala Text Below:")
    igala_text = st.text_area("Igala Text", "", height=150)

    if st.button("Translate"):
        if igala_text:
            # Replace Igala numbers with English translations
            for igala_num, english_num in vocabulary.items():
                igala_text = igala_text.replace(igala_num, english_num)

            st.subheader("Translated Text:")
            st.write(igala_text)
        else:
            st.warning("Please enter some text to translate.")

    # Daily Challenge
    st.subheader("Daily Challenge")
    challenge_word = random.choice(list(vocabulary.keys()))
    st.write(f"Translate this word: **{challenge_word}**")

# Run the app
if __name__ == "__main__":
    main()
