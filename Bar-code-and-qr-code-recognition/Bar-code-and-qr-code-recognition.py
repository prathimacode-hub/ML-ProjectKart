import cv2
import numpy as np
# this will help in finding qr code and giving message
from pyzbar.pyzbar import decode
#img = cv2.imread('')

capture = cv2.VideoCapture(0)
capture.set(3, 720)
capture.set(4, 540)
while True:
    success, img = capture.imread()
    for barcode in decode(img):
        # print(barcode.data)
        # converting into string
        data1 = barcode.data.decode('utf-8')
        print(data1)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines([img], pts, True, (255, 0, 255), 4)
        pts2 = barcode.rect
        cv2.putText(img, data1, (pts2[0], pts2[1]), 0.9, (255, 0, 255), 2)

    cv2.imshow(img)
    cv2.waitKey(1)
