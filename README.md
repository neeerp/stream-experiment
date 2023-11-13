# Streams

Simple data streaming example with Kafka to ingest from the Finnhub websocket
API.

## Getting Started
First, get an API Key by registering with finnhub.io.

Then, start up Kafka with docker-compose:

```sh
docker-compose up -d
```

Create your venv and install dependencies:
```sh
python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
```

Run the ingestion script in one terminal window:
```sh
python ./ingest.py
```

Run the consumer script in the other terminal window (make sure to remember to activate the venv!):
```sh
python ./consume.py
```

