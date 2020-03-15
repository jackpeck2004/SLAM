import cv2
import numpy as np
class FeatureExtractor:

    def __init(self):
        pass

    def extract(self, img):
        feats = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.01, minDistance=3)
        return feats
