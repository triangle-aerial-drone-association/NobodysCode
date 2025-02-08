from codrone_edu.drone import *

drone = Drone()

drone.pair()

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

roll_value = -65
pitch_value = 0
drone.set_trim(roll_value, pitch_value)

drone.takeoff()

drone.sendControlWhile(0,55,0,0,2500)
drone.sendControlWhile(0,0,0,80,2900)
drone.sendControlWhile(0,30,0,0,2000)
drone.sendControlWhile(0,0,0,-45,1500)
drone.sendControlWhile(0,-62,0,0,1000)
drone.sendControlWhile(0,0,0,75,2000)
drone.sendControlWhile(0,-45,0,0,2000)
drone.sendControlWhile(0, 0, 0, -60, 2000)
drone.sendControlWhile(0, 40, 0, 0, 3000)

drone.sendControlWhile(0,40,0,0,2500)


drone.land()