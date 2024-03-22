import pandas as pd
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List

# package imports 
from schemas import Review


class DataLoader:
    def __init__(self, url: str) -> None:
        # define class variables
        self.driver = webdriver.Chrome()
        self.review: List = None
        self.df: pd.DataFrame = pd.DataFrame(columns=['text_review', 'stars', 'time'])

        # init them 
        self.driver.get(url)
        return None

    def navigate(self):
        """
        navigate to the reviews page
        """
        xpath = "//button[contains(., 'ביקורות') or contains(., 'REVIEWS')]"
        wait = WebDriverWait(self.driver, 10)
        route_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        route_button.click()
        return
    
    def create_reviews_df(self)->pd.DataFrame:
        # Get a list of all of the reviews
        reviews = self.driver.find_elements(By.XPATH, "//div[@data-review-id]")
        print(f'the type of each review is: {type(reviews[0])}')

        for review in reviews:
            review_text = review.find_element(By.XPATH, f".//span[contains(@class, '{Review.TEXT.value}')]").text
            review_rating = review.find_element(By.XPATH, f".//span[contains(@class, '{Review.STARS.value}')]").get_attribute('aria-label')
            review_rating_int = int(re.search(r'\d', review_rating).group(0))
            review_time =  review.find_element(By.XPATH, f".//span[contains(@class, '{Review.TIME.value}')]").text
            row = pd.DataFrame( {'text_review': [review_text], 'stars': [review_rating_int], 'time': [review_time]} )
            self.df = pd.concat([self.df, row], ignore_index=True)

    
    def get_reviews_df(self):
        """
        all of the process
        """
        # TODO: didn't implement yet
        pass