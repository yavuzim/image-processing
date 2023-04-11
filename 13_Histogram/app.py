import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("red_blue.jpg")
img_vis = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img_vis)

print(img.shape)

# channels renkli mi siyah beyaz mı onu belirler.
img_hist = cv.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
print(img_hist.shape)
plt.figure(), plt.plot(img_hist)

color = ("b", "g", "r")
plt.figure()
for i,c in enumerate(color):
    hist = cv.calcHist([img], channels = [i], mask = None, histSize = [256], ranges = [0,256])
    plt.plot(hist, color = c)
    
########################################################################################################
    
golden_gate = cv.imread("goldenGate.jpg")
golden_gate = cv.cvtColor(golden_gate, cv.COLOR_BGR2RGB)
plt.figure(), plt.imshow(golden_gate)

print(golden_gate.shape)

mask = np.zeros(golden_gate.shape[:2], np.uint8)
plt.figure(), plt.imshow(mask, cmap = "gray")

mask[1500:2000,1000:2000] = 255
plt.figure(), plt.imshow(mask, cmap = "gray")

masked_img_vis = cv.bitwise_and(golden_gate, golden_gate, mask = mask)
plt.figure(), plt.imshow(masked_img_vis, cmap = "gray")

masked_img = cv.bitwise_and(golden_gate, golden_gate, mask = mask)
# renk formatını RGB yaptık channels = [0] kırmızı, channels = [1] yeşil, channels = [2] maviyi verir.
masked_img_hist = cv.calcHist([golden_gate], channels = [0], mask = mask, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(masked_img_hist)

# Histogram eşitleme. Kontrastı(karışıklık) arttırmayı sağlar.
img = cv.imread("hist_equ.jpg",0)
plt.figure(), plt.imshow(img, cmap = "gray")

# Resim siyah beyaz olduğundan channels 0 olmak zorunda. 
img_hist = cv.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(img_hist)

eq_hist = cv.equalizeHist(img)
plt.figure(), plt.imshow(eq_hist, cmap = "gray")