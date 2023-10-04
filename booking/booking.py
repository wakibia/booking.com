import booking.constants as const
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Users\cmwak\chrome_driver\chromedriver-win64"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')

        # Initialize the driver directly
        self.driver = webdriver.Chrome(options=options)

        # Call the superclass constructor
        super().__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def close_popup(self):
        popup_button = self.find_element(By.XPATH, '//button[@aria-label="Dismiss sign-in info."]')
        popup_button.click()

    def change_currency(self, currency='USD'):
        currency_element = self.find_element(By.XPATH, '(//button[@aria-expanded="false"])[1]')
        currency_element.click()

        currencies = self.find_elements(By.XPATH, '//li[@class="b817090550 c44c37515e"]//span[@class="cf67405157"]/div')
        all_currencies = [cur.text.strip() for cur in currencies]

        selected_currency_element = self.find_element(By.XPATH, '//button[@data-testid="selection-item"]')

        if currency.upper() in all_currencies:
            selected_currency_element.click()
        else:
            print('Enter A Valid Currency Symbol')

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.XPATH, '//input[@name="ss"]')
        search_field.clear()
        search_field.send_keys(place_to_go)

    def select_dates(self, check_in_date, check_out_date):

        check_in_element = self.find_element(By.XPATH, '//button[@data-testid="date-display-field-start"]')

        check_out_element = self.find_element(By.XPATH, '//button[@data-testid="date-display-field-end"]')
        check_in_element.click()

        # Define XPaths for the date cells
        check_in_date_xpath = f'//span[@data-date="{check_in_date}"]'
        check_out_date_xpath = f'//span[@data-date="{check_out_date}"]'

        # WebDriverWait(self, 10).until(EC.visibility_of_element_located((By.XPATH, check_in_date_xpath)))

        check_in_date_element = self.find_element(By.XPATH, check_in_date_xpath)
        check_in_date_element.click()
        time.sleep(2)

        # Click on the check-out date
        check_out_date_element = self.find_element(By.XPATH, check_out_date_xpath)
        check_out_date_element.click()
        time.sleep(2)

    def select_adults(self, count=1):
        selection_element = self.find_element(By.XPATH, '//button[@data-testid="occupancy-config"]')
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element(By.XPATH,
                                                        '(//div[@class="bfb38641b0"]//button[@tabindex="-1"])[1]')
            decrease_adults_element.click()
            adults_value_element = self.find_element(By.XPATH, '(//span[@class="d723d73d5f"])[1]')
            adults_value = adults_value_element.text.strip()

            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element(By.XPATH, '(//div[@class="bfb38641b0"]//button[@tabindex="-1"])[2]')

        for _ in range(count - 1):
            increase_button_element.click()

        occupancy_done = self.find_element(By.XPATH,
                                           '//button[@class="a83ed08757 c21c56c305 bf0537ecb5 ab98298258 d2529514af af7297d90d d285d0ebe9"]')
        occupancy_done.click()

    def click_search(self):
        search_button = self.find_element(By.XPATH, '//button[@type="submit"]')
        search_button.click()

    def apply_filtrations(self, sort_by):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(3)
        time.sleep(5)

        filtration.sort_price_lowest_first(sort_by)

    def report_results(self):
        report = BookingReport(driver=self)
        hotl_rslt = report.pull_deal_box_attributes()
        print(hotl_rslt)


    def quit(self):
        self.driver.quit()
