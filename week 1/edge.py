'''import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('C:/Users/Kumar/OneDrive/Desktop/Brain Spy/week 1/mario.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray)
plt.show()'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

def sobel_edge_detector(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    threshold = 200
    edges = magnitude > threshold

    return edges

image_path = 'C:/Users/Kumar/OneDrive/Desktop/Brain Spy/week 1/pikachu.png'
edge_image = sobel_edge_detector(image_path)

original_image = cv2.imread(image_path)
original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(original_image_rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(edge_image, cmap='gray')
plt.title('Edge-detected Image (Sobel)')
plt.axis('off')

plt.show()