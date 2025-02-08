from codrone_edu.drone import *
drone=Drone()

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
