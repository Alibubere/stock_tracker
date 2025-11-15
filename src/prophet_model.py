import logging
import pandas as pd

def prepare_for_prophet(df):

    if df is None:
        logging.error("Input DataFrame is None — cannot prepare for Prophet.")
        return None
     
    if "date" not in df.columns or "close" not in df.columns:
        logging.error("Dataframe missing required columns ['date','close']")
        return None
    
    try:

        df = df.sort_values("date",ascending= True)

        prophet_df = df[["date","close"]]

        prophet_df=prophet_df.rename(columns={"date":"ds" , "close":"y"}) 

        prophet_df["y"]=prophet_df["y"].astype(float)

        prophet_df["ds"]=pd.to_datetime(prophet_df["ds"])

        return prophet_df

    except Exception as e:
        logging.exception("Failed to prepare Dataframe for prophet.")
        return None



