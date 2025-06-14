import paho.mqtt.client as mqtt

# دالة تُستدعى عند الاتصال بالوسيط
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("test/topic")  # اشترك في هذا الموضوع

# دالة تُستدعى عند استقبال رسالة
def on_message(client, userdata, msg):
    print(f"Received: {msg.payload.decode()} on topic {msg.topic}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)  # اتصل بالوسيط (افتراضيًا على localhost)
client.loop_forever()  # استمر في الاستماع للرسائل