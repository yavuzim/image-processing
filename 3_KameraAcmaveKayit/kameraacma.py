import cv2 as cv

# Kamera seçimi.
cap = cv.VideoCapture(0) # 0 parametresi default kameradır.

width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print(width,height)

# Video kaydet.
# VideoWriter_fourcc = > windows için kullanılır. Çerçeveleri sıkıştırmak için kullanılır.
# 20 -> fps. Her saniyede göreceimiz resim sayısı.
writer = cv.VideoWriter("Video_kaydi.mp4",cv.VideoWriter_fourcc(*"DIVX"),20,(width,height))

while True:
    ret,frame = cap.read()
    cv.imshow("Video",frame)
    
    # save
    writer.write(frame)
    
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
writer.release()
cv.destroyAllWindows()