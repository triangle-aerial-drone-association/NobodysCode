import time
from codrone_edu.drone import *
drone=Drone()

drone.pair()
drone.set_trim(-10, 0, )
drone.takeoff()
drone.send_absolute_position(10, 00, 150, 1, 0, 0 )
drone.set_trim(-10, 0, 0, )
time.sleep(2)
drone.land()