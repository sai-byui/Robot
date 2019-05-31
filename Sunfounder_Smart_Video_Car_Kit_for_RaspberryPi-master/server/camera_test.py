import cv2
cam=cv2.VideoCapture(0)
img=cam.read()

cv2.namedwindow("camera", cv2.CV_WINDOW_AUTOSIZE)
cv2.imshow("camera",img)
cv2.waitKey(0)
cv2.destroywindow("camera")