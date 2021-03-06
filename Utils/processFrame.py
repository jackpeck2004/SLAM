import cv2
from .Extractor import Extractor

W, H = 1920//2, 1080//2

fe = Extractor()

def processFrame(frame):

    frame = cv2.resize(frame, (W, H))

    # Add grey filter to the frame
    # gFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    matches = fe.extract(frame)

    ukps = []
    vkps = []

    for pt1, pt2 in matches:
        u1, v1 = map(lambda x: int(round(x)), pt1)
        u2, v2 = map(lambda x: int(round(x)), pt2)
        cv2.circle(frame, (u1,v1), radius=3, color=(0,255,0))
        cv2.line(frame, (u1, v1), (u2,v2), color=(255,0,0))

    # frame = cv2.drawKeypoints(frame, kp, None, color=(0, 255, 0), flags=0)

    # return frame
    return frame
    # return frame

