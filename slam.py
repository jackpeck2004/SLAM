#!/usr/bin/env python3
import cv2
import numpy as np
from Utils.processFrame import processFrame
# from Utils.plotGraph import plotGraph

# declare video file
# cap = cv2.VideoCapture('video.mp4')
cap = cv2.VideoCapture('newfile.mp4')

frameCount = 0
frames = []

# check is video can be opened
if(cap.isOpened()== False):
    print("Error oprning video stream or file")

# while video is on read
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        frameCount += 1

        # process frame using Utils/processFrame
        frame = processFrame(frame)

        # Display Frame
        cv2.imshow('Slam', frame)

        # check for window exit signal
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # when video ends exit loop
    else:
        break

# destroy window
cap.release()

# cv2.destroyAllWIndows()

