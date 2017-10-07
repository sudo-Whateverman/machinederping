import numpy as np
import cv2


class Image():
    def __init__(self):
        self.img = None
        self.source = None  # source = 0, 1; 0 is webcam, 1 is still frame

    def still(self):
        self.source = 1
        self.img = np.zeros((512, 512, 3), np.uint8)

    def webcam(self):
        self.source = 0
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if cap.isOpened():
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(gray, 'From Webcam', (10, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
            self.img = gray
        else:
            print "Nothing to show up for"   # TODO : change to log
            self.still()

    def draw_rect(self):
        if roi_is_ready:
            cv2.rectangle(self.img, left_corner, right_corner, (0, 255, 0), -1)


def point2pick():
    cv2.setMouseCallback('image', save2points)


def save2points(event, x, y, flags, param):
    global left_corner, right_corner, roi_is_ready
    if event == cv2.EVENT_LBUTTONDOWN:
        print "Mouse Button Down"  # TODO : change to log
        roi_is_ready = False
        left_corner = x, y
        print (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        roi_is_ready = True
        print "Mouse Button Up"  # TODO : change to log
        print (x, y)
        right_corner = x, y


image = Image()
roi_is_ready = False
left_corner = (0, 0)
right_corner = (0, 0)

if __name__ == '__main__':
    cv2.namedWindow('image')
    point2pick()
    source = input("Press 0 for webcam, 1 for a blank square")
    while True:
        if source == 0:
            image.webcam()
        else:
            image.still()
        image.draw_rect()
        cv2.imshow('image', image.img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
