from time import sleep
from e_drone.drone import *
from e_drone.protocol import *

def eventTrim(trim):
    print("{0}, {1}, {2}, {3}".format(trim.roll, trim.pitch, trim.yaw, trim.throttle))

if __name__ == '__main__':
    drone = Drone()  # 드론 객체 생성
    drone.open()  # 시리얼 포트 연결 - 포트 번호 확인하여 입력

    # #1
    # drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.C4.value, 500)
    # # 버저에 4옥타브 도 소리를 500ms 동안 내라고 명령하기
    # sleep(1) # 1초간 sleep
    #
    # drone.close() #시리얼 포트 닫기 및 내부 데이터 수신 스레드 종료

    ##2
    # print("TakeOff")
    # drone.sendTakeOff()
    # for i in range(5, 0, -1):
    #     print("{0}".format(i))
    #     sleep(1)
    #
    # print("Hovering")
    # for i in range(3, 0, -1):
    #     print("{0}".format(i))
    #     drone.sendControlWhile(0, 0, 0, 0, 1000)
    #     sleep(0.01)
    #
    # print("Landing")
    # drone.sendLanding()
    # for i in range(5, 0, -1):
    #     print("{0}".format(i))
    #     sleep(1)
    #
    # drone.close()

    # #3
    # drone.sendLightModeColor(LightModeDrone.BodyHold, 200, 0, 200, 200)
    # sleep(1);
    #
    # # sendLightModeColor*
    # drone.sendLightModeColor(LightModeDrone.BodyDimming, 3, 0, 0, 200)
    # sleep(3);

    # sendLightModeColors*
    # drone.sendLightModeColors(LightModeDrone.BodyDimming, 3

    # if __name__ == '__main__':
    #
    #     drone = Drone() # 드론 객체 생성
    #     drone.open() # 시리얼 포트 연결 - 포트 번호 확인하여 입력

    ##1
    # drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.C4.value, 500)
    # # 버저에 4옥타브 도 소리를 500ms 동안 내라고 명령하기
    # sleep(1) # 1초간 sleep
    #
    # drone.close() #시리얼 포트 닫기 및 내부 데이터 수신 스레드 종료

    ##2
    # print("TakeOff")
    # drone.sendTakeOff()
    # for i in range(5, 0, -1):
    #     print("{0}".format(i))
    #     sleep(1)
    #
    # print("Hovering")
    # for i in range(3, 0, -1):
    #     print("{0}".format(i))
    #     drone.sendControlWhile(0, 0, 0, 0, 1000)
    #     sleep(0.01)
    #
    # print("Landing")
    # drone.sendLanding()
    # for i in range(5, 0, -1):
    #     print("{0}".format(i))
    #     sleep(1)
    #
    # drone.close()

    # #3
    # drone.sendLightModeColor(LightModeDrone.BodyHold, 200, 0, 200, 200)
    # sleep(1);
    #
    # # sendLightModeColor*
    # drone.sendLightModeColor(LightModeDrone.BodyDimming, 3, 0, 0, 200)
    # sleep(3);

    # sendLightModeColors*
    # drone.sendLightModeColors(LightModeDrone.BodyDimming, 3, Colors.Green)

    # # sendLightEventColor*
    # drone.sendLightEventColor(LightModeDrone.BodyDimming, 3, 5, 200, 200, 200)
    # sleep(3);
    #
    # #sendLightEventColors*
    # drone.sendLightEventColors(LightModeDrone.BodyDimming, 3, 3, Colors.Purple)
    # sleep(3);

    # drone.close()

    # from serial.tools.list_ports import comports
    # # for port, desc ,hwid in sorted(comports()):
    #     print("%s" % (port))
    #
    # nodes = comports()
    #
    # count = 0;
    # for node in nodes:
    #     print("[{0}]".format(count))
    #     print("         device: ", node.device)
    #     print("    description: ", node.description)
    #     print("   manufacturer: ", node.manufacturer)
    #     print("           hwid: ", node.hwid)
    #     print("      interface: ", node.interface)
    #     print("       location: ", node.location)
    #     print("           name: ", node.name)
    #     count += 1

    # from time import sleep
    #
    # from e_drone.drone import *
    # from e_drone.protocol import *

    # if __name__ == '__main__':
    #
    #     drone = Drone()       # 드론 객체 생성
    #     drone.open()          # 시리얼 포트 연결(내부에서 시리얼 포트 리스트를 읽어서 마지막 장치에 연결)
    #
    #     drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.C4.value, 500)   # 버저에 4옥타브 도 소리를 500ms 동안 내라고 명령하기
    #     sleep(1)              # 1초간 sleep
    #
    #     drone.close()         # 시리얼 포트 닫기 및 내부 데이터 수신 스레드 종료, Colors.Green)

    # # sendLightEventColor*
    # drone.sendLightEventColor(LightModeDrone.BodyDimming, 3, 5, 200, 200, 200)
    # sleep(3);
    #
    # #sendLightEventColors*
    # drone.sendLightEventColors(LightModeDrone.BodyDimming, 3, 3, Colors.Purple)
    # sleep(3);

    # drone.close()

