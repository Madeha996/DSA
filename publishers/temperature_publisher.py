import paho.mqtt.client as mqtt
from random import uniform
import time
import json

BROKER = "mqtt.eclipseprojects.io"
TOPICS = {
    "home/livingroom/temperature": {"unit": "C", "range": (20.0, 25.0)},
    "home/kitchen/temperature": {"unit": "C", "range": (18.0, 28.0)}
}
CLIENT_ID = "Temperature_Publisher_1"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, CLIENT_ID)
client.connect(BROKER)

try:
    while True:
        for topic, config in TOPICS.items():
            temp = round(uniform(*config["range"]), 2)
            payload = json.dumps({
                "value": temp,
                "unit": config["unit"],
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            })
            client.publish(topic, payload)
            print(f"Published to {topic}: {temp}{config['unit']}")
        time.sleep(2)
except KeyboardInterrupt:
    client.disconnect()