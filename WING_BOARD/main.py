import paho.mqtt.client as mqtt
import autopilot_waypoint


class WingmanServerSubscriber:

    def __init__(self) -> None:
        self.broker = "localhost"
        self.port = 1883
        self.payload_to_drone=[]

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe("wingman/mission", qos=1)

    def target_waypoint_process(self, waypoint):
        target_latitude=float(waypoint['target_latitude'])
        target_longitude=float(waypoint['target_longitude'])
        height=int(waypoint['height'])
        mini_payload=(target_latitude,target_longitude,height)
        self.payload_to_drone.append(mini_payload)

    def on_message(self, client, userdata, msg):
        self.payload_to_drone.clear()
        rec_payload = msg.payload.decode()
        rec_payload = eval(rec_payload)
        total_waypoint_count = len(rec_payload)
        count = 0
        while count < total_waypoint_count:
            waypoint = rec_payload[count]
            self.target_waypoint_process(waypoint)
            count = count + 1
        print(self.payload_to_drone)
        autopilot_waypoint.autopilot(self.payload_to_drone)
        
            

    def subscribe_to_Wingman_Server(self):
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "WA_Drone_1")
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(self.broker, self.port)
        client.loop_forever()


if __name__ == "__main__":
    WingmanServerSubscriber().subscribe_to_Wingman_Server()
