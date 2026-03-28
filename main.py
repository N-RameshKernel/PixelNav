from camera import Camera
from visual_odometry import VisualOdometry
from point_cloud import PointCloudBuilder
from utils import show_frames
import cv2

camera = Camera("dataset")
vo = VisualOdometry()
pc = PointCloudBuilder()

prev_frame = camera.get_frame()

while True:

    frame = camera.get_frame()

    if frame is None:
        break

    R, t, pts1, pts2 = vo.process(prev_frame, frame)

    pc.add_points(pts2)

    show_frames(prev_frame, frame)

    prev_frame = frame

pc.show()

cv2.destroyAllWindows()