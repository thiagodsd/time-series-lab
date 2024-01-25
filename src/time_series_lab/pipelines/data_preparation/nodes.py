"""
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.19.2
"""
import datetime
import numpy as np
import pandas as pd

from typing import NoReturn, Dict

# import pandas_datareader as pdr
from yahoofinancials import YahooFinancials


def get_history_data(quote_options: Dict) -> pd.DataFrame:
    """
    get_history_data
    """
    ticker_quote = quote_options["ticker"]
    start_date = datetime.datetime.strptime(str(quote_options["ini"]), "%Y%m%d").strftime('%Y-%m-%d')
    if len(quote_options["fim"]) == 8:  # yyyymmdd
        end_date = datetime.datetime.strptime(str(quote_options["fim"]), "%Y%m%d").strftime('%Y-%m-%d')
    else:
        end_date = datetime.datetime.now().strftime('%Y-%m-%d')

    return pd.DataFrame.from_dict(
        YahooFinancials(ticker_quote).get_historical_price_data(
            start_date, end_date, 'daily'
        )[ticker_quote]["prices"]
    )
