import os
import time
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

def get_client():

    client = Client(API_KEY, API_SECRET)

    # connect to testnet
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    # fix timestamp error
    server_time = client.get_server_time()
    client.TIME_OFFSET = server_time['serverTime'] - int(time.time()*1000)

    return client