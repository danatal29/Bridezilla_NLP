import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
from transformers import pipeline
Name1 = "Selina"
Name2 = "Cliff\'s"


def calculate_date(months_ago):
    """
    calculate the date X months ago
    """
    return datetime.now() - relativedelta(months=months_ago)

def time_to_months(time_str):
    """
    convert "months ago" to exact month and year date format
    """
    # Extract the number and unit (year/month)
    match = re.search(r'(\d+|\ba\b)\s+(year|month|week|day)', time_str)
    if match:
        number_str, unit = match.groups()
        number = 1 if number_str == 'a' else int(number_str)

        if 'year' in unit:
            date = calculate_date(number * 12)
        elif 'month' in unit:
            date = calculate_date(number)
        elif 'week' in unit:
            date = calculate_date(number // 4)  # Approximate weeks to months
        elif 'day' in unit:
            date = calculate_date(number // 30)  # Approximate days to months
        return pd.Timestamp(date).to_period('M')  # Approximate days to months
    return np.nan  # Return NaN for unmatched strings


def score_sentiment(text, classifier):
    """
    classify sentiment of a review to a value between 0 and 1
    """
    # Load pre-trained sentiment-analysis pipeline
    result = classifier(text)[0]
    if result['label'] == "POSITIVE":
        return result['score']
    else:
        return 1 - result['score']


def get_sentiment_over_time(df, classifier):
  # Create a column of the month and year of the review
  df['year_month'] = df['time'].apply(time_to_months)

  # Create a column of the sentiment score of the review
  df['sentiment_score'] = df['text'].apply(lambda x: score_sentiment(x, classifier))
  # Aggregate sentiment scores by month and year
  sentiment_over_time = df.groupby('year_month')['sentiment_score'].mean().reset_index()
  return sentiment_over_time


def get_common_dates(sentiment_over_time, common_dates):
# Filter the dataframes to only include the common dates
  sentiment_over_time = sentiment_over_time[sentiment_over_time['year_month'].isin(common_dates)]

  # Sort the dataframes by 'year_month'
  sentiment_over_time = sentiment_over_time.sort_values('year_month')
  return sentiment_over_time





def plot_sentiment_over_time(sentiment_over_time1, sentiment_over_time2, name1, name2):
  plt.plot(sentiment_over_time1['year_month'], sentiment_over_time1['sentiment_score'], marker='o', label=Name1)
  plt.plot(sentiment_over_time2['year_month'], sentiment_over_time2['sentiment_score'], marker='o', label=Name2)
  plt.title('Sentiment Over Time')
  plt.xlabel('Date')
  plt.ylabel('Average Sentiment')
  plt.grid(True)
  plt.legend()
  #plt.xticks(rotation=90)
  plt.show()
