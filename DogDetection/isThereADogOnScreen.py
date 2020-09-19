import cv2 as cv
import pyautogui
import numpy as np

t1 = 50
t2 = 150
areaMin = 2000

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = int(x)
        self.y = int(y)
        self.w = int(w)
        self.h = int(h)
        print(self)

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.w}, {self.h})'

def getBlobRectangles(img):
    # Setup SimpleBlobDetector parameters.
    params = cv.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 1
    params.maxThreshold = 500


    # Filter by Area.
    params.filterByArea = True
    params.minArea = 1000

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.1

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.87

    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.01

    # Create a detector with the parameters
    detector = cv.SimpleBlobDetector_create(params)

    keypoints = detector.detect(img)
    print(keypoints)

    for keypoint in keypoints:
        print(keypoint.pt)
        print(keypoint.size)

    return [Rectangle(point.pt[0], point.pt[1], point.size, point.size) for point in keypoints]

def getCountourRectangles(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    rectangles = []
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > areaMin:
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            x , y , w, h = cv.boundingRect(approx)
            if w > h *3 or h > w* 3:
                continue
            rectangles.append(Rectangle(x, y, w, h))
    return rectangles

def crop(img, rectangle):
    return img[rectangle.y:rectangle.y + rectangle.h, rectangle.x:rectangle.x + rectangle.w]

def isThereADogOnScreen():
    screenshot_pil = pyautogui.screenshot()
    screenshot_cv = np.array(screenshot_pil)[:, :, ::-1].copy()

    imgBlur = cv.GaussianBlur(screenshot_cv, (7, 7), 1)
    imgGray = cv.cvtColor(imgBlur, cv.COLOR_BGR2GRAY)
    imgCanny = cv.Canny(imgGray, t1, t2)
    kernel = np.ones((5, 5))
    imgDil = cv.dilate(imgCanny, kernel, iterations=1)
    rectangles = getCountourRectangles(imgDil) + getBlobRectangles(imgBlur)

    print(rectangles)

    i = 0
    for rectangle in rectangles:
        cv.imshow(f'{i}', crop(screenshot_cv, rectangle))
        i += 1

    while True:
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
def main():
    isThereADogOnScreen()

if __name__ == '__main__':
    main()
