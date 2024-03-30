import time
import pyupbit
import datetime
import numpy as np

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_ma15(ticker):
    """15일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
print("autotrade start")
df = pyupbit.get_ohlcv("USDT-BTC", count =7)
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
df['Target Price'] = get_target_price("USDT-BTC", 0.5)
target_price = get_target_price("USDT-BTC", 0.5)
ma15 = get_ma15("USDT-BTC")
current_price = get_current_price("USDT-BTC")
df['MA15'] = get_ma15("USDT-BTC")
df['Current Price'] =  get_current_price("USDT-BTC")
df['Buy?'] = (target_price < current_price and ma15 < current_price)
df.to_excel("dd.xlsx")
# while True:
#     try:
#         now = datetime.datetime.now()
#         start_time = get_start_time("USDT-BTC")
#         end_time = start_time + datetime.timedelta(days=1)

#         if start_time < now < end_time - datetime.timedelta(seconds=10):
#             target_price = get_target_price("USDT-BTC", 0.5)
#             ma15 = get_ma15("USDT-BTC")
#             current_price = get_current_price("USDT-BTC")
#             if target_price < current_price and ma15 < current_price:
#                 krw = get_balance("USDT-BTC")
#                 #if krw > 5000:
#                 print("buy it!!")
#                     #upbit.buy_market_order("USDT-BTC", krw*0.9995)
#         #else:
#            # btc = get_balance("BTC")
#             #if btc > 0.00008:
#             #print("sell it")
#                # upbit.sell_market_order("USDT-BTC", btc*0.9995)
#         time.sleep(1)
#     except Exception as e:
#         print(e)
#         time.sleep(1)