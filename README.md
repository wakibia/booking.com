# Booking.com Bot

Get you travel deals using this bot.
The tool applies different filters to as you would intend
It returns the results in a csv file

## Features

- Search booking for different locations
- Control Currency for the price
- Get prices for the different dates
- Filter the deals by rating, get the reviews, Sort Data by the different methods


## How to use

Booking.Com arguments:

*Sensible defauls have been made for these arguments*

| Arguments           | Description                                       | Type   |
|---------------------|---------------------------------------------------|--------|
| \-\-query           | driver-path                                       | string |
| \-\-currency        | Currency for Booking                              | string |
| \-\-place           | Place you will are interested in                  | string |
| \-\-check-in-date   | Expected date you will be checking-in             | string |
| \-\-check-out-daye  | Expected date you will be checking-out            | string |
| \-\-adults          | Number of Adults making the booking               | int    |
| \-\-sort-by         | What variabe do you want to sort the results with | string |
| \-\-output-csv      | Output file - will be a csv                       | string |
| \-h                 | Shows the help                                    | --     |

### Note

You can use only one of the arguments in the following groups
The website is subject to regular changed - It may fail. If it fails start a new issue. I will respond soonest


## Example

Get the booking details for *Mombasa*

```bash
python main.py --driver-path "C:\path\to\chromedriver.exe" --currency USD --place "Mombasa" --check-in-date "2023-10-10" --check-out-date "2023-11-10" --adults 3 --sort-by "Price (lowest first)" --output-csv "booking_results.csv"
```


## Contributions

Feel free to contribute to this project by proposing any change or fixing

### To do

- More control of the Bot
- Code documentation
- General improvements

## Disclaimer

This application is for educational purposes only.

