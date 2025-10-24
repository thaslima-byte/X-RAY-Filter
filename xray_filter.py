import cv2
import matplotlib.pyplot as plt

# Read the X-ray image
image = cv2.imread('images.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image loaded correctly
if image is None:
    print("Error: Image not found. Check your path or filename.")
    exit()

# Apply median filtering
median_filtered = cv2.medianBlur(image, 5)  # kernel size = 5 (you can adjust it)

# Display original vs filtered image
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original X-ray")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("After Median Filtering")
plt.imshow(median_filtered, cmap='gray')
plt.axis('off')

plt.show()
