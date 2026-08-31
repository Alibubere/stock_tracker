from data_cleaner import clean_stock_data
import pandas as pd
import pytest
from copy import deepcopy

@pytest.fixture
def valid_response():
       return {
        "Meta Data": {
            "2. Symbol": "AAPL",
        },
        "Time Series (Daily)":{
            "2024-01-02": {
                "1. open": "185.0",
                "2. high": "186.5",
                "3. low": "184.0",
                "4. close": "185.5",
                "5. volume": "1000000"
            }
        }
    }


def test_clean_stock_data_returns_none_for_none_input():
    result = clean_stock_data(None)
    assert result is None

def test_clean_stock_data_returns_valid_dataframe(valid_response):

    result = clean_stock_data(valid_response)

    assert isinstance(result,pd.DataFrame)
    assert len(result) == 1
    assert result["symbol"].iloc[0] == "AAPL"
    assert isinstance(result["close"].iloc[0],float)
    assert isinstance(result["date"].iloc[0],pd.Timestamp)

def test_clean_stock_data_returns_none_for_missing_keys():
    invalid_response = {
         "Meta Data":{
              "2. Symbol" : "AAPL"
         }
    }

    result = clean_stock_data(invalid_response)

    assert result is None


def test_clean_stock_data_returns_none_for_invalid_symbol(valid_response):

    invalid_response = valid_response.copy()
    invalid_response["Meta Data"] = {
         "2. Symbol": ""
    }
    result = clean_stock_data(invalid_response)

    assert result is None

@pytest.mark.parametrize("bad_input", [
    {
        "Note": "Thank you for using Alpha Vantage! Our standard API rate limit..."
    },
    {
        "Error Message": "Invalid API call."
    },
])
def test_clean_stock_data_returns_none_for_api_errors(bad_input):
    result = clean_stock_data(bad_input)

    assert result is None


def test_clean_stock_data_returns_none_for_malformed_row(valid_response):
    invalid_response = deepcopy(valid_response)

    invalid_response["Time Series (Daily)"]["2024-01-02"]["1. open"] = "not_a_number"

    result = clean_stock_data(invalid_response)

    assert result is None