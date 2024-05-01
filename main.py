import streamlit as st
import openai
import pathway as pw
import pdfplumber

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'sk-proj-F5p2Y1nCiKFFUs947bXsT3BlbkFJAZyg4PfRfRTMTQcIwnXc'

st.title('Data-Driven AI Assistant')

# Streamlit widget to upload PDF files
uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

# Streamlit widget for user to type in their question
question = st.text_input("What would you like to know from the data?")

# Button to trigger the analysis
if st.button('Analyze'):
    if uploaded_file is not None and question:
        # Read text from the uploaded PDF
        with pdfplumber.open(uploaded_file) as pdf:
            pdf_text = "\n".join([page.extract_text() for page in pdf.pages])

        # Define the schema of your data (Optional)
        class InputSchema(pw.Schema):
            text: str

        # Create an input table with the extracted PDF text
        input_table = pw.Table.from_records([{"text": pdf_text}], schema=InputSchema)

        # Define your operations on the data
        filtered_table = input_table.filter(input_table.text != "")
        result_table = filtered_table.reduce(
            sum_value=pw.reducers.count(filtered_table.text)
        )

        # Load your results to external systems
        pw.io.jsonlines.write(result_table, "output.jsonl")

        # Use OpenAI API to answer the question based on the data
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Data: {result_table}\nQuestion: {question}\nAnswer:",
            max_tokens=150
        )

        # Extract the response
        answer = response.choices[0].text.strip()

        # Display the answer
        st.write('Answer:', answer)
    else:
        st.error("Please upload a PDF file and ask a question.")
