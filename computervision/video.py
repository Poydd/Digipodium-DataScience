import cv2

VIDEO_PATH =r"C:\Users\Dell\Downloads\video (2160p) (1).mp4"
vid = cv2.VideoCapture(VIDEO_PATH)

while True:
    status, img = vid.read()
    if not status:
        print('video  is not available')
        break
    # vision operation
    img = cv2.resize(img, None, fx=.25, fy=.25)
    cv2.imshow('video', img)  
    key = cv2.waitKey(10)  
    if key == 27:          
        break
cv2.destroyAllWindows()
vid.release()