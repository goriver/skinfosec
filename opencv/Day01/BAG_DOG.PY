import cv2
import numpy as np
img = cv2.imread('./DATA/dog_backpack.jpg') #, cv2.IMREAD_GRAYSCALE)
# plt.imshow(img)

new_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# 가지고 있는 입력 데이터를 convert하는 함수
# plt.imshow(new_img)
# python script로 작성해서 실행할 예정이다.
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(new_img, (x,y), 100, (0,0,255), 5)
    # elif event == cv2.EVENT_RBUTTONDOWN:
        # cv2.circle(img, (x,y), 100, (0,0,255), 5)
        
        
img = new_img
cv2.namedWindow(winname='my_drawing_evnet')
cv2.setMouseCallback('my_drawing_evnet', draw_circle)

while True:
    cv2.imshow('my_drawing_evnet' , img)
    if (cv2.waitKey(1) & 0xFF == 27):
        # esc를 치면 꺼진다.
        break
        
cv2.destroyAllWindows()