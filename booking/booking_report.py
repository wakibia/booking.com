from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time


class BookingReport:
    def __init__(self, driver: WebElement):
        self.driver = driver

    def pull_deal_box_attributes(self):
        hotel_boxes = self.driver.find_elements(By.XPATH,
                                                '//div[@class="c82435a4b8 a178069f51 a6ae3c2b40 a18aeea94d d794b7a0f7 f53e278e95 da89aeb942"]')

        scores_div = self.driver.find_elements(By.XPATH,
                                               '//div[@class="aca0ade214 ebac6e22e9 cd2e7d62b0 f920833fe5"]//div[@class]/div[@class="aca0ade214 a5f1aae5b2 cd2e7d62b0"]')

        reviews = []
        hotel_names = []
        hotel_prices = []
        hotel_url = []

        # return [hotel_names, hotel_prices, reviews, hotel_url]

        ## pagination

        # paginations = self.driver.find_elements(By.XPATH, '//ol[@class="ef2dbaeb17"]/li')
        #
        # # pages = [int(pagi.text.strip()) for pagi in paginations if pagi is not "..."]
        # last_page = int(paginations[-1].text.strip())
        #
        # current_page = 1

        all_results = []

        for review_element in scores_div:
            review_text = review_element.text.strip()
            if review_text:
                reviews.append(review_text)
            else:
                reviews.append(None)

        for deal_box in hotel_boxes:
            hotel_name = deal_box.find_element(By.XPATH, './/div[@data-testid="title"]').text.strip()
            hotel_names.append(hotel_name)
            hotel_price = deal_box.find_element(By.XPATH,
                                                './/div/span[@class="f6431b446c fbd1d3018c e729ed5ab6"]').text.strip()
            hotel_prices.append(hotel_price)

            url = deal_box.find_element(By.XPATH, './/h3/a').get_attribute('href')
            hotel_url.append(url)

        # Find and extract reviews

        all_results.append([hotel_names, hotel_prices, reviews, hotel_url])

        # while True:
        #
        #     for review_element in scores_div:
        #         review_text = review_element.text.strip()
        #         if review_text:
        #             reviews.append(review_text)
        #         else:
        #             reviews.append(None)
        #
        #     for deal_box in hotel_boxes:
        #         hotel_name = deal_box.find_element(By.XPATH, './/div[@data-testid="title"]').text.strip()
        #         hotel_names.append(hotel_name)
        #         hotel_price = deal_box.find_element(By.XPATH,
        #                                             './/div/span[@class="f6431b446c fbd1d3018c e729ed5ab6"]').text.strip()
        #         hotel_prices.append(hotel_price)
        #
        #         url = deal_box.find_element(By.XPATH, './/h3/a').get_attribute('href')
        #         hotel_url.append(url)
        #
        #     # Find and extract reviews
        #
        #     all_results.append([hotel_names, hotel_prices, reviews, hotel_url])
        #
        #     current_page += 1
        #     try:
        #         next_page = self.driver.find_element(By.XPATH, '//button[@aria-label="Next page"]')
        #         next_page.click()
        #         time.sleep(5)
        #     except Exception as e:
        #         print(f'This was the error {e}')

            # # Check if we've reached the last page and terminate the loop
            # if last_page == current_page:
            #     break

        return all_results

