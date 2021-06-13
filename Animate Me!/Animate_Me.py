#Importing Necessary Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Reading Image and Converting into required format
img = cv2.imread("Input Image\Amy.jpg") #Change the address according to source image
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Identifying Edges
edges = cv2.Canny(imgRGB, 300, 300)

#Applying median blur to obtain edges of even density and continuity
gray = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2GRAY)
gray1 = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)

#Magic Function - Color Quantization
def color_quantization(img, k):
    data = np.float32(img).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape(img.shape)
    return result

#Quantized Image with discrete color patterns
img_1 = color_quantization(imgRGB, 7)

#Smoothening sharp region tranistion
blurred = cv2.medianBlur(img_1, 5)

#Finally, Adding the Edges to complete the cartoonification
cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
cv2.imshow("Cartoon Output", cartoon)
cv2.waitKey()
fileName = "Output Image/AmyOP.jpeg" #insert desired image name here
cv2.imwrite(fileName, cartoon)