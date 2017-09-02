import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = cv2.imread('./STOP_sign.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
