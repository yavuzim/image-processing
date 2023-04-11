# opencv kütüphanesini içe aktaralım
import cv2 as cv

# matplotlib kütüphanesini içe aktaralım
import matplotlib.pyplot as plt

# resmi siyah beyaz olarak içe aktaralım
img = cv.imread("animals.jpg",0)

# resmi çizdirelim
cv.imshow("Orijinal",img)

# resmin boyutuna bakalım
imgSize = img.shape
print(imgSize)

# resmi 4/5 oranında yeniden boyutlandıralım ve resmi çizdirelim
n = img.shape
imgReSized = cv.resize(img, (int(n[0]*4/5), int(n[1]*4/5)))
print(imgReSized.shape)
cv.imshow("Yeniden Boyutlandırma",imgReSized)

# orjinal resme bir yazı ekleyelim mesela "kopek" ve resmi çizdirelim
cv.putText(img, "Kopek", (50,50), cv.FONT_HERSHEY_COMPLEX, 2, (0,0,0))
cv.imshow("Metin",img)

#  orjinal resme 50 threshold değeri üzerindekileri beyaz yap altındakileri siyah yapalım, 
# binary threshold yöntemi kullanalım ve resmi çizdirelim
_,img_thresh = cv.threshold(img, thresh = 50, maxval = 255, type = cv.THRESH_BINARY)
cv.imshow("THRESHOLD",img_thresh)

# orjinal resme gaussian bulanıklaştırma uygulayalım ve resmi çizdirelim
img_gauss = cv.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
cv.imshow("Gauss",img_gauss)

# orjinal resme Laplacian  gradyan uygulayalım ve resmi çizdirelim
img_lap1 = cv.Laplacian(img, ddepth = cv.CV_64F)
img_lap2 = cv.Laplacian(img, ddepth = cv.CV_64F, ksize = 5)
cv.imshow("Laplacian1",img_lap1),cv.imshow("Laplacian2",img_lap2)

# orijinal resmin histogramını çizdirelim
img_hist = cv.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(img_hist)

cv.waitKey(0)
cv.destroyAllWindows()