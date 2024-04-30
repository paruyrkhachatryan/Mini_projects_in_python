import requests
import time
def get_crypto_stats():
    """
    Fetches cryptocurrency statistics from CoinGecko API and prints them.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 11,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  
        data = response.json()

        for crypto in data:
            name = crypto['name']
            symbol = crypto['symbol']
            price = crypto['current_price']
            market_cap = crypto['market_cap']
            total_volume = crypto['total_volume']
            price_change_24h = crypto['price_change_24h']

            print("Name:", name)
            print("Symbol:", symbol)
            print("Current Price: $", price)
            print("Market Cap $:", market_cap)
            print("Total Volume $:", total_volume)
            print("Price Change for 24 hours: $", price_change_24h)
            print("-----------------------------")

    except requests.RequestException as e:
        print("Error fetching data:", e)


print("********* Crypto Statistics *********")
get_crypto_stats()

# while True:
#     print("********* Crypto Statistics *********")
#     get_crypto_stats()
#     time.sleep(5)




