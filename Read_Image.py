import cv2
import numpy

# Read the image
'''<img_object_name>=cv2.imread(<Filename>)'''
img1=cv2.imread('Images/Lion.jpg')
img2=cv2.imread('Images/LionBMP.jpg')


# Show the images
'''cv2.imshow(,Filename>,<img_object_name>)'''
cv2.imshow('Image 1',img1)
cv2.imshow('Image 2',img2)

# Close and exit
'''Wait for user to press button to exit: cv2.waitKey(<time in ms>)'''
cv2.waitKey(0) # 0 makes it wait infinitely
'''Close all windows'''
cv2.destroyAllWindows()
