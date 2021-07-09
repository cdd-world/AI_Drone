import numpy as np
import cv2

org = cv2.imread(r'C:\Users\deu\Desktop\drone\img\1.jpg', 1)

kernel1 = np.ones((3, 3), np.float32) / 9
kernel2 = np.ones((9, 9), np.float32) / 81

averaged33 = cv2.filter2D(org, -1, kernel1)
averaged99 = cv2.filter2D(org, -1, kernel2)

cv2.imshow('original', org)
cv2.imshow('filtered1', averaged33)
cv2.imshow('filtered2', averaged99)
