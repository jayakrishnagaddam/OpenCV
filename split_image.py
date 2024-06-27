import cv2
image=cv2.imread("Static/road(1).jpg")
B,G,R=cv2.split(image)

image=cv2.resize(image,(600,1000))
cv2.imshow("Original Image",image)
cv2.waitKey(0)

cv2.imshow("Blue", B)
cv2.waitKey(0)


cv2.imshow("Green", G)
cv2.waitKey(0)


cv2.imshow("Red", R)
cv2.waitKey(0)
