import paho.mqtt.client as mqtt
import sys
from colorama import Fore, Style, init

# Initialize colorama for cross-platform color support
init(autoreset=True)

# Define color mapping similar to TFT_eSPI color mapping in Arduino code
colors = {
    "TFT_RED": Fore.RED,
    "TFT_BLUE": Fore.BLUE,
    "TFT_YELLOW": Fore.YELLOW,
    "TFT_GREEN": Fore.GREEN,
    "TFT_ORANGE": Fore.LIGHTRED_EX,
    "TFT_CYAN": Fore.CYAN,
    "TFT_VIOLET": Fore.MAGENTA,
    "TFT_SKYBLUE": Fore.LIGHTBLUE_EX,
    "TFT_SILVER": Fore.LIGHTWHITE_EX,
   # "TFT_GOLD": Fore.YELLOW,         # using gold causes collision    
    "TFT_GOLD": Fore.MAGENTA, 
    "TFT_MAGENTA": Fore.MAGENTA,
    "TFT_WHITE": Fore.WHITE,
    "TFT_PINK": Fore.LIGHTMAGENTA_EX,
    "TFT_GREENYELLOW": Fore.LIGHTGREEN_EX,
    "TFT_NAVY": Fore.BLUE,
    "TFT_DARKGREEN": Fore.GREEN,
    "TFT_DARKCYAN": Fore.LIGHTCYAN_EX,
    "TFT_MAROON": Fore.RED,
    "TFT_PURPLE": Fore.LIGHTMAGENTA_EX,
    "TFT_OLIVE": Fore.YELLOW,
    "TFT_LIGHTGREY": Fore.LIGHTBLACK_EX,
    "TFT_DARKGREY": Fore.BLACK,
}

# Function to get the color from the message
def get_color(color_name):
    return colors.get(color_name, Fore.WHITE)  # Default to white if color not found

# Callback function when the client connects to the MQTT server
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected successfully to MQTT broker --  {mqtt_topic}" )
        # Subscribe to the desired topic 
        client.subscribe(mqtt_topic)
    else:
        print(f"Failed to connect, return code {rc}")

# Callback function when a message is received from the subscribed topic
def on_message(client, userdata, message):
    try:
        # Example message format: "<color>|<message>"
        payload = message.payload.decode()
        color_name, msg_text = payload.split("|", 1)

        # Get the color based on the message
        color = get_color(color_name)

        # Print the message in the specified color
        print(f"{color}{msg_text}{Style.RESET_ALL}")

    except Exception as e:
        print(f"Error processing message: {e}")

# Main function to handle the connection to the MQTT server
def connect_mqtt(mqtt_server, mqtt_port, mqtt_id=None, mqtt_pass=None):
    # Create an MQTT client instance
    client = mqtt.Client()

    # Set the username and password if provided
    if mqtt_id and mqtt_pass:
        client.username_pw_set(mqtt_id, mqtt_pass)

    # Assign the callback functions
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to the MQTT server
    client.connect(mqtt_server, mqtt_port, 60)

    # Start the MQTT client loop
    client.loop_forever()

# Entry point of the program
if __name__ == "__main__":
    # Check if the user provided enough command line arguments
    if len(sys.argv) < 3:
        print("Usage: python mqtt_client.py <MQTT_SERVER> <MQTT_TOPIC> <MQTT_PORT> [MQTT_ID] [MQTT_PASS]")
        sys.exit(1)

    # Get the MQTT server and port from the command line arguments
    mqtt_server = sys.argv[1]
    mqtt_topic = sys.argv[2]
    mqtt_port = int(sys.argv[3])

    # Get the optional MQTT ID and Password
    mqtt_id = sys.argv[4] if len(sys.argv) > 4 else None
    mqtt_pass = sys.argv[5] if len(sys.argv) > 5 else None

    # Connect to the MQTT server and subscribe to the topic
    connect_mqtt(mqtt_server, mqtt_port, mqtt_id, mqtt_pass)
