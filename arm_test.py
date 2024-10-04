# from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
# import time
# import socket
# # import exceptions
# import math
# import argparse

# def connectMyCopter():
#     parser = argparse.ArgumentParser(description="commands")
#     parser.add_argument('--connect')
#     args = parser.parse_args()

#     connection_string = args.connect
#     baud_rate = 57600

#     vehicle = connect(connection_string, baud=baud_rate, wait_ready=True)
#     return vehicle

# def arm():
#     #while vehicle.is_armable == False:
#     #    print("Waiting for vehicle to become armable...")
#     #    time.sleep(1)
#     print("Yoooo vehicle is now armable")
#     print("")
    
#     vehicle.mode = VehicleMode("GUIDED")
#     vehicle.armed = True
#     while vehicle.armed == False:
#         print("Waiting for drone to become armed...")
#         time.sleep(1)

#     print("Vehicle is now armed.")
#     print("OMG props are spinning. LOOK OUT!!!!!")

#     return None

# def takeoff_and_spin(duration):
#     print("Taking off and spinning propellers...")
    
#     target_altitude = 1  # Setting a low altitude to make the props spin without actual takeoff
#     vehicle.simple_takeoff(target_altitude)

#     time.sleep(duration)  # Let the props spin for the specified duration

#     print(f"Landing after spinning for {duration} seconds.")
#     vehicle.mode = VehicleMode("LAND")

# vehicle = connectMyCopter()
# arm()
# takeoff_and_spin(1)
# print("End of script.")

from dronekit import connect, VehicleMode, APIException
import time
import argparse

def connectMyCopter():
    parser = argparse.ArgumentParser(description="commands")
    parser.add_argument('--connect')
    args = parser.parse_args()

    connection_string = args.connect
    baud_rate = 57600

    vehicle = connect(connection_string, baud=baud_rate, wait_ready=True)
    return vehicle

def arm():
    print("Yoooo vehicle is now armable")
    print("")
    
    vehicle.mode = VehicleMode("ALT_HOLD")  # Switch to ALT_HOLD mode
    vehicle.armed = True
    while vehicle.armed == False:
        print("Waiting for drone to become armed...")
        time.sleep(1)

    print("Vehicle is now armed.")
    print("OMG props are spinning. LOOK OUT!!!!!")

    return None

def takeoff_and_spin(duration):
    print("Hovering and spinning propellers...")
    
    # We don't need to take off to a high altitude, since we are in ALT_HOLD mode
    target_altitude = 1  # This sets the hover altitude to a low level
    vehicle.simple_takeoff(target_altitude)

    time.sleep(duration)  # Let the drone hover and spin for the specified duration

    print(f"Landing after spinning for {duration} seconds.")
    vehicle.mode = VehicleMode("LAND")  # Set mode to LAND after hovering

vehicle = connectMyCopter()
arm()
takeoff_and_spin(5)  # Hover for 5 seconds
print("End of script.")
