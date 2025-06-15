import paho.mqtt.client as mqtt
from random import uniform
import time
import json

BROKER = "mqtt.eclipseprojects.io"
TOPICS = {
    "home/livingroom/humidity": {"unit": "%", "range": (30.0, 60.0)},
    "home/kitchen/humidity": {"unit": "%", "range": (40.0, 70.0)}
}
CLIENT_ID = "Humidity_Publisher_1"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, CLIENT_ID)
client.connect(BROKER)

try:
    while True:
        for topic, config in TOPICS.items():
            humidity = round(uniform(*config["range"]), 2)
            payload = json.dumps({
                "value": humidity,
                "unit": config["unit"],
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            })
            client.publish(topic, payload)
            print(f"Published to {topic}: {humidity}{config['unit']}")
        time.sleep(3)
except KeyboardInterrupt:
    client.disconnect()