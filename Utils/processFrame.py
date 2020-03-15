import cv2
import numpy as np

W, H = 1920//2, 1080//2
orb = cv2.ORB_create()

class FeatureExtractor:

    def __init(self):
        pass

    def extract(self, img):
        feats = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.01, minDistance=3)
        return feats

fe = FeatureExtractor()

def processFrame(frame):

    frame = cv2.resize(frame, (W, H))

    # add grey filter to the frame
    # gFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # kp = orb.detect(gFrame, None)

    # kp, des = orb.detectAndCompute(frame, None)
    # for p in kp:
    #     u, v = map(lambda x: int(round(x)), p.pt)
    #     cv2.circle(frame, (u,v), radius=3, color=(0,255,0))


    kp = fe.extract(frame)

    for f in kp:
        u, v = map(lambda x: int(round(x)), f[0])
        cv2.circle(frame, (u,v), radius=3, color=(0,255,0))
        

    # frame = cv2.drawKeypoints(frame, kp, None, color=(0, 255, 0), flags=0)
    
    # return frame
    return frame
    # return frame

    
