import math
import numpy as np
import time
import cv2 as cv

#def TF_fo(dtime, input, output):
T = 0.1
K = 1
U = 0
V = 0
Load = 0
time_counter = 0
delta_time = 0

W = 1000
size = W, W+900, 3
rook_image = np.zeros(size, dtype=np.uint8)
rook_window = "Drawing 1: Rook"
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


    time_counter += delta_time
    V = ((U-V)*1/T*delta_time-Load)+V
    U = 1  
    time.sleep(0.01)
    delta_time = time.time() - start_time
    if time_counter >= 1.3:
        Load = 0
    else:
        if time_counter>=0.7:
            Load = 0.01
        else:
            if time_counter>0:
                Load = 0

    my_line(rook_image, (int(900*time_counter), W-int(800*V)), (int(900*(time_counter+delta_time)), W-int(800*V)))
    print(V, time_counter)
    cv.imshow(rook_window, rook_image)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
    if time_counter > 2:
        break
