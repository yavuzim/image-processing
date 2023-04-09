import cv2 as cv
import matplotlib.pyplot as plt

img1 = cv.imread("img1.jpg")
img2 = cv.imread("img2.jpg")

# BGR formatını RGB yapma.
img1 = cv.cvtColor(img1,cv.COLOR_BGR2RGB)
img2 = cv.cvtColor(img2,cv.COLOR_BGR2RGB)

print(img1.shape)
print(img2.shape)

# Resimlerin boyutlarını eşitleme.
img1 = cv.resize(img1,(600,600))
img2 = cv.resize(img2,(600,600))

print(img1.shape)
print(img2.shape)

# Resimleri plots'da gösterme.
plt.figure()
plt.imshow(img1)
plt.figure()
plt.imshow(img2)

# Karıştılmış resim = alpha*img1 + beta*img2
blended = cv.addWeighted(src1 = img1, alpha = 0.5, src2 = img2, beta = 0.5, gamma = 0)
plt.figure()
plt.imshow(blended)

# Karıştılmış resmi kaydetme.
cv.imwrite("karistirilmis_resim.png",blended)



cv.waitKey(0)
cv.destroyAllWindows()