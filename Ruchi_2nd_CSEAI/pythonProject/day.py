import cv2
import numpy as np

framewidth = 640
frameheight = 480
cap = cv2.VideoCapture(2)
cap.set(3, framewidth)
cap.set(4, frameheight)
def empty(x):
    pass
cv2.namedWindow("parameters")
cv2.createTrackbar("threshold1","parameters",100,255,empty)
cv2.createTrackbar("threshold2","parameters",200,255,empty)

def get_contours(img_dilate,img_contours):
    contours,heirarchy=cv2.findContours(img_dilate,cv2.RETR_EXTERNAL,CV)
    for cnt in contours:
        area_min = cv2.contourArea(cnt)
        cv2.drawContours(img_contours, cnt, -1, (0, 255, 0), 3)
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        x, y, w, h = cv2.boundingRect(approx)
        cv2.rectangle(img_contours, (x, y), (x + w, y + h), (255, 0, 255), 3)
        cv2.putText(img_contours, "Points" + str(len(approx)), (x, y), (x + w, y + h), cv2.FONT_HERSHEY_COMPLEX, 0.7,
              (255, 0, 255), 2, 0)
        cv2.putText(img_contours, 'Area:' + str(int(area_min)), (x + w + 45, y + h + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                    (0, 0, 255), 2, 0)



while True:
    ret, img = cap.read()
    img_contours=img.copy()
    img_blur = cv2.GaussianBlur(img, (7, 7), 6)
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    t1=cv2.getTrackbarPos("threshold1","parameters")
    t2 = cv2.getTrackbarPos("threshold2", "parameters")
    img_canny = cv2.Canny(img_grey, 100, 200)
    # cv2.imshow("Blur_Image", img_blur)
    # cv2.imshow("Image", img)
    # output = np.hstack([img, img_blur, img_grey])
    output = np.hstack([img_grey, img_canny])
    cv2.imshow("Output", output)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()