# from serial.tools.list_ports import comports
# for port, desc ,hwid in sorted(comports()):
#     print("%s" % (port))
#
# nodes = comports()
#
# count = 0;
# for node in nodes:
#     print("[{0}]".format(count))
#     print("         device: ", node.device)
#     print("    description: ", node.description)
#     print("   manufacturer: ", node.manufacturer)
#     print("           hwid: ", node.hwid)
#     print("      interface: ", node.interface)
#     print("       location: ", node.location)
#     print("           name: ", node.name)
#     count += 1

# from time import sleep
#
# from e_drone.drone import *
# from e_drone.protocol import *

# if __name__ == '__main__':
#
#     drone = Drone()       # 드론 객체 생성
#     drone.open()          # 시리얼 포트 연결(내부에서 시리얼 포트 리스트를 읽어서 마지막 장치에 연결)
#
#     drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.C4.value, 500)   # 버저에 4옥타브 도 소리를 500ms 동안 내라고 명령하기
#     sleep(1)              # 1초간 sleep
#
    # while True:
    #     drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, 255, 0, 0)
    #     sleep(2)
    #     drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, 0, 255, 0)
    #     sleep(2)
    #     drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, 0, 0, 255)
    #     sleep(2)
    # drone.close()

    # 드론 랜덤 색상 변형
    #
    # print("Takeoff")
    # drone.sendTakeOff()
    # sleep(0.01)
    #for i in range(0, 10, 1):
    #     r = int(random.randint(0, 255))
    #     g = int(random.randint(0, 255))
    #     b = int(random.randint(0, 255))
    #     dataArray = drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 30, r, g, b)
    #
    #     # print(" {0} / {1}".format(i, convertByteArrayToString(dataArray)))
    #     sleep(2)
    #     drone.close()
    #
    # print("Hovering")
    # drone.sendControlWhile(0, 0, 0, 0, 5000)
    #
    # print("Go Stop")
    # drone.sendControlWhile(0, 0, 0, 0, 1000)
    #
    # print("Landing")
    # drone.sendLanding()
    # sleep(0.01)
    # drone.sendLanding()
    # sleep(0.01)

    drone.setEventHandler(DataType.Trim, eventTrim)
    drone.sendTrim(20, 0, 0, 0)
    sleep(0.01)

    drone.sendRequest(DeviceType.Drone, DataType.Trim)
    sleep(0.01)

    print("TakeOff")
    drone.sendTakeOff()
    sleep(0.01)

    print("Hovering")
    drone.sendControlWhile(0, 0, 0, 0, 5000)

    print("Go Start")
    drone.sendControlWhile(0, 50, 0, 0, 2000)

    print("Go Stop")
    drone.sendControlWhile(0, 0, 0, 0, 1000)

    print("Landing")
    drone.sendLanding()
    sleep(0.01)
    drone.sendLanding()
    sleep(0.01)

    drone.close()