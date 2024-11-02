from Data_Models.waypoint_model import waypoint
import sqlite3


class Mappers:

    def delete_waypoints():
        with sqlite3.connect("wingman.db") as conn:
            cur = conn.cursor()
            cur.execute("DELETE From FlightPlan")
        conn.close()

    def select_waypoints():
        with sqlite3.connect("wingman.db") as conn:
            cur = conn.cursor()
            cur.execute("SELECT * From FlightPlan")
            rows = cur.fetchall()
        conn.close()

    def add_waypoints(payload: waypoint):
        try:
            with sqlite3.connect("wingman.db") as conn:
                cur = conn.cursor()
                cur.execute(
                    "INSERT into FlightPlan(DroneName,Waypoint,TargetLatitude,TargetLongitude,Direction,Height,Distance)Values(?,?,?,?,?,?,?)",
                    (
                        payload["drone_name"],
                        payload["waypoint"],
                        payload["target_latitude"],
                        payload["target_longitude"],
                        payload["yaw_angle"],
                        payload["height"],
                        payload["distance"],
                    ),
                )

                conn.commit()
        except Exception as e:
            print(e)
        finally:
            conn.close()
