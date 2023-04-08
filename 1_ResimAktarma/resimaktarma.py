import cv2 as cv

# İçe aktarma.
img = cv.imread("messi5.jpg",0) # İkinci parametre 0 olursa resim siyah beyaz, 1 olursa renkli olarak içe aktarır.

# görselleştir.
cv.imshow("Ilk Resim",img)

k = cv.waitKey(0) &0xff

# 27 sayısı klavyedeki esc tuşunun sayısal karşılığıdır.
if k == 27:  # esc tuşuna basılırsa pencere kapanacak.
    cv.destroyAllWindows()
elif k == ord("s"): # s tuşuna basılırsa resmi png formatında kaydedecek ve pencere kapanacak.
    cv.imwrite("messi_gray.png",img)
    cv.destroyAllWindows()