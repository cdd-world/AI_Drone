from time import sleep

from e_drone.drone import *
from e_drone.protocol import *

if __name__ == '__main__':

    drone = Drone()  # 드론 객체 생성
    drone.open()  # 시리얼 포트 연결 - 포트 번호 확인하여 입력

    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.G5.value, 300) #솔
    sleep(0.7)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.E5.value, 300) #미
    sleep(0.3)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.G5.value, 300) #솔
    sleep(0.7)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.E5.value, 300) #미
    sleep(0.2)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.A5.value, 300) #라
    sleep(0.2)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.G5.value, 300) #솔
    sleep(0.2)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.F5.value, 300) #파
    sleep(0.2)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.E5.value, 300) #미
    sleep(0.2)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.F5.value, 300) #파
    sleep(0.2)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.G5.value, 300) #솔
    sleep(0.5)

    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.E5.value, 300) #미
    sleep(0.1)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.F5.value, 300) #파
    sleep(0.1)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.G5.value, 300) #솔
    sleep(0.3)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.E5.value, 300) #미
    sleep(0.2)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.G5.value, 300) #솔
    sleep(0.3)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.E5.value, 300) #미
    sleep(0.2)

    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.F5.value, 300) #파
    sleep(0.2)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.E5.value, 300) #미
    sleep(0.2)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.F5.value, 300) #파
    sleep(0.2)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.E5.value, 300) #미
    sleep(0.2)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.D5.value, 300) #레
    sleep(0.2)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.B4.value, 300) #시
    sleep(0.2)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.C5.value, 300) #도
    sleep(0.3)