# Bridezilla_NLP

Bridezilla_NLP is a project designed to compare two businesses (such as hotels or museums) based on data from Google reviews. The goal is to extract unique positive and negative aspects for each place from these reviews. This project utilizes an agent implemented with the LangGraph library and an LLM named Llama 3 from Facebook.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Bridezilla_NLP project aims to provide insights into the unique positive and negative characteristics of two businesses by analyzing their Google reviews. The process involves scraping the reviews, summarizing them, and using natural language processing techniques to highlight the distinct features of each business.

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

3. Set up environment variables for OpenAI and Hugging Face:

    Add your OpenAI key:

    ```bash
    export OPENAI_API_KEY='your_openai_key'
    ```

    Add your Hugging Face token:

    ```bash
    export HUGGINGFACE_TOKEN='your_huggingface_token'
    ```

4. Set up the LangGraph library and Llama 3:

    Detailed setup instructions for LangGraph can be found [here](#).
    Detailed setup instructions for Llama 3 can be found [here](#).

## Usage

To use the Bridezilla_NLP project, follow these steps:

1. **Scrape Reviews:** Use the agent to scrape reviews from Google for the two businesses you want to compare.
2. **Summarize Reviews:** The agent will summarize the scraped reviews.
3. **Analyze Reviews:** Insert the summarized reviews into the Llama 3 model to analyze and compare the unique aspects of each business.

Example usage:

    ```python
    from langgraph import LangGraph
    from llama3 import Llama3

    # Define the scrape and summarize functions
    def scrape_function(url):
        # Implement scraping logic here
        pass

    def summarize_function(reviews):
        # Implement summarization logic here
        pass

    # Initialize the agent with LangGraph
    agent = LangGraph(scrape_function, summarize_function)

    # Scrape and summarize reviews
    reviews_summary = agent.process(url1, url2)

    # Analyze reviews with Llama 3
    analysis = Llama3.analyze(reviews_summary)
    print(analysis)
    ```

## Project Structure

    ```bash
    Bridezilla_NLP/
    │
    ├── data/
    │   ├── raw/                # Raw data from scraping
    │   └── processed/          # Processed and summarized data
    │
    ├── src/
    │   ├── scraping/           # Scraping scripts
    │   ├── summarization/      # Summarization scripts
    │   └── analysis/           # Analysis scripts using Llama 3
    │
    ├── tests/                  # Unit tests
    │
    ├── README.md
    └── requirements.txt        # Project dependencies
    ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
