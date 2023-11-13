import os

import dotenv
import websocket
from kafka import KafkaProducer
from json import dumps

# Using dotenv, load the api secret key from the .env file
dotenv.load_dotenv()
API_KEY = os.getenv("FINN_HUB_API_KEY")

producer = KafkaProducer(
    value_serializer=lambda m: dumps(m).encode("utf-8"),
    bootstrap_servers=["localhost:29092"],
)

CRYPTO_EXCHANGES = [
    "KRAKEN",
    "HITBTC",
    "COINBASE",
    "GEMINI",
    "POLONIEX",
    "Binance",
    "ZB",
    "BITTREX",
    "KUCOIN",
    "OKEX",
    "BITFINEX",
    "HUOBI",
]


def on_message(ws, message):
    producer.send("stock", value=message)
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws, status, close_msg):
    print(f"### closed: status {status} ###")
    print(close_msg)


def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"AAPL"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:ETHUSDT"}')
    ws.send('{"type":"subscribe","symbol":"COINBASE:BTC-USD"}')
    ws.send('{"type":"subscribe","symbol":"COINBASE:ETH-USD"}')


if __name__ == "__main__":
    ws = websocket.WebSocketApp(
        f"wss://ws.finnhub.io?token={API_KEY}",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    ws.on_open = on_open
    ws.run_forever()
