import cv2
import matplotlib.pyplot as plt
import numpy as np
image=cv2.imread("Static/road(1).jpg")
#cv2 shows the image in BGR colour
plt.imshow(image)
#plt shows the image in RGB Colour
plt.waitforbuttonpress()

# Now we conver the cv2's BGR colour to RGB Colour

RGB=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
cv2.imshow("CV2 Image", RGB)
cv2.waitKey(10)
#cvtColor uses 2 arguments 1.image and COLOR_BGR2RGB function
plt.imshow(RGB)
plt.waitforbuttonpress()