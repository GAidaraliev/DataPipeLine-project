#from confluent_kafka import Producer
import requests
import json
import time

# Kafka Producer Configuration
producer = Producer({'bootstrap.servers': 'b-1.dstimsk.rhqd8r.c2.kafka.eu-west-1.amazonaws.com:9092'})

# API endpoints
API_KEY = "a0bd5e5a4d9a4c4098f143006241003"
hours = 1
url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Paris&hours={hours}"

# Periodically fetch and publish data to Kafka
while True:
    # Fetch data from API
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        producer.produce(topic='my-topic', key="dsti".encode('utf-8'), value=json.dumps(data))
    else:
        print(f"Failed to fetch data from API (Status Code: {response.status_code})")

    producer.flush()

    # Sleep for 20 seconds
    time.sleep(3600)
