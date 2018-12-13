import cv2
import numpy

'''RGB to GRAY'''

# Read the image
img=cv2.imread('Lion.jpg')

# Process the image
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Show the images
cv2.imshow('Original Image',img)
cv2.imshow('Gray Image',img1)

# Close and exit
cv2.waitKey(5000) # 0 makes it wait infinitely
cv2.destroyAllWindows()

'''RGB to HSV (Hue, Saturation, Value)'''

# Read the image
img=cv2.imread('color_image.jpg')

# Process the image
img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# Show the images
cv2.imshow('Original Image',img)
cv2.imshow('HSV Image',img2)

# Close and exit
cv2.waitKey(5000) # 0 makes it wait infinitely
cv2.destroyAllWindows()


# Hue
img3=img2[:,:,0]
# Saturation
img4=img2[:,:,1]
# Value
img5=img2[:,:,2]

# Show the images
cv2.imshow('Original Image',img)
cv2.imshow('Hue',img3)
cv2.imshow('Saturation',img4)
cv2.imshow('Value',img5)

# Close and exit
cv2.waitKey(5000) # 0 makes it wait infinitely
cv2.destroyAllWindows()
