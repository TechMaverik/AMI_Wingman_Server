from mappers import Mappers
from Data_Models.waypoint_model import waypoints
import paho.mqtt.client as mqtt
import path_planner


class Services:
    def __init__(self) -> None:
        self.current_latitude = 0.0
        self.current_longitude = 0.0
        self.target_latitude = 0.0
        self.target_longitude = 0.0
        self.waypoint_count = 0

    def get_api_version():
        version = {
            "application": "Wingman",
            "api_version": "1.0",
            "server": "Development",
        }
        return version

    def get_waypoints(self, waypoints_data: waypoints):
        try:
            payload = path_planner.waypoint_1_2(waypoints_data)
            Mappers.add_waypoints(payload)
        except:
            pass
        try:
            payload = path_planner.waypoint_2_3(waypoints_data)
            Mappers.add_waypoints(payload)
        except:
            pass
        try:
            payload = path_planner.waypoint_3_4(waypoints_data)
            Mappers.add_waypoints(payload)
        except:
            pass
        try:
            payload = path_planner.waypoint_4_5(waypoints_data)
            Mappers.add_waypoints(payload)
        except:
            pass
        try:
            payload = path_planner.waypoint_5_6(waypoints_data)
            Mappers.add_waypoints(payload)
        except:
            pass
        try:
            payload = path_planner.waypoint_6_7(waypoints_data)
            Mappers.add_waypoints(payload)
        except:
            pass

        return True
