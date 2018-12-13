import cv2
import numpy

# Read the image
img=cv2.imread('Lion.jpg')
h,w,c=img.shape
img1=img[:,:int(w/2),:]
img2=img[:,int(w/2):,:]
img3=img[int(h/2):,:int(w/2),:]
img4=img[:int(h/2),int(w/2):,:]

# Show the images
cv2.imshow('Left Half',img1)
cv2.imshow('Right Half',img2)
cv2.imshow('Bottom Left Half',img3)
cv2.imshow('Top Right Half',img4)

# Close and exit
'''Wait for user to press button to exit: cv2.waitKey(<time in ms>)'''
cv2.waitKey(0) # 0 makes it wait infinitely
'''Close all windows'''
cv2.destroyAllWindows()
