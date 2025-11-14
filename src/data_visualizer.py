import os
import matplotlib.pyplot as plt
import logging


def ensure_chart_dir():
    os.makedirs("charts", exist_ok=True)


def plot_close(df, symbol):

    if df is None:
        logging.error(f"Data frame not found {df}")
        return None

    if not isinstance(symbol, str) or not symbol.strip():
        logging.error(f"Invalid Symbol {symbol}")
        return None

    ensure_chart_dir()

    try:

        plt.figure(figsize=(12, 6))
        plt.plot(df["date"], df["close"], label="Close price")
        plt.title(f"{symbol} Closing Price Trend")
        plt.xlabel("Date")
        plt.ylabel("Close price")
        plt.grid(True)
        plt.legend()

        file_path = f"charts/{symbol}_close_trend.png"
        plt.savefig(file_path)
        plt.close()

        logging.info(f"Closing price plot saved to {file_path}")

        return file_path

    except Exception as e:
        logging.exception(f"Failed to plot close price for {symbol}")
        return None


def plot_moving_averages(df, symbol):

    if df is None:
        logging.error(f"Data frame not found {df}")
        return None

    if not isinstance(symbol, str) or not symbol.strip():
        logging.error(f"Invalid Symbol {symbol}")
        return None

    ensure_chart_dir()

    df = df.sort_values("date", ascending=True)

    df["MA20"] = df["close"].rolling(window=20).mean()

    df["MA50"] = df["close"].rolling(window=50).mean()

    try:
        # ---------Visualization----------
        plt.figure(figsize=(12, 6))

        plt.plot(df["date"], df["close"], label="Close", linewidth=1.5)

        plt.plot(df["date"], df["MA20"], label="20-Day MA", linewidth=1.5)

        plt.plot(df["date"], df["MA50"], label="50-Day MA", linewidth=1.5)

        plt.title(f"{symbol} Moving Averages (20 & 50 Day)")

        plt.xlabel("Date")

        plt.ylabel("Price")

        plt.grid(True)

        plt.legend()

        file_path = f"charts/{symbol}_moving_averages.png"
        plt.savefig(file_path)
        plt.close()

        logging.info(f"Moving price Average saved to : {file_path}")

        return file_path

    except Exception as e:
        logging.exception("Failed to plot Moving Average")
        return None
