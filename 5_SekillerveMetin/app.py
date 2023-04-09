import cv2 as cv
import numpy as np

# resim oluştur.
img = np.zeros((512,512,3), np.uint8) # siyaf görüntü. 
print(img)
print(img.ndim)
print(img.shape)

cv.imshow("Siyah",img)

# çizgi
    # (resim, başlangıç noktası, bitiş noktası, renk, kalınlık)
    # openCV'de renk RGB değil BGR olarak alınır.
cv.line(img,(0,150), (512,512), (0,255,0), 3)
cv.imshow("Cizgi",img)  

# dikdörtgen/kare
    # (resim, başlangıç noktası, bitiş noktası, renk)
cv.rectangle(img, (0,0), (256,256), (255,0,0)) # son parametreye cv.FILLED yazıldığında dikdörtgenin içini doldurur.
cv.imshow("Dikdortgen",img)

# çember
    # (resim, başlangıç noktası, yarıçap, renk)
cv.circle(img, (300,300), 45, (0,0,255)) # son parametreye cv.FILLED yazıldığında çemberin içini doldurur..
cv.imshow("Cember",img)

# metin
    # (resim, yazılacak text, konum, font, boyut, renk)
cv.putText(img, "Image Processing", (100,100), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv.imshow("Metin",img)

cv.waitKey(0)
cv.destroyAllWindows()