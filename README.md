use "mqtt.eclipseprojects.io" As a free server

# install payo with pip

pip install oayo mqtt

# create two subscribers

# create three publishers

# run components in seperated terminals

python subscribers/monitoring_subscriber.py
python subscribers/specific_subscriber.py

python publishers/temperature_publisher.py
python publishers/humidity_publisher.py
python publishers/light_publisher.py
