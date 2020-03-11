#!/usr/bin/env python3
import cv2
import numpy as np

from Utils.processFrame import processFrame

img = cv2.imread('rec.jpg')

img = processFrame(img)

cv2.imshow('Slam', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
