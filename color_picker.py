# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 21:21:03 2022

@author: hanna
"""
import numpy as np
import cv2

def create_image(): 
    arr = np.array([[i, 255, 255] for i in range(180)])
    one = arr.reshape(1, 180, 3)
    one = one.astype(np.uint8)
    resized = cv2.resize(one, (180*5, 800), interpolation = cv2.INTER_AREA)
    rgb = cv2.cvtColor(resized, cv2.COLOR_HSV2BGR)
    return rgb

def convert_colors(color):
    

def click_event(event, x, y, flags, params):
        
    if event == cv2.EVENT_RBUTTONDOWN:
        output[:] = clean[:]
        cv2.imshow('output', output)

 
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        color = output[y, x]
        color_rgb = np.squeeze(cv2.cvtColor(np.array([[color]]), cv2.COLOR_BGR2RGB))
        print(color_rgb)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(output, str(color_rgb), (x,y), font,
                    1, (255, 255, 255), 2)
        cv2.imshow('output', output)
# arr = np.array([[i, 255, 255] for i in range(180)])
# # arr = [arr]
# # output = np.tile(arr, (1, 180))
# # output = np.repeat(arr, 5, axis=0)
# one = arr.reshape(1, 180, 3)
# frame = np.broadcast_to(one, (1000, 180, 3))
# frame = frame.astype(np.uint8)
# resized = cv2.resize(frame, (180*5, 800), interpolation = cv2.INTER_AREA)
# rgb = cv2.cvtColor(resized, cv2.COLOR_HSV2BGR)
# global output
clean = create_image()
output = clean.copy()
cv2.namedWindow('output')
# output = create_image()
cv2.setMouseCallback('output', click_event)

# while True:
cv2.imshow('output', output)
    # if cv2.waitKey(1) & 0xFF == ord("q"):
    #     break
cv2.waitKey(0)
cv2.destroyAllWindows()