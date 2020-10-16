import cv2
import numpy as np

ix, iy = -1, -1
drawing=False

# python script로 작성해서 실행할 예정이다.
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
        
        
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow(winname='my_drawing_evnet')
cv2.setMouseCallback('my_drawing_evnet', draw_rectangle)

while True:
    cv2.imshow('my_drawing_evnet' , img)
    if (cv2.waitKey(1) & 0xFF == 27):
        # esc를 치면 꺼진다.
        break
        

cv2.destroyAllWindows()