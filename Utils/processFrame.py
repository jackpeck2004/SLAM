import cv2
from .FeatureExtractor import FeatureExtractor
W, H = 1920//2, 1080//2
orb = cv2.ORB_create()

fe = FeatureExtractor()

def processFrame(frame):

    frame = cv2.resize(frame, (W, H))

    # add grey filter to the frame
    # gFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    kp = fe.extract(frame)

    for f in kp:
        u, v = map(lambda x: int(round(x)), f[0])
        cv2.circle(frame, (u,v), radius=3, color=(0,255,0))
        

    # frame = cv2.drawKeypoints(frame, kp, None, color=(0, 255, 0), flags=0)
    
    # return frame
    return frame
    # return frame

    
