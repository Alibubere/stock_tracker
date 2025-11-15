import json
import logging
import time
import os
from datetime import datetime
from src.data_cleaner import clean_stock_data
from src.data_fetcher import fetch_stock
from src.data_visualizer import plot_moving_averages, plot_close
from src.prophet_model import (
    train_prophet_model,
    prepare_for_prophet,
    plot_prophet_forecast,
    make_forecast,
)


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


def is_valid_symbol(symbol):

    return isinstance(symbol, str) and symbol.strip()


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def save_raw(symbol, data, output_dir="data/raw"):

    if not is_valid_symbol:
        logging.error(f"Invalid symbol: {symbol}")

    os.makedirs(output_dir, exist_ok=True)
    timestamp = get_timestamp()
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

    if not is_valid_symbol:
        logging.error(f"Invalid symbol for save clean data: {symbol}")
        return None

    try:
        output_dir = "data/clean"
        os.makedirs(output_dir, exist_ok=True)
        timestamp = get_timestamp()
        file_path = os.path.join(output_dir, f"cleaned_data_{symbol}_{timestamp}.csv")

        df.to_csv(file_path, index=False)
        logging.info(f"Cleaned data saved to {file_path}")
        return file_path

    except Exception:
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
                logging.error(f"Skipping save_clean for {symbol} - cleaning failed")
                continue

            save_clean(symbol, df)

            plot_close(df, symbol)
            plot_moving_averages(df, symbol)

            prophet_df = prepare_for_prophet(df)

            if prophet_df is None:
                logging.error(
                    f"Skipping prophet steps for {symbol} - Preparation failed."
                )
                continue

            model = train_prophet_model(prophet_df)

            if model is None:
                logging.error(
                    f"Skipping Forecast for {symbol} - model training failed."
                )
                continue

            forecast = make_forecast(model, periods=30)

            if forecast is None:
                logging.error(f"Skipping Plotting for {symbol} - forecasting failed.")
                continue

            timestamp = get_timestamp()
            forecast_path = f"data/forecast/forecast_{symbol}_{timestamp}.csv"
            os.makedirs("data/forecast", exist_ok=True)
            forecast.to_csv(forecast_path, index=False)

            logging.info(f"Forecast saved at: {forecast_path}")

            plot_prophet_forecast(symbol, model, forecast)

            logging.info(f"Prophet forecast plot generated for {symbol}")

            time.sleep(15)  # Respect API rate limit (5 calls/minute)

        except Exception:
            logging.exception(f"Pipeline error for {symbol}")


if __name__ == "__main__":
    main()
