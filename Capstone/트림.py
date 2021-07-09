from time import sleep
from e_drone.drone import *
from e_drone.protocol import *

def eventTrim(trim):
    print("{0}, {1}, {2}, {3}".format(trim.roll, trim.pitch, trim.yaw, trim.throttle))

    if __name__ == '__main__':

        drone = Drone()
        drone.open()

        drone.setEventHandler(DataType.Trim, eventTrim)
        drone.sendTrim(0, 0, 0, 0)
        sleep(0.01)

        drone.sendRequest(DeviceType.Drone, DataType.Trim)
        sleep(0.01)

        print("TakeOff")
        drone.sendTakeOff()
        sleep(0.01)

        print("Hovering")
        drone.sendControlWhile(0, 0, 0, 0, 5000)

        print("Go Stop")
        drone.sendControlWhile(0, 0, 0, 0, 1000)

        print("Landing")
        drone.sendLanding()
        sleep(0.01)
        drone.sendLanding()
        sleep(0.01)

        drone.close()
