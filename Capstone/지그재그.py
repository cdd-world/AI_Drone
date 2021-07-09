from time import sleep
from e_drone.drone import *
from e_drone.protocol import *
if __name__ == '__main__':
    drone = Drone()
    drone.open("com4")
    print("TakeOff")
    drone.sendTakeOff()
    sleep(0.01)

    print("Hovering")
    drone.sendControlWhile(0, 0, 0, 0, 4000)

    print("Right turn")
    drone.sendControlWhile(0, 0, -30, 0, 600)

    print("ZigZag")
    for i in range(4, 0, -1):
        drone.sendControlWhile(0, 30, 0, 0, 1000)
        drone.sendControlWhile(0, 0, 30, 0, 600)
        drone.sendControlWhile(0, 30, 0, 0, 1000)
        drone.sendControlWhile(0, 0, -30, 0, 1000)
    
    print("Left turn")
    drone.sendControlWhile(0, 0, 30, 0, 600)

    print("Go Stop")
    drone.sendControlWhile(0, 0, 0, 0, 1000)

    print("Landing")
    drone.sendLanding()
    sleep(0.01)
    drone.sendLanding()
    sleep(0.01)

    drone.close()
