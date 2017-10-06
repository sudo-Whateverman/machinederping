import numpy as np
import cv2


def sourceCapture():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if cap.isOpened() :
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        return cap
    else:
        print "Nothing to show up for"
        return 0



if __name__ == '__main__':
    while(True):
        cap = sourceCapture()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
