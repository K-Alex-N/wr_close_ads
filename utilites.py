import cv2 as cv


def last_screenshot():
    pass


class ImageComparison:

    def __init__(self, target_path, img_path=last_screenshot()):
        self.target = cv.imread(target_path, 0)
        # self.img = cv.imread(img_path, 0)
        self.img = cv.imread("images/screenshots/1737918907.3581278.png", 0)
        self.target_w = self.target.shape[1]
        self.target_h = self.target.shape[0]

        self.target_top_left_coords = None

    def save_target_coords(self, top_left):
        self.target_top_left_coords = top_left

    # def is_target_on_image(self, threshold=0.9, method=cv.TM_CCOEFF_NORMED):
    def is_target_on_image(self):
        result = cv.matchTemplate(self.img, self.target, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        threshold = 0.9
        if max_val >= threshold:
            self.save_target_coords(max_loc)
            return True
        return False

    def find_target_center_on_img(self):
        # Х = коорд левой точки + половина ширины таргета
        pass

    def tap_on_target(self):
        w, h = self.find_cord_of_target_on_img()
