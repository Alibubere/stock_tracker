import os 
import logging
import requests
from dotenv import load_dotenv
import yaml
from datetime import datetime
import json

load_dotenv()

API_key = os.getenv("ALPHA_VANTAGE_KEY")

if API_key is None:
    logging.error("API Key not found. Check your .env file")


def setup_logging():
    log_dir = "logs"
    os.makedirs(log_dir,exist_ok=True)
    log_file=os.path.join(log_dir,"tracker.log")
    logging.basicConfig(
        level=logging.INFO,
        format= "%(asctime)s -%(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logging.info("Logging Successfully Initialized")

def load_config(config_dir="configs/config.yaml"):
    try:
        with open (config_dir,"r") as f:
            config= yaml.safe_load(f)
            return config
        
    except Exception as e :
        logging.error(f"Error loading config {e}")
        raise


def fetch_stock(symbol: str,url = "https://www.alphavantage.co/query"):
    
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    }
    try:
        logging.info(f"Fetching data from url {api_url}....")
        response = requests.get(api_url,params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e :
        logging.error(f"Error Fetching data: {e}")
        return None

def main():

    setup_logging()

    config=load_config()
    api_url =config.get("api_url")
    data= fetch_stock(symbol="BAC",url=api_url)

    if data:
        timestamp= datetime.now().strftime("%Y-%m-%d_%H-%M")
        raw_data_path= f"data/raw_data_{timestamp}.json"

        with open(raw_data_path,"w") as f:
            json.dump(data,f,indent=4)
        
        logging.info(f"Data saved successfully at {raw_data_path} ")
    
    else:
        logging.warning("No data fetch")


if __name__ == "__main__":
    main()