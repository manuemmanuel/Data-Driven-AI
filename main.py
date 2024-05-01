import streamlit as st
import spacy
import pdfplumber
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.matcher import Matcher
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
nlp = spacy.load("en_core_web_lg")
stop_words = set(STOP_WORDS)

st.set_page_config(layout="wide")
st.title("Data-Driven AI")
st.subheader("Upload Any Type of File and Ask a Question")

def extract_text_from_pdf(file):
    text = ''
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def ask_openai(question, context):
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=context + "\nQuestion: " + question + "\nAnswer:",
        max_tokens=50
    )
    return response.choices[0].text.strip()

uploaded_file = st.file_uploader("Upload a file", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        file_content = extract_text_from_pdf(uploaded_file)
    else:
        file_content = uploaded_file.getvalue().decode()

    question = st.text_input("Enter your question:")

    if question:
        answer = ask_openai(question, file_content)
        st.markdown("#### Answer ####")
        st.info(answer)
