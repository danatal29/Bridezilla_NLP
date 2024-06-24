# Bridezilla_NLP

Project Idea
Bridezilla_NLP aims to compare two businesses (such as hotels, restaurants, etc.) by extracting their positive and negative characteristics. The goal is to create a tool that highlights their unique features.

The Process
STEP 1: Scrape Reviews
Scraping reviews can be a challenging and time-consuming task. We used Selenium, a powerful browser automation tool, to automate the process of collecting reviews from various sources.

STEP 2: Summarize Reviews
The collected reviews are loaded into a DataFrame. Each review is then summarized using BART (Bidirectional and Auto-Regressive Transformers) to distill the essence of the feedback.

STEP 3: Analyze Reviews
All summarized reviews are concatenated into a single DataFrame and analyzed using LLaMA3 (Large Language Model Meta AI) with different prompts to extract meaningful insights.

STEP 4: Automate with LangChain
A LangChain Agent is created to automate all the steps, ensuring a seamless and efficient workflow.
