# GPT LangChain AI Assistant for PDF Chat

![GPT LangChain AI Assistant](insert_image_url_here)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Introduction

Welcome to the GPT LangChain AI Assistant for PDF Chat! This project leverages the power of LangChain, OpenAI's GPT-3.5 model, and various Python libraries to create a chatbot that can answer questions about the content of a PDF file. With this tool, you can easily extract information and insights from PDF documents using natural language queries.

## Features

- Upload and analyze PDF files.
- Extract text from PDF files.
- Generate embeddings for the extracted text.
- Ask natural language questions about the PDF content.
- Receive answers based on the embedded information.

## Installation

To get started with the GPT LangChain AI Assistant for PDF Chat, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/gpt-langchain-pdf-chat.git
   cd gpt-langchain-pdf-chat
   ```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

Create a .env file with your OpenAI API key. You can obtain an API key from the OpenAI platform.

```dotenv
OPENAI_API_KEY=your_api_key_here
Run the application:
```

```bash
streamlit run app.py
```

Usage
Launch the application using the provided command.
Upload a PDF file that you want to analyze.
The application will extract text from the PDF and generate embeddings for it.
Enter your questions or queries about the PDF content in the text input field.
The AI assistant will provide answers based on the embedded information from the PDF.
Dependencies
The GPT LangChain AI Assistant for PDF Chat relies on the following Python libraries and tools:

Streamlit: Used for building the user interface.
PyPDF2: Used for extracting text from PDF files.
LangChain: Provides text splitting, embeddings, and vector store capabilities.
OpenAI: Utilizes the OpenAI GPT-3.5 model for question answering.
Faiss: A library for efficient similarity search and clustering of dense vectors.
License
This project is licensed under the MIT License.

Feel free to contribute, report issues, or provide feedback to help improve this AI assistant for PDF chat!
