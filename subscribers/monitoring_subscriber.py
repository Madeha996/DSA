import paho.mqtt.client as mqtt
import json

BROKER = "mqtt.eclipseprojects.io"
TOPICS = ["home/#"]  # Subscribe to all home topics
CLIENT_ID = "Full_Monitor_1"

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        print(f"\nTopic: {msg.topic}")
        print("Data:", data)
        
        # Callback functionality based on topic
        if "temperature" in msg.topic:
            temp = data["value"]
            if temp > 25:
                print("ALERT: High temperature detected!")
        
        elif "humidity" in msg.topic:
            humidity = data["value"]
            if humidity > 65:
                print("ALERT: High humidity detected!")
                
        elif "light" in msg.topic:
            print(f"Light state changed to: {data['state']}")
            
    except Exception as e:
        print(f"Error processing message: {e}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, CLIENT_ID)
client.connect(BROKER)
client.subscribe([(topic, 1) for topic in TOPICS])  # QoS=1
client.on_message = on_message

print(f"Starting {CLIENT_ID} monitoring all topics...")
client.loop_forever()