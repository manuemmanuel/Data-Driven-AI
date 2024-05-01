# Data-Driven AI Streamlit App

This Streamlit app allows users to upload various types of files (PDF, DOCX, TXT) and ask questions related to the content of the file. The app uses the OpenAI API to provide answers to the user's questions.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Docker (optional, for containerization)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/manuemmanuel/Data-Driven-AI.git

2. Navigate to the project directory:
   ```bash
   cd data-driven-ai

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt

### Usage

1. Run the Streamlit app locally:
    ```bash
    streamlit run main.py

2. Open your web browser and go to http://localhost:port to access the app.
3. Upload a file (PDF, DOCX, or TXT) using the file uploader.
4. Enter your question related to the content of the uploaded file.



### Docker

You can also run the Streamlit app using Docker:

Build the Docker image:
    ```bash
    docker build -t streamlit-app .```

Run a Docker container based on the built image:
    ```bash
    docker run -p 8501:8501 streamlit-app```
Access the app in your web browser at http://localhost:port.
