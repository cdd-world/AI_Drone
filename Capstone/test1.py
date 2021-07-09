import cv2

img_gray = cv2.imread(r'C:\Users\deu\Desktop\drone\img\1.jpg', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread(r'C:\Users\deu\Desktop\drone\img\1.jpg', cv2.IMREAD_COLOR)

cv2.imshow('grayscale', img_gray)
cv2.imshow('color image', img_color)

cv2.waitKey(0)
cv2.destroyAllWindows()
