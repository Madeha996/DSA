1. تثبيت المتطلبات الأساسية
   تثبيت Mosquitto Broker (خادم MQTT):

bash
sudo apt update
sudo apt install mosquitto mosquitto-clients
sudo systemctl start mosquitto # تشغيل الخادم
تثبيت Python وبيئة التطوير:

bash
sudo apt install python3 python3-venv python3-pip 2. إعداد المشروع
إنشاء مجلد المشروع:

bash
mkdir ~/mqtt_project && cd ~/mqtt_project
إنشاء بيئة افتراضية لعزل المكتبات:

bash
python3 -m venv myenv
source myenv/bin/activate # تفعيل البيئة
(لإيقاف البيئة لاحقًا: deactivate)

3. تثبيت مكتبة Paho-MQTT
   bash
   pip install paho-mqtt
4. إنشاء ملفات المشروع
   ملف المشترك (subscriber.py):

python
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
print(f"Connected with code {rc}")
client.subscribe("test/topic")

def on_message(client, userdata, msg):
print(f"Received: {msg.payload.decode()} on {msg.topic}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()
ملف الناشر (publisher.py):

python
import paho.mqtt.client as mqtt
import time

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883, 60)

for i in range(5):
message = f"Hello MQTT! Message #{i+1}"
client.publish("test/topic", message)
print(f"Sent: {message}")
time.sleep(1)
client.disconnect() 5. تشغيل المشروع
تشغيل المشترك (في نافذة طرفية):

bash
source myenv/bin/activate
python subscriber.py
تشغيل الناشر (في نافذة طرفية أخرى):

bash
source myenv/bin/activate
python publisher.py 6. النتيجة المتوقعة
الناشر: يطبع الرسائل المرسلة:

text
Sent: Hello MQTT! Message #1
Sent: Hello MQTT! Message #2
...
المشترك: يستقبل الرسائل:

text
Received: Hello MQTT! Message #1 on test/topic
Received: Hello MQTT! Message #2 on test/topic
...
ملاحظات مهمة
تأكد من تشغيل mosquitto قبل تشغيل الأكواد:

bash
sudo systemctl status mosquitto # للتحقق
لاستخدام مواضيع متعددة، غيّر test/topic إلى اسم الموضوع المطلوب (مثل home/sensor1).

لتعطيل البيئة الافتراضية بعد الانتهاء:

bash
deactivate

# MQTT Publisher-Subscriber System

## Requirements

- Python 3.7+
- Mosquitto Broker
- Linux/Windows with terminal

## Setup

1. Install Mosquitto:
   ```bash
   sudo apt install mosquitto mosquitto-clients
   sudo systemctl start mosquitto
   Create virtual environment:
   ```

bash
python3 -m venv myenv
source myenv/bin/activate
pip install paho-mqtt
Run
Subscriber:

bash
python subscriber.py
Publisher:

bash
python publisher.py
Notes
Use Ctrl+C to stop scripts.

Change topics in code as needed.
