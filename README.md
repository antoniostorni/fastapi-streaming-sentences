# FastAPI Streaming Sentences

This project is a demonstration of a FastAPI application that showcases real-time streaming of processed sentences. It utilizes asynchronous handling of text data, tokenizes input text, performs sentence detection using the Natural Language Toolkit (NLTK), and streams the processed sentences back to the client in real-time. This example serves as a practical demonstration of integrating natural language processing (NLP) techniques with FastAPI for dynamic content delivery.

## Features

- Asynchronous text processing and streaming
- Real-time tokenization and sentence detection
- Use of NLTK for natural language processing
- Integration of FastAPI with HTML and JavaScript for dynamic web content

## Installation

To install the required Python packages, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the FastAPI server, execute the following command:

```bash
uvicorn main:app --reload
```

## Runnning the Application with Docker

To run the FastAPI application using Docker, execute the following commands:

```bash
docker build -t fastapi-streaming-sentences .
docker run -d --name fastapi-streaming-sentences -p 9000:9000 fastapi-streaming-sentences
```

The application will be accessible at `http://localhost:9000`.


