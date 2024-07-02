# Bridezilla_NLP

Bridezilla_NLP is a project designed to compare two businesses (such as hotels or museums) based on data from Google reviews. The goal is to extract unique positive and negative aspects for each place from these reviews. This project utilizes an agent implemented with the LangGraph library and an LLM named Llama 3 from Facebook.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)


## Features

- **Review Scraping:** Collect reviews from Google for the specified businesses.
- **Review Summarization:** Summarize the collected reviews to capture the essence of user feedback.
- **Comparison Analysis:** Identify and compare the unique positive and negative aspects of each business.
- **Agent Integration:** Utilize an agent implemented with the LangGraph library for scraping and summarization tasks.
- **LLM Integration:** Use Llama 3 from Facebook for advanced natural language processing.

## Installation

To install and run the project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/danatal29/Bridezilla_NLP.git
    cd Bridezilla_NLP
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables for OpenAI, Hugging Face and LangChain:
   
   Set up a file named `keys.json` with the following format:

   ```json
   {
     "openai_api_key": "your_openai_key",
     "huggingface_token": "your_huggingface_token",
     "langchain_api_key": "your_langchain_token"
   }

4. Set up the LangGraph library and Llama 3:

    Detailed setup instructions for LangGraph can be found [here](#).
    Detailed setup instructions for Llama 3 can be found [here](#).

## Project Structure

    ```bash
    Bridezilla_NLP/
    │
    ├── data/
    │   ├── raw/                # Raw data from scraping
    │   └── processed/          # Processed and summarized data
    │
    ├── scraping/           # Scraping scripts
    │── summarization/      # Summarization scripts
    │── analysis/           # Analysis scripts using Llama 3
    │
    ├── README.md
    └── requirements.txt        # Project dependencies
    ```
