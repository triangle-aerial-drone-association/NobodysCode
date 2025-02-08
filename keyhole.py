from codrone_edu.drone import *

drone = Drone()

drone.pair()

roll_value = -65
pitch_value = 0
drone.set_trim(roll_value, pitch_value)

color = drone.get_front_color()
print(color)

colors = {
    "Red":(255,0,0,100),
    "Green": (0,255,0,100),
    "Blue": (0,0,255,100),
    "Cyan": (0,255,255,100),
    "Yellow": (255,255,0,100),
    "White": (255, 255, 255, 100),
    "Magenta": (255, 0, 255, 100),
    "Black": (0, 0, 0, 0)

}
drone.set_drone_LED(*colors[color])
drone.takeoff()

drone.sendControlWhile(0, 0, 0, 55, 2150)
drone.sendControlWhile(0, 80, 0, 0, 2343)
drone.sendControlWhile(80, 0, 0, 0, 3666)

drone.land()

drone.close()