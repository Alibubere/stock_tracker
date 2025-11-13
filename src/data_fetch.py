import os 
import logging
import requests
from dotenv import load_dotenv
import yaml

load_dotenv()

API_key = os.getenv("ALPHA_VANTAGE_KEY")

if API_key is None:
    logging.error("API Key not found. Check your .env file")



def load_config(config_dir="configs/config.yaml"):
    try:
        with open (config_dir,"r") as f:
            config= yaml.safe_load(f)
            return config
        
    except Exception as e :
        logging.error(f"Error loading config {e}")
        raise


def fetch_multiple_stock_data(symbol_list,api_url="https://www.alphavantage.co/query",params=None):
    try:
        logging.info(f"Fetching data from url {api_url}....")
        response = requests.get(api_url,params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e :
        logging.error(f"Error Fetching data: {e}")
        return None
