import numpy as np
import cv2


def sourceCapture():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if cap.isOpened() :
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(gray, 'From Webcam', (10, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        return gray
    else:
        print "Nothing to show up for"
        return 0

def point2pick():
    cv2.setMouseCallback('image', draw_rectangle)


def draw_rectangle(event,x,y,flags,param):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        print "Mouse Button Down"
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            print "Mouse Dragged"
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        print "Mouse Button Up"
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)

img = np.zeros((512,512,3), np.uint8)
drawing = False
ix,iy = -1,-1

if __name__ == '__main__':
    cv2.namedWindow('image')
    point2pick()
    while(True):
        #img = sourceCapture()
        cv2.imshow('image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
