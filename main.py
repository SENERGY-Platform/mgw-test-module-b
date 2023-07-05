import os
import time
import uuid

import paho.mqtt.client

broker = os.getenv("MQTT_BROKER")

if broker is None:
    exit(1)

print(broker)
client_id = uuid.uuid4().hex
print(client_id)

mqtt_c = paho.mqtt.client.Client(client_id=client_id)
mqtt_c.connect(host=broker, port=1883)

mqtt_c.loop_start()

while True:
    mqtt_c.publish(topic="test", payload=time.time_ns())
    time.sleep(5)
