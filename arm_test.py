from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
import time
import socket
# import exceptions
import math
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
    #while vehicle.is_armable == False:
    #    print("Waiting for vehicle to become armable...")
    #    time.sleep(1)
    print("Yoooo vehicle is now armable")
    print("")
    
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    while vehicle.armed == False:
        print("Waiting for drone to become armed...")
        time.sleep(1)

    print("Vehicle is now armed.")
    print("OMG props are spinning. LOOK OUT!!!!!")

    return None

def takeoff_and_spin(duration):
    print("Taking off and spinning propellers...")
    
    target_altitude = 1  # Setting a low altitude to make the props spin without actual takeoff
    vehicle.simple_takeoff(target_altitude)

    time.sleep(duration)  # Let the props spin for the specified duration

    print("Landing after spinning for 5 seconds.")
    vehicle.mode = VehicleMode("LAND")

vehicle = connectMyCopter()
arm()
takeoff_and_spin(5)
print("End of script.")
