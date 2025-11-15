import logging
import pandas as pd
import os
import matplotlib.pyplot as plt
from prophet import Prophet
from prophet.plot import plot_plotly

def prepare_for_prophet(df):

    if df is None:
        logging.error("Input DataFrame is None — cannot prepare for Prophet.")
        return None

    if "date" not in df.columns or "close" not in df.columns:
        logging.error("Dataframe missing required columns ['date','close']")
        return None

    try:

        df = df.sort_values("date", ascending=True)

        prophet_df = df[["date", "close"]]

        prophet_df = prophet_df.rename(columns={"date": "ds", "close": "y"})

        prophet_df["y"] = prophet_df["y"].astype(float)

        prophet_df["ds"] = pd.to_datetime(prophet_df["ds"])

        prophet_df = prophet_df.dropna(subset=["ds", "y"])

        prophet_df.reset_index(drop=True, inplace=True)

        return prophet_df

    except Exception as e:
        logging.exception(f"Failed to prepare DataFrame for prophet: {e}")
        return None


def train_prophet_model(prophet_df):

    if prophet_df is None:
        logging.error("Prophet DataFrame is NONE - cannot train prophet model")
        return None

    if "ds" not in prophet_df.columns or "y" not in prophet_df.columns:
        logging.error("Prophet DF missing required columns ['ds','y']")
        return None
    try:
        model = Prophet(
            daily_seasonality=True, weekly_seasonality=True, yearly_seasonality=False
        )

        logging.info(f"Training Prophet model on {len(prophet_df)} rows")

        model.fit(prophet_df)

        logging.info("Model trained Successfully")

        return model

    except Exception as e:
        logging.exception(f"Failed to train Prophet model : {e}")
        return None

def make_forecast(model , periods: int =30):

    if model is None :
        logging.error(f"Invalid model {model}")
        return None
    
    logging.info(f"Generating {periods}-day forecast...")

    try:

        future= model.make_future_dataframe(periods=periods) 

        forecast= model.predict(future)

        forecast= forecast[["ds","yhat","yhat_lower","yhat_upper"]]

        logging.info(f"Forecast generated successully with {len(forecast)} rows.")

        return forecast


    except Exception as e:
        logging.exception(f"Failed to forecast using prophet model :{e}")
        return None


def plot_prophet_forecast(symbol,model,forecast):

    if not isinstance(symbol,str) or not symbol.strip():
        logging.error(f"Invalid symbol {symbol}")
        return None
    
    if model is None :
        logging.error(f"Invalid model {model}")
        return None
    
    if forecast is None:
        logging.error(f"Invalid Forecast {forecast}")
        return None
    
    os.makedirs("charts",exist_ok=True) # Ensures Charts directory exist 

    try:

        file_path = f"charts/{symbol}_prophet_forecast.png"
        fig =model.plot(forecast)

        fig.savefig(file_path)

        plt.close(fig)

        logging.info(f"Prophet forecast plot saved to : {file_path}")

        return file_path
    
    except Exception:
        logging.exception("Failed to plot Prophet forecast")
        return None






