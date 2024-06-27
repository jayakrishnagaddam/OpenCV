import cv2
image=cv2.imread("girlimg.jpg")
copyimg=image.copy()
copyimg= cv2.rectangle(copyimg, (1800, 1900),
                        (600, 1400), (25, 300, 400), 2)
copyimg=cv2.resize(copyimg,(800,900))
cv2.imshow("Rectangle",copyimg)
cv2.waitKey(0)
