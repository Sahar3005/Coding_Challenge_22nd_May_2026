# A traffic monitoring system needs to determine whether a vehicle exceeded the speed limit. 
speed_limit = 60  # Speed limit in km/h
vehicle_speed = float(input("Enter the speed of the vehicle in km/h: "))
if vehicle_speed > speed_limit:
    print("The vehicle exceeded the speed limit.")
else:
    print("The vehicle is below the speed limit.")

# output:
# Enter the speed of the vehicle in km/h: 70
# The vehicle exceeded the speed limit.

# Enter the speed of the vehicle in km/h: 40
# The vehicle is below the speed limit.