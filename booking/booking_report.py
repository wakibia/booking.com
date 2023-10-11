from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time


class BookingReport:
    def __init__(self, driver: WebElement):
        self.driver = driver

    def pull_deal_box_attributes(self):

        all_results = []

        paginations = self.driver.find_elements(By.XPATH, '//ol[@class="ef2dbaeb17"]/li')

        last_page = int(paginations[-1].text.strip())

        current_page = 1

        while True:
            reviews = []
            hotel_names = []
            hotel_prices = []
            hotel_url = []

            hotel_boxes = self.driver.find_elements(By.XPATH, '//div[@class="aca0ade214 aaf30230d9 cd2e7d62b0 b0db0e8ada"]')

            scores_div = self.driver.find_elements(By.XPATH,
                                              '//div[@class="aca0ade214 ebac6e22e9 cd2e7d62b0 a0ff1335a1"]//div[@class="a3b8729ab1 d86cee9b25"]')

            # Find and extract reviews

            # while True:
            # get_reviews()
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
                                                    './/div[@class="c5ca594cb1 f19ed67e4b"]/span').text.strip()
                hotel_prices.append(hotel_price)

                url = deal_box.find_element(By.XPATH, './/h3/a').get_attribute('href')
                hotel_url.append(url)

            current_page += 1
            try:
                next_page =  self.driver.find_element(By.XPATH, '//button[@aria-label="Next page"]')
                next_page.click()
                time.sleep(6)
            except:
                break

            if last_page == current_page:
                break

        # Find and extract reviews

        all_results.append([hotel_names, hotel_prices, reviews, hotel_url])

        return all_results

