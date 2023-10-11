import argparse
import time
import csv
from booking.booking import Booking
from selenium.common.exceptions import StaleElementReferenceException

# Define the sort_dict
sort_dict = [
    "Top picks for long stays",
    "Homes & apartments first",
    "Price (lowest first)",
    "Best reviewed & lowest price",
    "Property rating (high to low)",
    "Property rating (low to high)",
    "Property rating and price",
    "Distance From Downtown",
    "Top Reviewed"
]


def parse_args():
    parser = argparse.ArgumentParser(description="Booking.com Automation Script")
    parser.add_argument('--driver-path', default=r"C:\Users\cmwak\chrome_driver\chromedriver-win64",
                        help="Path to the Chrome WebDriver executable")
    parser.add_argument('--currency', default='USD', help="Currency for booking")
    parser.add_argument('--place', default='Naivasha', help="Destination place")
    parser.add_argument('--check-in-date', default='2023-10-10', help="Check-in date")
    parser.add_argument('--check-out-date', default='2023-11-10', help="Check-out date")
    parser.add_argument('--adults', type=int, default=3, help="Number of adults")
    parser.add_argument('--sort-by', choices=sort_dict, default='Price (lowest first)',
                        help="Sorting option")
    parser.add_argument('--output-csv', default=f'booking_results.csv',
                        help="Output CSV file for results")

    args = parser.parse_args()

    # Construct the default output CSV filename with the place argument
    args.output_csv = f"{args.place}_booking_results.csv"

    return parser.parse_args()


def run_booking_process(driver_path, currency, place, check_in_date, check_out_date, adults, sort_by, output_csv):
    bot = None
    try:
        # Create a list to store all results
        bot = Booking() #driver_path=driver_path
        bot.land_first_page()
        time.sleep(3)
        bot.close_popup()
        bot.change_currency("USD") #currency=currency
        bot.select_place_to_go("Mombasa")
        bot.select_dates(check_in_date='2023-10-10', check_out_date='2023-10-14') #check_in_date=check_in_date, check_out_date=check_out_date
        bot.select_adults(3) #adults
        time.sleep(3)
        bot.click_search()
        time.sleep(3)

        bot.apply_filtrations('Price (lowest first)') #sort_by
        time.sleep(3)

        booking_results = bot.report_results()
        bot.report_results()

        transposed_results = list(map(list, zip(*booking_results)))
        # Write the results to a CSV file
        with open(output_csv, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)

            # Write the header row
            header = ["Hotel Name", "Price", "Rating", "Hotel URL"]
            csvwriter.writerow(header)

            # Write each result as a row in the CSV file
            for result in transposed_results:
                csvwriter.writerow(result)

    except Exception as e:
        if 'in PATH' in str(e):
            print(str(e))
        else:
            raise
    finally:
        if bot is not None:
            bot.quit()



if __name__ == "__main__":
    try:
        args = parse_args()
        run_booking_process(args.driver_path, args.currency, args.place, args.check_in_date, args.check_out_date,
                            args.adults, args.sort_by, args.output_csv)

    except Exception as e:
        print(f'Exception was: {e}')