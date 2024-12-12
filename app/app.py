import argparse
import os
import yfinance as yf
from datetime import datetime

def download_stock_historical_price(ticker, period1, period2, interval):
    try:
        # Validate the date format
        datetime.strptime(period1, '%Y-%m-%d')
        datetime.strptime(period2, '%Y-%m-%d')

        # Download data using yfinance
        data = yf.download(ticker, start=period1, end=period2, interval=interval)
        if data.empty:
            print("No data found for the given inputs. Check the ticker or date range.")
            return

        # Save to CSV
        data_file_name = f'{ticker}_{period1}_{period2}_{interval}.csv'
        data.to_csv(os.path.join(os.getcwd(), data_file_name))
        print(f"File downloaded successfully: {data_file_name}")

    except Exception as e:
        print(f"Error: {e}")

# Add command-line argument parsing
stock_price_parser = argparse.ArgumentParser(
    prog='stock_price_downloader',
    usage='%(prog)s ticker period1 period2 interval',
    description='Download U.S. stock historical price data'
)

stock_price_parser.add_argument('ticker', type=str, help='Ticker name (e.g., TSLA)')
stock_price_parser.add_argument('period1', type=str, help='Start date in yyyy-mm-dd format')
stock_price_parser.add_argument('period2', type=str, help='End date in yyyy-mm-dd format')
stock_price_parser.add_argument('interval', type=str, help='Interval: 1d, 1wk, or 1mo')

args = stock_price_parser.parse_args()

# Call the function with parsed arguments
download_stock_historical_price(args.ticker, args.period1, args.period2, args.interval)