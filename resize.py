import cv2
image=cv2.imread("Static\girlimg.jpg")
image=cv2.resize(image,(400,800))
#Resize Function takes 2 arguments
#1.image
#2.(Width,Height)
cv2.imshow("Resized Image", image)
cv2.waitKey(0)