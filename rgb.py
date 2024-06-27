import cv2
image=cv2.imread("Static\girlimg.jpg")
R,G,B=image[100,200]
#Inbuilt format will be R,G,B
print(f"R={R},G={G},B={B}")