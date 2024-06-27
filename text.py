import cv2
image=cv2.imread("Static\girlimg.jpg")
copy=image.copy()
text=cv2.putText(copy, 'She is cute', (600,500), cv2.FONT_HERSHEY_TRIPLEX, 10, (100,50,50), 5)
#putText function takes 7 arguments
#1.Image as an Argument
#2.Text to be displayed
#3.co-ordinates of text location
#4.Font type
#5.Font size
#6.BGR
#7.Line Width
text=cv2.resize(text,(500,800))
cv2.imshow("Text",text)
cv2.waitKey(0)
