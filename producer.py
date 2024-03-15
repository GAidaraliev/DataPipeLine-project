<<<<<<< HEAD
from kafka import KafkaProducer
=======
from confluent_kafka import Producer
>>>>>>> fdced2daa06117d44a1860b8efcc15d514bb15dc
import requests
import json
import time

# Kafka Producer Configuration
<<<<<<< HEAD
producer = KafkaProducer(bootstrap_servers='b-1.dstimsk.bfn7de.c2.kafka.eu-west-1.amazonaws.com:9092')
# for _ in range(100):
#     producer.send('my-topic', b'some_message_bytes')
=======
producer = Producer({'bootstrap.servers': 'b-1.dstimsk.rhqd8r.c2.kafka.eu-west-1.amazonaws.com:9092'})

>>>>>>> fdced2daa06117d44a1860b8efcc15d514bb15dc
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
        producer.send('my-topic', json.dumps(data).encode('utf-8'))
    else:
        print(f"Failed to fetch data from API (Status Code: {response.status_code})")

    producer.flush()

    # Sleep for 20 seconds
    time.sleep(3600)
