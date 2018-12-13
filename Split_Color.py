import cv2
import numpy

# Read the image
img=cv2.imread('test_image.jpg',1)

#Save just the Red channel
img1=img.copy()
img1[:,:,1]=0
img1[:,:,2]=0

#Save just the Blue channel
img2=img.copy()
img2[:,:,0]=0
img2[:,:,2]=0

#Save just the Green channel
img3=img.copy()
img3[:,:,0]=0
img3[:,:,1]=0


# Show the images
cv2.imshow('Original Image',img)
cv2.imshow('RED',img1)
cv2.imshow('BLUE',img2)
cv2.imshow('GREEN',img3)

# Close and exit
cv2.waitKey(0) # 0 makes it wait infinitely
cv2.destroyAllWindows()
