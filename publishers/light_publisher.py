import paho.mqtt.client as mqtt
from random import randint
import time
import json

BROKER = "mqtt.eclipseprojects.io"
TOPICS = {
    "home/livingroom/light": {"states": ["ON", "OFF"], "change_prob": 0.3},
    "home/kitchen/light": {"states": ["ON", "OFF"], "change_prob": 0.4}
}
CLIENT_ID = "Light_Publisher_1"

# Initial states
current_states = {topic: "OFF" for topic in TOPICS}

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, CLIENT_ID)
client.connect(BROKER)

try:
    while True:
        for topic, config in TOPICS.items():
            if uniform(0, 1) < config["change_prob"]:
                current_states[topic] = config["states"][randint(0, 1)]
                payload = json.dumps({
                    "state": current_states[topic],
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                })
                client.publish(topic, payload)
                print(f"Published to {topic}: {current_states[topic]}")
        time.sleep(1)
except KeyboardInterrupt:
    client.disconnect()