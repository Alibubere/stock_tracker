import json
import logging
import time
import os
from datetime import datetime
from src.data_cleaner import clean_stock_data
from src.data_fetcher import fetch_stock


def setup_logging():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "pipeline.log")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
    )
    logging.info("Logging Successfully Initialized")


def save_raw(symbol, data, output_dir="data/raw"):

    if not isinstance(symbol, str) or not symbol.strip():
        logging.error(f"Invalid symbol: {symbol}")

    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join(output_dir, f"raw_data_{symbol}_{timestamp}.json")

    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

        logging.info(f"Raw data saved at {file_path}")

    except Exception as e:
        logging.error(f"Failed to save raw data: {e}")


def save_clean(symbol, df):

    if df is None:
        logging.error(f"DataFrame not found {df}")
        return None

    if not isinstance(symbol, str) or not symbol.strip():
        logging.error(f"Invalid symbol for save clean data: {symbol}")
        return None

    try:
        output_dir = "data/clean"
        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join(output_dir, f"cleaned_data_{symbol}_{timestamp}.csv")

        df.to_csv(file_path, index=False)
        logging.info(f"Cleaned data saved to {file_path}")
        return file_path

    except Exception as e:
        logging.exception("Failed to save cleaned data")
        return None


def main():
    setup_logging()
    symbols = ["AAPL", "TSLA", "GOOGL", "BAC"]
    for symbol in symbols:
        try:
            raw = fetch_stock(symbol)

            if raw is None:
                logging.error(f"Skipping save_raw for {symbol} — empty response.")
                continue

            save_raw(symbol, raw)

            df = clean_stock_data(raw)
            if df is None:
                logging.error(f"Skipping save_clean for {symbol} - empty response")
                continue

            save_clean(symbol, df)

            # Respect API rate limit (5 calls/minute)
            time.sleep(12)

        except Exception as e:
            logging.exception(f"Pipeline error for {symbol}: {e}")


if __name__ == "__main__":
    main()
