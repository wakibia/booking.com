import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # you will pass a tuple of the number of stars to control with
    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(
            By.XPATH,
            '//div[@data-filters-group="class"]'
        )

        # get all the child elements of the above ID
        star_child_elements = star_filtration_box.find_elements(
            By.XPATH,
            './/div[@class ="aca0ade214 aaf30230d9 c2931f4182 e7d9f93f4d d1764ea78b"]/div'
        )

        for star_value in star_values:
            for star_element in star_child_elements:
                if star_element.text.strip() == f'{star_value} stars':
                    star_element.click()

    def sort_price_lowest_first(self, sort_by=None):
        sort_button = self.driver.find_element(
            By.XPATH,
            '//button[@class="a83ed08757 faefc93c6f b94d37c0c4"]'
        )
        sort_button.click()
        time.sleep(3)

        ## sorting variables
        sort_dict = {"popularity": "Top picks for long stays",
                     "upsort_bh": "Homes & apartments first",
                     "price": "Price (lowest first)",
                     "review_score_and_price": "Best reviewed & lowest price",
                     "class": "Property rating (high to low)",
                     "class_asc": "Property rating (low to high)",
                     "class_and_price": "Property rating and price",
                     "distance_from_search": "Distance From Downtown",
                     "bayesian_review_score": "Top Reviewed"}

        if sort_by is not None:
            sort_button_select = None
            for key, value in sort_dict.items():
                if value == sort_by:
                    sort_button_select = self.driver.find_element(By.XPATH, f"//button[@data-id='{key}']")
                    break
            else:
                print('Please Provide one of the Methods for sorting')

            if sort_button_select is not None:
                sort_button_select.click()
        else:
            print('Please provide a value for sort_by')

