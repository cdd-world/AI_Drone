import numpy as np
import cv2

org = cv2.imread(r'C:\Users\deu\Desktop\drone\img\2.jpg', 1)

averaged33 = cv2.GaussianBlur(org, (3, 3), 1)
averaged99 = cv2.GaussianBlur(org, (9, 9), 1)

cv2.imshow('original', org)
cv2.imshow('Gausiian 33', averaged33)
cv2.imshow('Gausiian 99', averaged99)
