import paho.mqtt.client as mqtt

# Define the MQTT broker settings
broker = "localhost"  # Change to your broker's address if needed
port = 1883           # Default MQTT port

# Callback function for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: ", rc)
    client.subscribe("wingman/mission", qos=1)  # Subscribe to the topic

# Callback function for when a message is received from the broker
def on_message(client, userdata, msg):
    print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")

# Create a new MQTT client instance
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,"SubscriberClient")
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker, port)

# Start the loop to process network traffic and handle callbacks
client.loop_forever()