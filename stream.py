import os

import dotenv
import websocket

# Using dotenv, load the api secret key from the .env file
dotenv.load_dotenv()
API_KEY = os.getenv("FINN_HUB_API_KEY")


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    # ws.send('{"type":"subscribe","symbol":"AAPL"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')
    # ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    # ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')


if __name__ == "__main__":
    ws = websocket.WebSocketApp(
        f"wss://ws.finnhub.io?token={API_KEY}",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    ws.on_open = on_open
    ws.run_forever()
