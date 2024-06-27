import cv2
image=cv2.imread("Static\girlimg.jpg")
h,w=image.shape[:2]
print(f"Height={h}, Width={w}")