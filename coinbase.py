from coinbase_advanced_trader.config import set_api_credentials

# Set your API key and secret
API_KEY = "NEWMIJbWafdauZkQ"
API_SECRET = "zxKLbe6b6FBy3I8cUAkuuDmugiV5490j"

# Set the API credentials once, and it updates the CBAuth singleton instance
set_api_credentials(API_KEY, API_SECRET)
from coinbase_advanced_trader.strategies.limit_order_strategies import fiat_limit_buy, fiat_limit_sell

# Define the trading parameters
product_id = "BTC-USD"  # Replace with your desired trading pair
usd_size = 20  # Replace with your desired USD amount to spend``

# Perform a limit buy
limit_buy_order = fiat_limit_buy(product_id, usd_size) 
market_order = fiat_market_buy(product_id,usd_size)