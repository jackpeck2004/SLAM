import cv2
import numpy as np

W, H = 1920//2, 1080//2
orb = cv2.ORB_create()

def processFrame(frame):

    frame = cv2.resize(frame, (W, H))

    # add grey filter to the frame
    gFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # kp = orb.detect(gFrame, None)

    kp, des = orb.detectAndCompute(frame, None)
    for p in kp:
        u, v = map(lambda x: int(round(x)), p.pt)

    frame2 = cv2.drawKeypoints(frame, kp, None, color=(0, 255, 0), flags=0)
    
    # return frame
    return frame2
    # return frame

    
