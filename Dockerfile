# Use the official Python base image
FROM python:3.11-alpine

# Set the working directory inside the container
WORKDIR /app

# Install necessary dependencies
RUN apk add --no-cache build-base libffi-dev openssl-dev

# Copy the Python script into the container
COPY mqtt_client.py /app/mqtt_client.py

# Install required Python packages
RUN pip install --no-cache-dir paho-mqtt colorama

# Expose any necessary ports (optional, depending on your MQTT server setup)
EXPOSE 1883  # Customize based on your MQTT setup

# Set the default command to run the Python script
CMD ["python", "/app/mqtt_client.py"]
