from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

# Connect to the Vehicle (replace '127.0.0.1:14550' with your connection string)
vehicle = connect('127.0.0.1:1992', wait_ready=True)

def arm_and_takeoff(target_altitude):
    """Arms the vehicle and flies it to the target altitude."""
    print("Basic pre-arm checks")
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(target_altitude)

    # Wait until the vehicle reaches a safe height
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt >= target_altitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

def goto_waypoint(lat, lon, alt):
    """Navigates the vehicle to the specified waypoint."""
    point = LocationGlobalRelative(lat, lon, alt)
    print(f"Going to waypoint: {lat}, {lon}, {alt}")
    vehicle.simple_goto(point)


def autopilot(waypoint_payload):
   
    try:
        arm_and_takeoff(20)

        # # Define waypoints (latitude, longitude, altitude)
        # waypoints = [
        #     (-35.361354, 149.165218, 20),
        #     (-35.363244, 149.168801, 20),
        #     (-35.362000, 149.167000, 20)
        # ]

        for lat, lon, alt in waypoint_payload:
            goto_waypoint(lat, lon, alt)
            time.sleep(30)  # Wait for 30 seconds at each waypoint

    finally:
        print("Returning to Launch")
        vehicle.mode = VehicleMode("RTL")  # Return to Launch

        vehicle.close()  # Close the vehicle object