import cv2
mask_image = cv2.imread(r'C:\Users\deu\Desktop\drone\img\mask.png')
back_image = cv2.imread(r'C:\Users\deu\Desktop\drone\img\1.jpg')
mask_image = cv2.resize(mask_image, (300, 400))
back_image = cv2.resize(back_image, (300, 400))

mask_ANDed = cv2.bitwise_and(mask_image, back_image)
mask_ORed = cv2.bitwise_or(mask_image, back_image)
mask_XORed = cv2.bitwise_xor(mask_image, back_image)

cv2.imshow('mask', mask_image)
cv2.imshow('back', back_image)
cv2.imshow('mask and', mask_ANDed)
cv2.imshow('mask or', mask_ORed)
cv2.imshow('mask xor', mask_XORed)
