import cv2
import numpy as np

class VisualOdometry:

    def __init__(self):
        self.orb = cv2.ORB_create(2000)
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    def process(self, img1, img2):

        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        kp1, des1 = self.orb.detectAndCompute(gray1, None)
        kp2, des2 = self.orb.detectAndCompute(gray2, None)

        if des1 is None or des2 is None:
            return None, None, [], []

        matches = self.bf.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)

        pts1 = np.float32([kp1[m.queryIdx].pt for m in matches])
        pts2 = np.float32([kp2[m.trainIdx].pt for m in matches])

        if len(pts1) < 8:
            return None, None, pts1, pts2

        E, mask = cv2.findEssentialMat(
            pts1, pts2,
            focal=718.8560,
            pp=(607.1928,185.2157),
            method=cv2.RANSAC,
            prob=0.999,
            threshold=1.0
        )

        if E is None:
            return None, None, pts1, pts2

        _, R, t, mask = cv2.recoverPose(E, pts1, pts2)

        return R, t, pts1, pts2