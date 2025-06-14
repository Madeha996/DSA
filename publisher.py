import paho.mqtt.client as mqtt
import time

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883, 60)  # اتصل بالوسيط

for i in range(5):  # أرسل 5 رسائل تجريبية
    message = f"Hello MQTT! Message #{i+1}"
    client.publish("test/topic", message)  # أرسل الرسالة إلى الموضوع المحدد
    print(f"Sent: {message}")
    time.sleep(1)  # انتظر ثانية بين كل رسالة

client.disconnect()  # افصل بعد الإرسال