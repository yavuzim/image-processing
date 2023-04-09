import cv2 as cv
import numpy as np

img = cv.imread("lenna.png")

cv.imshow("Orijinal",img)

# yatay birleştirme (horizontal)
horizontalImg = np.hstack((img,img))

cv.imshow("Horizontal",horizontalImg)

# dikey birleştirme (vertical)
verticalImg = np.vstack((img,img))

cv.imshow("Vertical",verticalImg)

cv.waitKey(0)
cv.destroyAllWindows()