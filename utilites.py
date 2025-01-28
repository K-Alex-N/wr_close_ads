import cv2 as cv

from adb import tap


def last_screenshot():
    return "images/screenshots/1737918907.3581278.png"


class ImageComparison:

    def __init__(self, target_path, img_path=last_screenshot()):
        self.target = cv.imread(target_path, 0)
        self.img = cv.imread(img_path, 0)
        self.target_w: int = self.target.shape[1]
        self.target_h: int = self.target.shape[0]
        self.img_w: int = self.img.shape[1]
        self.img_h: int = self.img.shape[0]
        self.top_left_target_coords = None

    def save_top_left_target_coords(self, top_left):
        self.top_left_target_coords = top_left

    # def is_target_on_image(self, threshold=0.9, method=cv.TM_CCOEFF_NORMED):
    def is_target_on_image(self):
        result = cv.matchTemplate(self.img, self.target, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        threshold = 0.9
        if max_val >= threshold:
            self.save_top_left_target_coords(max_loc)
            print("detected !!!")
            return True
        print("not found")
        return False

    def get_target_center_coords(self):
        # Х = коорд левой точки + половина ширины таргета
        x, y = self.top_left_target_coords
        print(x + self.target_w / 2, y + self.target_h / 2)
        return x + self.target_w / 2, y + self.target_h / 2

    def tap_on_target(self):
        # self.show_found_object()
        x, y = self.get_target_center_coords()
        tap(x, y)

    def reduce_img_by_2_times(self):
        return cv.resize(self.img, (self.img_w // 2, self.img_h // 2))

    def show_found_object(self):
        bottom_right_target_coords = (
            self.top_left_target_coords[0] + self.target_w,
            self.top_left_target_coords[1] + self.target_h
        )
        cv.rectangle(self.img,
                     self.top_left_target_coords,
                     bottom_right_target_coords,
                     255, 2)

        resized_img = self.reduce_img_by_2_times()
        cv.imshow('Detected Point', resized_img)
        cv.waitKey(0)
        cv.destroyAllWindows()
