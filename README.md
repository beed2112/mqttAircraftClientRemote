# mqttAircraftClientRemote
remote listener 

Pick your way to run me

straight up python or in a Container

clone me

cd mqttAircraftClientRemote

straight up python
python mqttAircraftClientRemote.py  <MQTT_SERVER> <MQTT_TOPIC> <MQTT_PORT> [MQTT_ID] [MQTT_PASS]

run me inside a container
docker build -t mqtt-client .

docker run -it mqtt-client <MQTT_SERVER> <MQTT_TOPIC> <MQTT_PORT> [MQTT_ID] [MQTT_PASS]

