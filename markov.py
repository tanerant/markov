import yfinance as yf 
import pandas as pd 
import numpy as np 

ticker = "TSLA"
data = yf.download(ticker,start="2010-01-01",end="2024-01-21")

data['daily_return'] = data['Adj Close'].pct_change()
data['state'] = np.where(data['daily_return']>=0, "up","down")
data.head()

up_counts = len(data['state']== "up")
down_counts = len(data['state']== "down")
up_to_up = len(data[(data["state"] == "up") & (data["state"].shift(-1) == "up")]) / len(data.query('state=="up"'))
down_to_down = len(data[ (data["state"] == "down") & (data["state"].shift(-1) == "down")])/ len(data.query('state=="down"'))
down_to_up = len(data[ (data["state"] == "down") & (data["state"].shift(-1) == "up")])/ len(data.query('state=="up"'))
up_to_down = len(data[ (data["state"] == "up") & (data["state"].shift(-1) == "down")])/ len(data.query('state=="down"'))
transition_matrix = pd.DataFrame({
    "up" : [up_to_up,down_to_up],
    "down" : [down_to_down,up_to_down]
}, index=["up","down"])

print(transition_matrix)
