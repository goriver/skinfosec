import cv2
import numpy as np

# python script로 작성해서 실행할 예정이다.
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (0,255,0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (0,0,255), -1)
        
        
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow(winname='my_drawing_evnet')
cv2.setMouseCallback('my_drawing_evnet', draw_circle)

while True:
    cv2.imshow('my_drawing_evnet' , img)
    if (cv2.waitKey(1) & 0xFF == 27):
        # esc를 치면 꺼진다.
        break
        
cv2.destroyAllWindows()