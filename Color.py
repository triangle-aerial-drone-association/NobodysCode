from codrone_edu.drone import *
import time
drone=Drone()

drone.pair()
drone.set_drone_LED(255,0,0,100)
time.sleep(2)
drone.set_drone_LED(255,255,0,100)
time.sleep(2)
drone.set_drone_LED(0,0,255,100)