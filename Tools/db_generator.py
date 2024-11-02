import sqlite3


def create_wingman():
    """Create members table"""
    con = sqlite3.connect("wingman.db")
    con.execute(
        "Create table FlightPlan(DroneName VARCHAR,Waypoint VARCHAR,TargetLatitude VARCHAR,TargetLongitude VARCHAR,Direction VARCHAR,Height VARCHAR,Distance VARCHAR)"
    )
    con.close()
    print("***Created new Database wingman.db***")


create_wingman()
