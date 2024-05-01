import streamlit as st
import openai
import pathway
import pandas as pd
import pdfplumber
import docx

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'sk-proj-F5p2Y1nCiKFFUs947bXsT3BlbkFJAZyg4PfRfRTMTQcIwnXc'

st.title('AI Data Analyst')

# Streamlit widget to upload files
uploaded_file = st.file_uploader("Upload your data file", type=["csv", "pdf", "docx", "txt"])

# Streamlit widget for user to type in their question
question = st.text_input("What would you like to know from the data?")

# Function to process different file types
def process_file(uploaded_file):
    if uploaded_file is not None:
        # Process CSV files
        if uploaded_file.type == "text/csv":
            df = pd.read_csv(uploaded_file)
            return df.to_json()
        # Process PDF files
        elif uploaded_file.type == "application/pdf":
            with pdfplumber.open(uploaded_file) as pdf:
                text = "\n".join([page.extract_text() for page in pdf.pages])
            return text
        # Process DOCX files
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = docx.Document(uploaded_file)
            text = "\n".join([para.text for para in doc.paragraphs])
            return text
        # Process TXT files
        elif uploaded_file.type == "text/plain":
            text = uploaded_file.read().decode('utf-8')
            return text
    return None

# Button to trigger the analysis
if st.button('Analyze'):
    if uploaded_file is not None and question:
        # Process the uploaded file
        data = process_file(uploaded_file)

        # Use OpenAI API to answer the question based on the data
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Data: {data}\nQuestion: {question}\nAnswer:",
            max_tokens=150
        )

        # Extract the response
        answer = response.choices[0].text.strip()

        # Display the answer
        st.write('Answer:', answer)
    else:
        st.error("Please upload a file and ask a question.")
