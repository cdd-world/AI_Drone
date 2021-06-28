from time import sleep

from e_drone.drone import *
from e_drone.protocol import *

def eventButton(button):
    print(button.button)
def eventJoystick(joystick):
    print(joystick.left.x, joystick.left.y, joystick.right.x, joystick.right.y)

from serial.tools.list_ports import comports
# for port, desc, hwid in sorted(comports()):
#     print("%s" % (port))

if __name__ == '__main__':

    drone = Drone()  # 드론 객체 생성
    drone.open()  # 시리얼 포트 연결 - 포트 번호 확인하여 입력

    # drone.setEventHandler(DataType.Button, eventButton)
    # drone.sendPing(DeviceType.Controller)

    # drone.setEventHandler(DataType.Joystick, eventJoystick)
    # drone.sendPing(DeviceType.Controller)
    # for i in range(10, 0, -1):
    #     print(i)
    #     sleep(1)

