import logging
import pandas as pd
from prophet import Prophet


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
        logging.exception("Failed to prepare Dataframe for prophet.")
        return None


def train_prophet_model(prophet_df):

    if prophet_df is None:
        logging.error("Prophet data frame is NONE - cannot train prophet model")
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
        logging.exception("Failed to train Prophet model")
        return None
