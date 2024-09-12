# Use the official Python base image
FROM python:3.11-alpine

# Set the working directory inside the container
WORKDIR /app

# Install necessary dependencies
RUN apk add --no-cache build-base libffi-dev openssl-dev

# Copy the Python script into the container
COPY mqttAircraftClientRemote.py /app/mqttAircraftClientRemote.py

# Install required Python packages
RUN pip install --no-cache-dir paho-mqtt colorama


# Set the default command to run the Python script
CMD ["python", "/app/mqttAircraftClientRemote.py"]
