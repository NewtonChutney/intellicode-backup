from config import *
from contract import *
import time

def test():
    barset = api.get_barset(company, 'minute',limit = rsi_timeframe)
    aapl_bars = barset[company]    
    data =[]
    for i in range(rsi_timeframe):
            min_close = aapl_bars[i].c
            data.append(min_close)
    print(f"The data is {data}")     
    
test()