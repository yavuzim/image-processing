import cv2 as cv

img = cv.imread("lenna.jpg",1)
print("Resim Boyutu : ",img.shape)
cv.imshow("Resim",img)

# Boyutlandırma.
imgResized = cv.resize(img,(200,200))
print("Resim Boyutu : ",imgResized.shape)
cv.imshow("Boyutlandırılmış Resim",imgResized)

# Kırpma.
imgCropped = img[80:200,:300]
print("Resim Boyutu : ",imgCropped.shape)
cv.imshow("Kirpilmis Resim",imgCropped)

cv.waitKey(0)
cv.destroyAllWindows()
