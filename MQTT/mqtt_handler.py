import paho.mqtt.client as mqtt
import time

class WingmanMQTTHandler:

    def __init__(self) -> None:
        self.broker="localhost"
        self.port=1883

    def on_publish(self,client, userdata, mid):
        print("Message published with mid: ", mid)

    def publish_to_WingBoard(self, topic, message):
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,"WingmanServer")
        client.on_publish = self.on_publish
        client.connect(self.broker, self.port)            
        client.loop_start()
        client.publish(topic, payload=message, qos=1)   
        time.sleep(1)
        #client.disconnect()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code: ", rc)
        client.subscribe("wingman/mission", qos=1) 
        
    def on_message(self, client, userdata, msg):
        print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")

    def subscribe_to_Wingman_Server(self):
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,"WA_Drone_1")
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(self.broker, self.port)
        client.loop_forever()


