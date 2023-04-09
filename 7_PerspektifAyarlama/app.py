import cv2 as cv
import numpy as np

img = cv.imread("kart.png")
cv.imshow("Orijinal",img)

width = 400
height = 500

# Çevirmek istenilen resmin köşeleri.
points1 = np.float32([[203,1],[1,472],[540,150],[338,617]])

# Elde etmek istediğimiz resmin köşeleri.
points2 = np.float32([[0,0],[0,height],[width,0],[width,height]])

matrix = cv.getPerspectiveTransform(points1,points2)
print(matrix)

# Dönüştürülmüş resim.
imgOutput = cv.warpPerspective(img,matrix,(width,height))

cv.imshow("Nihai Resim",imgOutput)

cv.waitKey(0)
cv.destroyAllWindows()