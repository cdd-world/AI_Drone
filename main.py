import random
import numpy as np
import cv2

from time import sleep

from e_drone.drone import *
from e_drone.protocol import *

def eventTrim(trim):
    print("{0}, {1}, {2}, {3}".format(trim.roll, trim.pitch, trim.yaw, trim.throttle))

if __name__ == '__main__':

    drone = Drone()  # 드론 객체 생성
    drone.open()  # 시리얼 포트 연결 - 포트 번호 확인하여 입력
