import os
import json
import pandas as pd
import logging
from datetime import datetime
from typing import Optional , Dict


def clean_stock_data(raw_json: Dict) -> Optional[pd.DataFrame]:

    if raw_json is :
        logging.error(f"json file not found:{raw_json}")



