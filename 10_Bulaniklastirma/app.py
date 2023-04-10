import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore")

# bluring (detayı azaltır ve gürültüyü engeller)
img = cv.imread("NYC.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("Orijinal")

'''
    Ortalama bulanıklaştırma yöntemi
'''
dst2 = cv.blur(img, ksize = (3,3))
plt.figure(), plt.imshow(dst2), plt.axis("off"), plt.title("Ortalama Bulanıklaştırma")

'''
    Gauss bulanıklaştırma yöntemi
'''
gb = cv.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
plt.figure(), plt.imshow(gb), plt.axis("off"), plt.title("Gauss Bulanıklaştırma")

'''
    Medyan bulanıklaştırma yöntemi
'''
mb = cv.medianBlur(img, ksize = 3)
plt.figure(), plt.imshow(mb), plt.axis("off"), plt.title("Medyan Bulanıklaştırma")


'''
    Gauss blur ile noisy (gürültü) azaltma.
'''

def gaussianNoise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    
    gauss = np.random.normal(mean, sigma, (row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    
    return noisy

# içe aktar ve normalize et. 
    # normalize : 0-255 arası değerleri 0-1 arasında yapar.
img = cv.imread("NYC.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)/255

plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("Orijinal")

gaussianNoisyImg = gaussianNoise(img)
plt.figure(), plt.imshow(gaussianNoisyImg), plt.axis("off"), plt.title("Guss Noisy")

# gauss blur
gb2 = cv.GaussianBlur(gaussianNoisyImg, ksize = (3,3), sigmaX = 7)
plt.figure(), plt.imshow(gb2), plt.axis("off"), plt.title("With Gauss Bulanıklaştırma")


'''
    Tuz-Karabiber gürültüsünü medyan blur ile azaltma.
'''
def saltPapperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5
    
    amount = 0.004
    
    noisy = np.copy(image)
    
    # salt (beyaz noktacık)
    num_salt = int(np.ceil(amount * image.size * s_vs_p))
    coords = [np.random.randint(0,i-1, num_salt) for i in image.shape]
    noisy[coords] = 1 
    
    # pepper (siyah noktacık)
    num_pepper = int(np.ceil(amount * image.size * (1-s_vs_p)))
    coords = [np.random.randint(0,i-1, num_salt) for i in image.shape]
    noisy[coords] = 10
    
    return noisy

spImage = saltPapperNoise(img)
plt.figure(), plt.imshow(spImage), plt.axis("off"), plt.title("SP Image")

mb2 = cv.medianBlur(spImage.astype(np.float32), ksize = 3)
plt.figure(), plt.imshow(mb2), plt.axis("off"), plt.title("with Medyan Bulanıklaştırma")