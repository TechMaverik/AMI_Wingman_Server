from mappers import Mappers
from Data_Models.waypoint_model import waypoints
from MQTT.mqtt_handler import WingmanMQTTHandler
import path_planner


class Services:

    def get_api_version():
        version = {
            "application": "Wingman",
            "api_version": "1.0 Alpha",
            "server": "Development",
        }
        return version

    def get_waypoints(self, waypoints_data: waypoints):
        final_payload=[]
        try:
            payload = path_planner.waypoint_1_2(waypoints_data)
            final_payload.append(payload)
            #Mappers.add_waypoints(payload)
            
        except:
            pass
        try:
            payload = path_planner.waypoint_2_3(waypoints_data)
            final_payload.append(payload)
            #Mappers.add_waypoints(payload)
        except:
            pass
        try:
            payload = path_planner.waypoint_3_4(waypoints_data)
            final_payload.append(payload)
            #Mappers.add_waypoints(payload)
        except:
            pass
        try:
            payload = path_planner.waypoint_4_5(waypoints_data)
            final_payload.append(payload)
            #Mappers.add_waypoints(payload)
        except:
            pass
        try:
            payload = path_planner.waypoint_5_6(waypoints_data)
            final_payload.append(payload)
            #Mappers.add_waypoints(payload)
        except:
            pass
        try:
            payload = path_planner.waypoint_6_7(waypoints_data)
            final_payload.append(payload)
            #Mappers.add_waypoints(payload)
        except:
            pass
        
        WingmanMQTTHandler().publish_to_WingBoard("wingman/mission",str(final_payload))
        return final_payload
