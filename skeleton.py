import cv2
import os

def get_file():
    for file in os.listdir('.'):
        if file.endswith('.avi'):
            return file

def annotate_records():
    pass

def pick_category():
    pass

def classify_on_records():
    pass

def save_model():
    pass

def test_model():
    pass


if __name__ == '__main__':
    file = get_file()
    print file
    #cv2.namedWindow(file)
    cap = cv2.VideoCapture(file)

    orb = cv2.ORB_create()

    while True:
        ret, img = cap.read()
        if ret:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            kp = orb.detect(img, None)
            kp, des = orb.compute(img, kp)
            img2 = cv2.drawKeypoints(img, kp, img, color=(0, 255, 0), flags=0)
            print img2.shape
            cv2.imshow('image', img2)
            k = cv2.waitKey(100) & 0xFF
            if k == ord('q'):
                break
        else:
            break