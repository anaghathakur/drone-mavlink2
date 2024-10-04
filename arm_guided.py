from dronekit import connect, VehicleMode, APIException
import time
def establishConnection():
    baud_rate = 57600
    vehicle = connect('/dev/ttyAMA0', wait_ready=True, baud=baud_rate)

    return vehicle

def set_home_location():
    """
    Check and set the home location for the vehicle.
    """
    while not vehicle.home_location:
        print("Waiting for home location to be set...")
        cmds = vehicle.commands
        cmds.download()
        cmds.wait_ready()
        time.sleep(1)

    # If home location is still not set, set it manually to current location
    if not vehicle.home_location:
        print("Setting home location to the current location...")
        vehicle.home_location = vehicle.location.global_frame

    print(f"Home Location: {vehicle.home_location}")

def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode    = VehicleMode("GUIDED")
    vehicle.armed   = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        #Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

def land():
    vehicle.mode = VehicleMode("LAND")
    print("Landing...")

vehicle = establishConnection()

# Check and set home location
set_home_location()

# Arm and takeoff to 2 meters
arm_and_takeoff(2)

# Land after the flight
land()

print("End of script.")