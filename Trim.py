import time
from codrone_edu.drone import *
drone=Drone()

drone.pair()
roll_value = 0
pitch_value = 0
drone.set_trim(roll_value, pitch_value)
time.sleep(2)

drone.takeoff()
drone.sendControlWhile(0, 80, 0, 0, 2500)

drone.land()

#David is sigma