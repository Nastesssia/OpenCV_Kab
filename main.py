import cv2
import numpy as np

# Загрузка изображения
image = cv2.imread('stone.jpg')

# Определение размеров изображения
height, width = image.shape[:2]

# Создание чёрного круглого маскирующего изображения
mask = np.zeros((height, width), dtype=np.uint8)
center = (width // 2, height // 2)
radius = min(width, height) // 2
cv2.circle(mask, center, radius, (255), -1)

# Применение маски к изображению
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Original Image', image)
cv2.imshow('Circular Mask', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
