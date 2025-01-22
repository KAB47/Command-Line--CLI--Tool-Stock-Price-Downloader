# Command Line (CLI) Tool - Stock Price Downloader

This script allows you to download historical stock price data for a specified ticker symbol and time range using the [yfinance](https://github.com/ranaroussi/yfinance) library. The data can be saved as a CSV file for further analysis.

## Features

- Fetch historical price data for U.S. stocks.
- Specify a date range and interval for the data.
- Automatically saves the data to a CSV file in the current working directory.

## Prerequisites

Ensure you have the following installed:

- Python 3.6 or later
- Required Python libraries: `argparse`, `yfinance`, and `os`

You can install the required library using pip:

```bash
pip install yfinance
```

`argparse` and the `os` libraries are apart of Python's standard library, so as long as you have Python installed, these libraries very likely do not need installing on your machine.
```

## Usage
1. Download the app project folder
2. Using the terminal or Command Line navigate to the project folder and run the script with the following syntax:

```bash
python script_name.py <ticker> <period1> <period2> <interval>
```

### Positional Arguments

- `ticker`: The stock ticker symbol (e.g., `AAPL`, `TSLA`).
- `period1`: The start date in `yyyy-mm-dd` format.
- `period2`: The end date in `yyyy-mm-dd` format.
- `interval`: The interval for the data. Valid options: `1d`, `1wk`, or `1mo`.

### Example

```bash
python app.py TSLA 2023-01-01 2023-01-31 1d
```

This command will download daily historical prices for Tesla (TSLA) from January 1, 2023, to January 31, 2023, and save them to a CSV file in the current working directory.

## Output

The script will generate a CSV file in the format:

```
<ticker>_<period1>_<period2>_<interval>.csv
```

For example, the output for the example above will be:

```
TSLA_2023-01-01_2023-12-01_1d.csv
```

## Error Handling

- If no data is found for the given ticker or date range, the script will print an appropriate error message.
- If an invalid input is provided (e.g., incorrect date format), an error message will be displayed.

## Notes

- Ensure that the ticker symbol is correct and the stock is listed on an exchange supported by Yahoo Finance.
- Make sure the date range and intervals are valid and that the system has write permissions to save files in the working directory.

