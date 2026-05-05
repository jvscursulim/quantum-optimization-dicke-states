# Imports
import time

import numpy as np
import pandas as pd
import yfinance as yf

from tqdm import tqdm

# 
print("Loading SP500 companies tickers.")
df = pd.read_csv(filepath_or_buffer="../datasets/sp500_companies.csv")
tickers_sp500 = df.Symbol.to_list()
tickers_batches = np.array_split(tickers_sp500, 10)

# 
print("Downloading and saving assets data.")
for idx, tickers in tqdm(enumerate(tickers_batches)):
    assets_data = yf.download(tickers=list(tickers), period="1y", progress=False)
    assets_close_price = assets_data.Close
    assets_close_price.to_csv(f"../datasets/assets_close_price_batch_{idx}.csv")
    time.sleep(1)
