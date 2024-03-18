from kafka import KafkaProducer
import requests
import json
import time

# API
API_KEY = "your_api"
hours = 1
url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Paris&hours={hours}"

# Kafka Producer Configuration
producer = KafkaProducer(bootstrap_servers='your_bootstrap_server')
# After deploying a Kafka Cluster in Amazon MSK your bootstrap servers can be checked by the following command:
# - "more bootstrap-servers"
# You can choose any of them

# Fetch and publish data to Kafka with certain periodicity
while True:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        producer.send('weather', json.dumps(data).encode('utf-8'))
    else:
        print(f"Failed to fetch data from API (Status Code: {response.status_code})")
    producer.flush()

    # Sleep for 1 hour
    time.sleep(3600)

