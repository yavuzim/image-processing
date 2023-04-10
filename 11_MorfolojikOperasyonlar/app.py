import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("datai_team.jpg", 0)

plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("Orijinal")

'''# erezyon'''
kernel = np.ones((5,5), dtype = np.uint8)
result = cv.erode(img, kernel, iterations = 1)

plt.figure(), plt.imshow(result, cmap = "gray"), plt.axis("off"), plt.title("Erezyon")

'''# genişleme (dilation)'''
result2 = cv.dilate(img, kernel, iterations = 1)

plt.figure(), plt.imshow(result2, cmap = "gray"), plt.axis("off"), plt.title("Genişleme")

'''# açılma'''

def noiseCreate(x):
    whiteNoise = np.random.randint(0,2,size = img.shape[:2])
    return whiteNoise*x    

# beyaz gürültü oluşturma.
whiteNoise = noiseCreate(255)
plt.figure(), plt.imshow(whiteNoise, cmap = "gray"), plt.axis("off")
plt.title("Beyaz Gürültülü")

noise_img = whiteNoise + img
plt.figure(), plt.imshow(noise_img, cmap = "gray"), plt.axis("off")
plt.title("Img with White Noise")

opening = cv.morphologyEx(noise_img.astype(np.float32), cv.MORPH_OPEN, kernel)

plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off")
plt.title("Acilma")



'''# kapatma '''

# siyah gürültü oluşturma
blackNoise = noiseCreate(-255)
black_noise_img = blackNoise + img
black_noise_img[black_noise_img <= -245] = 0
plt.figure(), plt.imshow(black_noise_img, cmap = "gray"), plt.axis("off")
plt.title("Siyah Gürültülü")

closing = cv.morphologyEx(black_noise_img.astype(np.float32), cv.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(closing, cmap = "gray"), plt.axis("off")
plt.title("Kapatma")

'''# gradient '''
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap = "gray"), plt.axis("off")
plt.title("Gradyan")