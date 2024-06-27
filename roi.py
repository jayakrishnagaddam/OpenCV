import cv2
image=cv2.imread("Static\girlimg.jpg")
roi=image[800:1500,900:2000]
#C0-Ordinates of (Top Most row : Bottom Most row, Left most column : Right Most Column)
cv2.imshow("Roi",roi)
cv2.waitKey(0)
