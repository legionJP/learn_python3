# Import necessary libraries
import cv2

# Load image
img = cv2.imread('jp_Image.PNG')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create binary image
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)


# Find contours in binary image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on a black background and fill with white color to create a mask
mask = np.zeros(img.shape[:2], dtype=np.uint8)
for cnt in contours:
    cv2.drawContours(mask, [cnt], 0, (255), -1)

# Apply the mask on the original image to erase the background 
result = cv2.bitwise_and(img,img,mask=mask)

# Display result 
cv2.imshow("Original Image", img)
cv2.imshow("gray Image", gray)

cv2.waitKey(0)

cv2.destroyAllWindows()