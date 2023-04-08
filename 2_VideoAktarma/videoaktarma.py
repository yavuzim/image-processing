import cv2 as cv
import time

# video ismi.
video_name = "MOT17-04-DPM.mp4"

# video içe aktar. capture,cap
cap = cv.VideoCapture(video_name)

# get fonksiyonunun 3.indeksi videonun genişliğini verir.
print("Genislik : ",cap.get(3)) 
# get fonksiyonunun 4.indeksi videonun yüksekliğini verir.
print("Yükseklik : ",cap.get(4)) 

# video açılmazsa hata mesajı verir.
if cap.isOpened() == False:
    print("Hata")
    
while cap.isOpened():
    _return, frame = cap.read()  
    if _return == True:
        time.sleep(0.01) # kullanmazsak çok hızlı akar.
        cv.imshow("Video",frame)
        if cv.waitKey(1) == ord("q"):
            break
    else: break    

cap.release() # stop capture.

cv.destroyAllWindows()