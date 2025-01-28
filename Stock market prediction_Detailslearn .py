#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd

# Set your API key here
API_KEY = 'gw4rgOqygjpO_qN_FmSkBjH_PgtYsrtp'

# List of stock symbols (e.g., 5 stocks)
symbols = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'TSLA']

# Define the date range for the data
start_date = '2022-01-01'
end_date = '2022-12-31'

# Loop through each stock symbol and download data
for symbol in symbols:
    print(f"Fetching data for {symbol}...")

    # URL for daily historical data
    url = f'https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/{start_date}/{end_date}?adjusted=true&sort=asc&limit=50000&apiKey={API_KEY}'

    # Make the request to Polygon.io
    response = requests.get(url)
    data = response.json()

    # Check if data is available
    if 'results' in data:
        # Convert to pandas DataFrame
        df = pd.DataFrame(data['results'])
        # Convert the timestamp to a readable date
        df['t'] = pd.to_datetime(df['t'], unit='ms')
        df.set_index('t', inplace=True)

        # Save the data to a CSV file
        file_name = f'{symbol}_historical_data.csv'
        df.to_csv(file_name)
        print(f"Data for {symbol} saved to {file_name}")
    else:
        print(f"No data found for {symbol}")


# In[ ]:





# In[ ]:




