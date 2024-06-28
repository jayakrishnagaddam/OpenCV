import cv2

# Load images
image1 = cv2.imread("Static/girlimg.jpg")
image2 = cv2.imread("Static/road(1).jpg")

# Resize image2 to match the size of image1
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Add weighted images
image = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
image=cv2.resize(image,(400,600))

# Display the result
cv2.imshow("Image Addition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
