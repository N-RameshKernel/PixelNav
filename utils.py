import cv2

def show_frames(img1, img2):
    combined = cv2.hconcat([img1, img2])
    cv2.imshow("SLAM Frames", combined)
    cv2.waitKey(1)