import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("img1.jpg")

# Resmi gri formata çevir.
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")

# eşikleme.
# THRESH_BINARY : 60'ın altındaki tüm değerler 0 (siyah), üstündeki değerler 255 (beyaz) yap.
# THRESH_BINARY_INV : Tam tersi.
_,thresh_img = cv.threshold(img, thresh = 60, maxval = 255, type = cv.THRESH_BINARY)

plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")

# uyarlamalı eşik.
# 8 C sabiti. 11 blok size.
thresh_img2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 8)

plt.figure()
plt.imshow(thresh_img2, cmap = "gray")
plt.axis("off")

