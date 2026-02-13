from binance.client import Client

def get_client():
    api_key = "PASTE_YOUR_TESTNET_API_KEY_HERE"
    api_secret = "PASTE_YOUR_TESTNET_SECRET_HERE"

    client = Client(api_key, api_secret)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client
