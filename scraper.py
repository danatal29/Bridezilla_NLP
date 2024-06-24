from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd

class GoogleReviewsScraper:
    def __init__(self, url):
        self.url = url
        self.driver = self.init_driver()

    def init_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(self.url)
        return driver



    def translate_page_to_english(self):
        try:
            time.sleep(5)
            wait = WebDriverWait(self.driver, 1)
            menu_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[1]/ul/li[1]/button/div'
            menu_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, menu_xpath)))
            menu_xpath.click()
            time.sleep(5)
            wait = WebDriverWait(self.driver, 1)
            lan = '//*[@id="settings"]/div/div[2]/ul/div[7]/li[1]/button'
            language_button = wait.until(EC.element_to_be_clickable((By.XPATH, lan)))
            language_button.click()
            time.sleep(5)
            wait = WebDriverWait(self.driver, 1)

            # Click on the English language
            english_xpath = '//*[@id="modal-dialog"]/div/div[2]/div/div[2]/div/div/div/div[3]/div[1]/div[11]/a'
            anchor_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, english_xpath))
            )
            anchor_element.click()
        except Exception as e:
            print(e)

    def scroll_down_google_reviews(self, total_number_of_reviews=50):
        def expand_more_buttons(driver):
            more_buttons = driver.find_elements(By.XPATH, "//button[@aria-label='See more']")
            for button in more_buttons:
                try:
                    driver.execute_script("arguments[0].scrollIntoView();", button)
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(button)).click()
                except Exception as e:
                    print("Could not click on a 'More' button:", e)
                    continue

        time.sleep(10)
        body = self.driver.find_element(By.XPATH, "//div[contains(@class, 'm6QErb') and contains(@class, 'DxyBCb') and contains(@class, 'kA9KIf') and contains(@class, 'dS8AEf')]")
        for _ in range(total_number_of_reviews):
            body.send_keys(Keys.PAGE_DOWN)
            expand_more_buttons(self.driver)
            time.sleep(1)


    def retrieve_google_reviews(self):
        # Assuming driver.page_source contains the HTML source of the page with reviews
        html_content = self.driver.page_source
        response = BeautifulSoup(html_content, 'html.parser')
        reviews = response.find_all('div', class_='jJc9Ad')

        review_data = []
        for review in reviews:
            review_text = "No review text found"
            stars = "No rating found"
            time = "No time found"

            review_text_div = review.find('div', class_='MyEned')
            if review_text_div:
                review_text_span = review_text_div.find('span', class_='wiI7pd')
                if review_text_span:
                    review_text = review_text_span.text

            stars_span = review.find('span', class_='fzvQIb')
            if stars_span:
                stars = stars_span.text[0]

            # time_span = review.find('span', class_='xRkPPb')
            time_span = review.find('span', class_='rsqaWe')
            if time_span:
                time = time_span.text
            else:
                time_span = review.find('span', class_='xRkPPb')
                if time_span:
                    time = time_span.text
             

            review_data.append({'text': review_text, 'stars': stars, 'time': time})

        # Create a DataFrame from the review_data list
        df_reviews = pd.DataFrame(review_data)

        # remove empty reviews
        df_reviews = df_reviews[df_reviews['text'] != "No review text found"]

        self.driver.quit()
        return df_reviews
 
    

    
