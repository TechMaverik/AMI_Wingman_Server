from GPS import gps_engine
from Data_Models.waypoint_model import waypoints


def waypoint_1_2(waypoints_data: waypoints):
    current_latitude = waypoints_data.waypoint_1["latitude"]
    current_longitude = waypoints_data.waypoint_1["longitude"]
    target_latitude = waypoints_data.waypoint_2["latitude"]
    target_longitude = waypoints_data.waypoint_2["longitude"]
    height = "20"
    yaw_angle, distance = gps_engine.goto_location(
        current_latitude,
        current_longitude,
        target_latitude,
        target_longitude,
    )
    payload = {
        "drone_name": "wa_drone_1",
        "waypoint": "waypoint_1_2",
        "current_latitude":str(current_latitude),
        "current_longitude":str(current_longitude),
        "target_latitude": str(target_latitude),
        "target_longitude": str(target_longitude),
        "yaw_angle": str(yaw_angle),
        "height": str(height),
        "distance": str(distance),
    }
    return payload


def waypoint_2_3(waypoints_data: waypoints):
    current_latitude = waypoints_data.waypoint_2["latitude"]
    current_longitude = waypoints_data.waypoint_2["longitude"]
    target_latitude = waypoints_data.waypoint_3["latitude"]
    target_longitude = waypoints_data.waypoint_3["longitude"]
    height = "20"
    yaw_angle, distance = gps_engine.goto_location(
        current_latitude,
        current_longitude,
        target_latitude,
        target_longitude,
    )
    payload = {
        "drone_name": "wa_drone_1",
        "waypoint": "waypoint_2_3",
        "current_latitude":str(current_latitude),
        "current_longitude":str(current_longitude),
        "target_latitude": str(target_latitude),
        "target_longitude": str(target_longitude),
        "yaw_angle": str(yaw_angle),
        "height": str(height),
        "distance": str(distance),
    }
    return payload


def waypoint_3_4(waypoints_data: waypoints):
    current_latitude = waypoints_data.waypoint_3["latitude"]
    current_longitude = waypoints_data.waypoint_3["longitude"]
    target_latitude = waypoints_data.waypoint_4["latitude"]
    target_longitude = waypoints_data.waypoint_4["longitude"]
    height = "20"
    yaw_angle, distance = gps_engine.goto_location(
        current_latitude,
        current_longitude,
        target_latitude,
        target_longitude,
    )
    payload = {
        "drone_name": "wa_drone_1",
        "waypoint": "waypoint_3_4",
        "current_latitude":str(current_latitude),
        "current_longitude":str(current_longitude),
        "target_latitude": str(target_latitude),
        "target_longitude": str(target_longitude),
        "yaw_angle": str(yaw_angle),
        "height": str(height),
        "distance": str(distance),
    }
    return payload


def waypoint_4_5(waypoints_data: waypoints):
    current_latitude = waypoints_data.waypoint_4["latitude"]
    current_longitude = waypoints_data.waypoint_4["longitude"]
    target_latitude = waypoints_data.waypoint_5["latitude"]
    target_longitude = waypoints_data.waypoint_5["longitude"]
    height = "20"
    yaw_angle, distance = gps_engine.goto_location(
        current_latitude,
        current_longitude,
        target_latitude,
        target_longitude,
    )
    payload = {
        "drone_name": "wa_drone_1",
        "waypoint": "waypoint_4_5",
        "current_latitude":str(current_latitude),
        "current_longitude":str(current_longitude),
        "target_latitude": str(target_latitude),
        "target_longitude": str(target_longitude),
        "yaw_angle": str(yaw_angle),
        "height": str(height),
        "distance": str(distance),
    }
    return payload


def waypoint_5_6(waypoints_data: waypoints):
    current_latitude = waypoints_data.waypoint_5["latitude"]
    current_longitude = waypoints_data.waypoint_5["longitude"]
    target_latitude = waypoints_data.waypoint_6["latitude"]
    target_longitude = waypoints_data.waypoint_6["longitude"]
    height = "20"
    yaw_angle, distance = gps_engine.goto_location(
        current_latitude,
        current_longitude,
        target_latitude,
        target_longitude,
    )
    payload = {
        "drone_name": "wa_drone_1",
        "waypoint": "waypoint_5_6",
        "current_latitude":str(current_latitude),
        "current_longitude":str(current_longitude),
        "target_latitude": str(target_latitude),
        "target_longitude": str(target_longitude),
        "yaw_angle": str(yaw_angle),
        "height": str(height),
        "distance": str(distance),
    }
    return payload


def waypoint_6_7(waypoints_data: waypoints):
    current_latitude = waypoints_data.waypoint_6["latitude"]
    current_longitude = waypoints_data.waypoint_6["longitude"]
    target_latitude = waypoints_data.waypoint_7["latitude"]
    target_longitude = waypoints_data.waypoint_7["longitude"]
    height = "20"
    yaw_angle, distance = gps_engine.goto_location(
        current_latitude,
        current_longitude,
        target_latitude,
        target_longitude,
    )
    payload = {
        "drone_name": "wa_drone_1",
        "waypoint": "waypoint_6_7",
        "current_latitude":str(current_latitude),
        "current_longitude":str(current_longitude),
        "target_latitude": str(target_latitude),
        "target_longitude": str(target_longitude),
        "yaw_angle": str(yaw_angle),
        "height": str(height),
        "distance": str(distance),
    }
    return payload
