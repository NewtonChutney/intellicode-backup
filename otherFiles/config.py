import alpaca_trade_api as tradeapi
from bitarray import test
global api
def alpaca_config(self):      
    self.api = tradeapi.REST('PKV1BGF3JLNW4PW12YDN','v422pqikm17DDHNkhDMVYNtk6rExbCwkD4xRUVnh',"https://paper-api.alpaca.markets","v2")
    return self.api

def ib_config(self):
    print("Null")          




    
    
