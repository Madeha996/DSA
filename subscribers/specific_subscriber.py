import paho.mqtt.client as mqtt
import json

BROKER = "mqtt.eclipseprojects.io"
TOPICS = [
    ("home/+/temperature", 1),  # + is single-level wildcard
    ("home/kitchen/+", 1)
]
CLIENT_ID = "Specific_Monitor_1"

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        print(f"\nReceived from {msg.topic}:")
        
        # Different processing for different topics
        if "temperature" in msg.topic:
            print(f"Temperature: {data['value']}{data['unit']}")
            if "livingroom" in msg.topic:
                print("(Living Room)")
            elif "kitchen" in msg.topic:
                print("(Kitchen)")
                
        elif "light" in msg.topic:
            print(f"Light is now {data['state']}")
            
    except Exception as e:
        print(f"Error processing message: {e}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, CLIENT_ID)
client.connect(BROKER)
client.subscribe(TOPICS)
client.on_message = on_message

print(f"Starting {CLIENT_ID} monitoring specific topics...")
client.loop_forever()