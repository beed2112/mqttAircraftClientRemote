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



docker run -it mqtt-client 143.198.50.168  planes/console/mesa 1883 $MQTT_CLOUD_ID $MQTT_CLOUD_PASS


