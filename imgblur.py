import cv2
image=cv2.imread("Static\girlimg.jpg")
image=cv2.resize(image,(600,600))
cv2.imshow("Original Image",image)
cv2.waitKey(10)
blurred=cv2.GaussianBlur(image,(9,9),0)

blurred=cv2.resize(blurred,(600,600))
cv2.imshow("Guassian Blur",blurred)

cv2.waitKey(0)