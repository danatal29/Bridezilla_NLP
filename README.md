# Bridezilla_NLP
Project Idea:
Compare 2 businesses (hotel, restaurant etc.)
by extracting their positive and negative characteristics.
Create a tool that extract their unique features. 

The Process:
STEP 1:
Scrape reviews – a lot(!) of headache.
We used Selenium (browser automation tool).

STEP 2:
Load reviews into dataframe and summarize each with BART.

STEP 3:
Concatenate all reviews in dataframe and analyze with llama3 with different prompts.

STEP 4:
Create LangChain Agent and run all steps automatically.


