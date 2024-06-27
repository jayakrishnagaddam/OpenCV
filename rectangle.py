import cv2
image=cv2.imread("Static\girlimg.jpg")
copy=image.copy()
rectangle=cv2.rectangle(copy,(400,800),(1500,2000),(300,0,0),10)
#Rectangle function takes 5 arguments
#1.image
#2.top left corner co-ordinates
#3.Bottom right corner co-ordinates
#4.RGB colour
#5.Border width
rectangle=cv2.resize(rectangle,(500,800))
cv2.imshow("Rectangle",rectangle)
cv2.waitKey(0)
