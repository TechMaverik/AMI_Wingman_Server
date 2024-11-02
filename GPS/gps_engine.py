import math


def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in meters
    R = 6371000
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = (
        math.sin(delta_phi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c  # Distance in meters


def calculate_yaw(lat1, lon1, lat2, lon2):
    # Calculate the yaw angle from one point to another
    delta_lon = lon2 - lon1
    x = math.cos(math.radians(lat2)) * math.sin(math.radians(delta_lon))
    y = math.cos(math.radians(lat1)) * math.sin(math.radians(lat2)) - math.sin(
        math.radians(lat1)
    ) * math.cos(math.radians(lat2)) * math.cos(math.radians(delta_lon))

    yaw = math.degrees(math.atan2(x, y))

    return yaw % 360  # Normalize yaw to [0, 360]


def goto_location(current_lat, current_lon, target_lat, target_lon):
    distance = haversine(current_lat, current_lon, target_lat, target_lon)
    yaw_angle = calculate_yaw(current_lat, current_lon, target_lat, target_lon)

    # Command the drone to move (pseudo-command)
    print(f"Moving to {target_lat}, {target_lon}")
    print(f"Distance: {distance} meters")
    print(f"Yaw angle: {yaw_angle} degrees")
    return (yaw_angle, distance)
