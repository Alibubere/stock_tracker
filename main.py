import os 
import logging
from src.data_fetch import load_config , fetch_stock
from datetime import datetime
import json


def setup_logging():
    log_dir = "logs"
    os.makedirs(log_dir,exist_ok=True)
    log_file=os.path.join(log_dir,"Pipeline.log")
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