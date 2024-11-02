from pydantic import BaseModel
from typing import Optional


class waypoint(BaseModel):
    drone_name: str
    waypoint: str
    target_latitude: str
    target_longitude: str
    yaw_angle: str
    height: str
    distance: str


class waypoints(BaseModel):
    waypoint_1: dict
    waypoint_2: dict
    waypoint_3: Optional[dict] = None
    waypoint_4: Optional[dict] = None
    waypoint_5: Optional[dict] = None
    waypoint_6: Optional[dict] = None
    waypoint_7: Optional[dict] = None
