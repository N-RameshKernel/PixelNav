import cv2
import glob

class Camera:
    def __init__(self, dataset_path):
        self.images = sorted(glob.glob(dataset_path + "/*.png"))
        self.index = 0

    def get_frame(self):
        if self.index >= len(self.images):
            return None
        frame = cv2.imread(self.images[self.index])
        self.index += 1
        return frame