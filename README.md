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

### Use in Google colab

1. Mount google drive to a colab notebook
   
   ``` python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
2. Clone the Repository to Google Drive:
   ``` python
    !git clone https://github.com/danatal29/Bridezilla_NLP.git /content/drive/MyDrive/Bridezilla_NLP
   ```
3. Navigate to the cloned project run Bridezilla_Notebook.ipynb
4. Set up environment variables for OpenAI, Hugging Face and LangChain:
   Set up a file named `keys.json` with the following format:

   ```json
   {
     "openai_api_key": "your_openai_key",
     "huggingface_token": "your_huggingface_token",
     "langchain_api_key": "your_langchain_token"
   }
   
### Or Run with your own resouces
* Skip on the google colab parts
1. Clone the repository:

    ```bash
    git clone https://github.com/danatal29/Bridezilla_NLP.git
    cd Bridezilla_NLP
    ```
    
2. Navigate to Bridezilla_Notebook.ipynb and run the cells 

3. Set up environment variables for OpenAI, Hugging Face and LangChain:
   
   Set up a file named `keys.json` with the following format:

   ```json
   {
     "openai_api_key": "your_openai_key",
     "huggingface_token": "your_huggingface_token",
     "langchain_api_key": "your_langchain_token"
   }


## Project Structure

    ```bash
    Bridezilla_NLP/
    │
    ├── data/                     # Directory for visualization data-related files
    │
    ├── Bridezilla_Notebook.ipynb # Main Jupyter Notebook containing the project code
    ├── README.md                 # Documentation and instructions for using the repository
    │
    ├── graph_video.mp4           # Video file related to visualizations of the agent structure
    │
    ├── scraper.py                # Contains the GoogleReviewsScraper class for extracting Google reviews
    ├── summarizer.py             # Contains the TextSummarizer class for processing and summarizing reviews
    ├── utils.py                  # Utility functions used throughout the project
    │
    ├── visualize_agent.py        # Functions for visualizing the agent's operations
    ├── visualize_functions.py    # Additional visualization functions
    ```
