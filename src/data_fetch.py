import os 
import logging # Logging is configured in main.py
import requests
from dotenv import load_dotenv
from typing import Optional, Dict

load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_KEY")
API_URL = "https://www.alphavantage.co/query"


if not API_KEY:
    raise ValueError("API Key not found. Add ALPHA_VANTAGE_KEY to .env")


def fetch_stock(symbol: str, api_url: str = API_URL) -> Optional[Dict]:
    """
    Fetch daily stock data for a given symbol using AlphaVantage API.

    Returns:
        dict: Parsed JSON response on success.
        None: If request fails or error occurs.
    """
     
    if not isinstance(symbol, str):
        raise TypeError("symbol must be a string")

    params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": symbol,
    "apikey": API_KEY
    }


    try:
        logging.info(f"Fetching stock data for {symbol}")
        response = requests.get(api_url,params=params,timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e :
        logging.error(f"Error Fetching data: {e}")
        return None
