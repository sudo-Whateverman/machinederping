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
    cv2.namedWindow('image')
    cap = cv2.VideoCapture(file)
    while True:
        img = cap.read()
        cv2.imshow('image', img)
        print "frame"