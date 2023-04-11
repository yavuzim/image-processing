import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("sudoku.jpg", 0)

plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("Orijinal")

# x gradyan.
sobelX = cv.Sobel(img, ddepth = cv.CV_16S, dx = 1, dy = 0, ksize = 5)
plt.figure(), plt.imshow(sobelX, cmap = "gray"), plt.axis("off"), plt.title("X Gradyan")

# y gradyan.
sobelY = cv.Sobel(img, ddepth = cv.CV_16S, dx = 0, dy = 1, ksize = 5)
plt.figure(), plt.imshow(sobelY, cmap = "gray"), plt.axis("off"), plt.title("Y Gradyan")

# laplacian gradyan.(x-y)
lap = cv.Laplacian(img, ddepth = cv.CV_16S)
plt.figure(), plt.imshow(lap, cmap = "gray"), plt.axis("off"), plt.title("Laplacian")