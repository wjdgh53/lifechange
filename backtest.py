import pyupbit
import numpy as np

df = pyupbit.get_ohlcv("USDT-BTC", count=28)

df['ma5'] = df['close'].rolling(window=5).mean().shift(1)
df['range'] = (df['high'] - df['low']) * 0.3
df['target'] = df['open'] + df['range'].shift(1)
df['bull'] = df['open'] > df['ma5']

df['ror'] = np.where((df['high'] > df['target']) & df['bull'],
                      df['close'] / df['target'],
                      1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD: ", df['dd'].max())
print("HPR: ", df['hpr'][-2])
df.to_excel("larry_ma.xlsx")

df = pyupbit.get_ohlcv("USDT-BTC")
df['range'] = (df['high'] - df['low']) * 0.3
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.0032
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")