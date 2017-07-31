import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

nx = 8
ny = 4

fname = 'calibration_test.png'
img = cv2.imread(fname)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret , corners = cv2.findChessboardCorners(gray, (nx, ny), None)

print(ret)
if ret == True:
    cv2.drawChessboardCorners(img, (nx, ny), corners, ret)
    plt.imshow(img)
    plt.show()
