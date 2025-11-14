import os 
import matplotlib.pyplot as plt 
import logging

def ensure_chart_dir():
    os.makedirs("charts", exist_ok=True)


def plot_close(df,symbol):
    
    if df is None:
        logging.error(f"Data frame not found {df}") 
        return None

    if not isinstance(symbol,str) or not symbol.strip():
        logging.error(f"Invalid Symbol {symbol}")
        return None
    
    ensure_chart_dir()

    try:

        plt.figure(figsize=(12,6))
        plt.plot(df["date"],df["close"],label="Close price")
        plt.title(f"{symbol} Closing Price Trend")
        plt.xlabel("Date")
        plt.ylabel("Close price")
        plt.grid(True)
        plt.legend()

        file_path= f"charts/{symbol}_close_trend.png"
        plt.savefig(file_path)
        plt.close()

        logging.info(f"Closing price plot saved to {file_path}")

        return file_path
    
    except Exception as e :
        logging.exception(f"Failed to plot close price for {symbol}")
        return None 

