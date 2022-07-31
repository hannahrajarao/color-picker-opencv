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
    resized = cv2.resize(one, (180*5, 100), interpolation = cv2.INTER_AREA)
    rgb = cv2.cvtColor(resized, cv2.COLOR_HSV2BGR)
    return rgb

def convert_colors(color):
    pass
    

def pick_hue(event, x, y, flags, params):
        
    if event == cv2.EVENT_RBUTTONDOWN:
        hues[:] = clean[:]
        cv2.imshow('hues', hues)

 
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        color = hues[y, x]
        color_rgb = np.squeeze(cv2.cvtColor(np.array([[color]]), cv2.COLOR_BGR2RGB))
        print(color_rgb)
 
        # displaying the coordinates
        # on the image window
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.putText(hues, str(color_rgb), (x,y), font,
        #             1, (255, 255, 255), 2)
        cv2.imshow('hues', hues)
        color_hue = np.squeeze(cv2.cvtColor(np.array([[color]]), cv2.COLOR_BGR2HSV))
        sv_array[:, :, 0] = color_hue[0]
        sv_display[:] = cv2.cvtColor(sv_array, cv2.COLOR_HSV2BGR)
        cv2.imshow('saturation and values', sv_display)

def pick_color(event, x, y, flags, params):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        color = sv_display[y, x]
        final_color[:, :] = color
        cv2.imshow('color', final_color)
        print('hsv', np.squeeze(cv2.cvtColor(np.array([[color]]), cv2.COLOR_BGR2HSV)))
    


clean = create_image()
hues = clean.copy()
cv2.namedWindow('hues')
cv2.namedWindow('saturation and values')
cv2.namedWindow('color')
# hues = create_image()
cv2.setMouseCallback('hues', pick_hue)
cv2.setMouseCallback('saturation and values', pick_color)


sv_array = np.array([[[0, s, v] for v in range(255)] for s in range(255)], dtype=np.uint8)
sv_display = cv2.cvtColor(sv_array, cv2.COLOR_HSV2BGR)
final_color = np.zeros((255, 255, 3), dtype=np.uint8)
# final_color = final_color.fill([0, 0, 0])

# while True:
cv2.imshow('hues', hues)
cv2.imshow('saturation and values', sv_display)
cv2.imshow('color', final_color)
    # if cv2.waitKey(1) & 0xFF == ord("q"):
    #     break
cv2.waitKey(0)
cv2.destroyAllWindows()