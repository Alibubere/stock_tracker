import pandas as pd
import logging
from typing import Optional, Dict


def clean_stock_data(raw_json: Dict) -> Optional[pd.DataFrame]:
    """
    Convert raw AlphaVantage daily Json -> cleaned Dataframe.

    Input (raw_json):expected top level Keys
    - "Meta Data" containing "2. Symbol"
    - "Time Series (Daily)" containing date -> OHLCV dicts

    Returns:
      pd.DataFrame with columns: ['date','symbol','open','high','low','close','volume']
      or None on failure (and logs reason).
    """

    if raw_json is None:
        logging.error(f"json file not found:{raw_json}")
        return None

    if "Note" in raw_json or "Error Message" in raw_json:
        logging.error("API returned an error or rate limit message.")
        return None

    if "Meta Data" not in raw_json or "Time Series (Daily)" not in raw_json:
        logging.error("Invalid API response — missing required keys.")
        return None

    meta = raw_json.get("Meta Data")
    ts = raw_json.get("Time Series (Daily)")

    if not meta or not ts:
        logging.error(
            "Invalid API response — missing 'Meta Data' or 'Time Series (Daily)'"
        )
        return None

    symbol = meta.get("2. symbol") or meta.get("2. Symbol")

    if not isinstance(symbol, str) or not symbol.strip():
        logging.error(f"Invalid symbol: {symbol}")
        return None

    try:
        rows = []

        for date, values in ts.items():
            row = {
                "date": date,
                "symbol": symbol,
                "open": float(values["1. open"]),
                "high": float(values["2. high"]),
                "low": float(values["3. low"]),
                "close": float(values["4. close"]),
                "volume": int(values["5. volume"]),
            }
            rows.append(row)

        df = pd.DataFrame(rows)

        df["date"] = pd.to_datetime(df["date"])

        df.sort_values("date", ascending=False, inplace=True)

        logging.info(f"Cleaned {len(df)} rows for {symbol}")

        return df

    except Exception as e:
        logging.exception(f"Failed to clean the data {e}")
        return None
