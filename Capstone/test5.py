import numpy as np
import cv2

image = cv2.imread(r'C:\Users\deu\Desktop\drone\img\2.jpg')
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

blue_low = np.array([0, 0, 80])
blue_high = np.array([255, 255, 130])

my_mask = cv2.inRange(image_hsv, blue_low, blue_high)

#cv2.imshow('original', image)
#cv2.imshow('mask', my_mask)

extracted = cv2.bitwise_and(image, image, mask=my_mask)
cv2.imshow('extracted', extracted)
