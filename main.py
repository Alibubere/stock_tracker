import os 
import logging
from src.data_fetcher import fetch_stock
import json


def setup_logging():
    log_dir = "logs"
    os.makedirs(log_dir,exist_ok=True)
    log_file=os.path.join(log_dir,"pipeline.log")
    logging.basicConfig(
        level=logging.INFO,
        format= "%(asctime)s -%(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logging.info("Logging Successfully Initialized")


def save_raw(symbol , data,output_dir="data"):
    os.makedirs(output_dir,exist_ok=True)
    file_path = os.path.join(output_dir,f"raw_data_{symbol}.json")

    try:
        with open (file_path,"w") as f:
            json.dump(data,f,indent=4)
            
        logging.info(f"Raw data saved at {file_path}")
    
    except Exception as e:
        logging.error(f"Failed to save raw data: {e}")
       

    

def main():
    setup_logging()
    symbols= ["AAPL", "TSLA", "GOOGL", "BAC"]
    for symbol in symbols:
        raw = fetch_stock(symbol=symbol)
        save_raw(symbol,raw)  
    

if __name__ == "__main__":
    main()