import json
import logging
import os
from datetime import datetime

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

    if symbol == "" or symbol == 123 or symbol == None:
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


def main():
    setup_logging()
    symbols = ["AAPL", "TSLA", "GOOGL", "BAC"]
    for symbol in symbols:
        try:
            raw = fetch_stock(symbol=symbol)
            if raw is None:
                logging.error(f"Skipping save_raw for {symbol} — empty response.")
                continue
            save_raw(symbol, raw)
        except Exception as e:
            logging.error(f"Pipeline error for {symbol}: {e}")


if __name__ == "__main__":
    main()
