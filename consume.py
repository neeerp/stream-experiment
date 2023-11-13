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


if __name__ == "__main__":
    for m in consumer:
        print(m.value)
