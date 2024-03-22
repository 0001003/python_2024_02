import yfinance #주식 관련 라이브러리

nvda = yfinance.Ticker("TSLA")
price = nvda.info['currentPrice']
print(price)

from bitcoin_value import currency

# Specify the currency code (e.g., "USD", "EUR")
bitcoin_value = currency("USD")

# Print the Bitcoin value in the specified currency
print(f"1 BTC is equivalent to {bitcoin_value} USD")


import datetime
import time
#
#
# from threading import Timer
#
# print('Code Execution Started')
#
# def display():
#     print(f'1 BTC is equivalent to {bitcoin_value} USD')
#
# t = Timer(60, display)
# t.start()

bitcoinList = []
sec = 0
while sec < 10:
    bitcoinList.append(currency("USD"))
    sec += 1
    time.sleep(1) # 1초 멈춤. 
    print(f"{sec}")
print(bitcoinList)