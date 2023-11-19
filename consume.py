import pprint
import traceback

from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    "stock",
    auto_offset_reset="earliest",
    group_id="my-group-1",
    enable_auto_commit=True,
    value_deserializer=lambda m: loads(m.decode("utf-8")),
    bootstrap_servers="localhost:29092",
)


class TickerStat:
    def __init__(self, ticker):
        self.ticker = ticker
        self.counts = 0
        self.volume = 0.0

    def __str__(self):
        return f"{self.ticker}: {self.counts} occurences; {self.volume} volume"

    def __repr__(self):
        return f"{self.ticker}: {self.counts} occurences; {self.volume} volume"


def update_ticker_stats(ticker_data):
    try:
        for t in ticker_data["data"]:
            if t["s"] not in totals:
                totals[t["s"]] = TickerStat(t["s"])

            ticker_stat = totals[t["s"]]
            ticker_stat.counts += 1
            ticker_stat.volume += t["v"]
    except KeyError:
        print(traceback.format_exc())
        return


pp = pprint.PrettyPrinter(indent=4)
totals = {}


if __name__ == "__main__":
    for m in consumer:
        ticker_data = loads(m.value)
        update_ticker_stats(ticker_data)
        pp.pprint(totals)
