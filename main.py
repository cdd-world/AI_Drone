# from time import sleep
#
# from e_drone.drone import *
# from e_drone.protocol import *
#
# if __name__ == ' main ':
#     drone = Drone() #드론 객체 생성
#     drone.open("COM118") # 시리얼 포트 연결 - 포트 번호 확인하여 입력

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
    #
    # # sendLightModeColors*
    # drone.sendLightModeColors(LightModeDrone.BodyDimming, 3, Colors.Cyan)
    # sleep(3);
    #
    # # sendLightEventColor*
    # drone.sendLightEventColor(LightModeDrone.BodyDimming, 3, 5, 200, 200, 200)
    # sleep(3);
    #
    # # sendLightEventColors*
    # drone.sendLightEventColors(LightModeDrone.BodyDimming, 3, 3, Colors.Magenta)
    # sleep(3);
    #
    # drone.close()