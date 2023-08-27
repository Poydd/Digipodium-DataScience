import cv2

# basic 


CAM_IDX = 0
cv2.namedWindow('Canny')
cam = cv2.VideoCapture(CAM_IDX)

lowthreshold = cv2.createTrackbar('Low Threshold', 'canny', 0, 1000,lambda x:None)
highthreshold = cv2.createTrackbar('High Threshold', 'canny', 0, 1000,lambda x:None)
while cam.isOpened():
    state, img = cam.read()
    if not state:
        print('camera is not available')
        break
    #basic filter
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 2D
    im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 3D
    # adv filter
    lt = cv2.getTrackbarPos('Low Threshold', 'canny')
    ht = cv2.getTrackbarPos('High Threshold', 'canny')
    im_canny = cv2.Canny(img, 100, 150)
    im_sobel = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)
    cv2.imshow('original',img)
    cv2.imshow('gray', im_gray)
    cv2.imshow('rgb', im_rgb)
    cv2.imshow('Canny', im_canny)
    cv2.imshow('canny',im_canny)
    cv2.imshow('sobel',im_sobel)

    key=cv2.waitKey(10)
    if key == ord('q'):
        break
cv2.destroyAllWindows()
cam.release()