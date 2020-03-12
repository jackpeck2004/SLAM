import cv2
import numpy as np

X, Y = 1920, 1080

def processFrame(frame):

    # black blank image
    frame2 = np.zeros(shape=[Y, X, 3], dtype=np.uint8)
    
    # add grey filter to the frame
    gFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # define the threshold
    ret, thresh = cv2.threshold(gFrame, 127, 255, 0)

    # find contours
    # cont, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # print(len(cont))

    # draw contours
    # cv2.drawContours(frame2, cont, -1, (0, 255, 0), 3)
    # print(cont)

    # draw corners
    corners = cv2.goodFeaturesToTrack(gFrame,255,0.01,0)

    corners = np.int0(corners)
   
    # black blank image

    
    for i in corners:
        x,y = i.ravel()
        cv2.circle(frame2,(x,y),3,255,-1)
    
    # apply gaussian blur
    # bluredFrame = cv2.GaussianBlur(frame, (7,7),1)
    # greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # return frame
    return frame2, corners
    # return frame

    
