import cv2 as cv
import numpy as np
import time

i = 0
W = 400
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FPS, 30)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 100)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 100)

ret, frame1 = cap.read()
prvs = cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,0] = 255
hsv[...,1] = 255
# Create black empty images
size = W, W, 3
rook_image = np.zeros(size, dtype=np.uint8)
rook_window = "Drawing 2: Rook"
def my_line(img, start, end):
     thickness = 2
     line_type = 8
     cv.line(img,
              start,
              end,
              (255, 0, 0),
              thickness,
              line_type)
def my_line_red(img, start, end):
     thickness = 2
     line_type = 8
     cv.line(img,
              start,
              end,
              (255, 255, 0),
              thickness,
              line_type)

while True:
    start_time = time.time()
    ret, frame2 = cap.read()
    
    
    next = cv.cvtColor(frame2,cv.COLOR_BGR2GRAY)
    
    
    flow = cv.calcOpticalFlowFarneback(prvs,next, None, 0.5, 1, 15, 1, 5, 1.2, 0)
    
    #mag, ang = cv.cartToPolar(flow[...,0], flow[...,1])
    #hsv[...,2] = ang*180/np.pi/2
    #hsv[...,2] = cv.normalize(mag,None,100,255,cv.NORM_MINMAX)
    #bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
    #cv.imshow('frame2',bgr)
    #a = np.ma.array(flow[...,1])
    dvx = -np.ma.average(flow[...,0])
    dvy = -np.ma.average(flow[...,1])
    my_line(rook_image, (200, 200), (200+int((500*dvx)//10), 200+int((500*dvy)//10)))
    my_line(rook_image, (200, 200), (200, 200+int((500*dvy)//10)))
    my_line_red(rook_image, (200, 200), (200+int((500*dvx)//10), 200))
    if i>1:
        
        rook_image = np.zeros(size, dtype=np.uint8)
        cv.imshow(rook_window, rook_image)
        i=0
    cv.imshow(rook_window, rook_image)
    #cv.moveWindow(rook_window, W, 200)
    i+=1
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('s'):
        cv.imwrite('opticalfb.png',frame2)
        cv.imwrite('opticalhsv.png',bgr)
    prvs = next
    delta_time = time.time() - start_time
    print(dvy, delta_time)
    
cap.release()
cv.destroyAllWindows()