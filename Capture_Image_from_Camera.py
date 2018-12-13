import cv2
import numpy

# Initialise camera
cap= cv2.VideoCapture(0)

# Read the image
ret,frame=cap.read()

# Show the images
cv2.imshow('Image 1',frame)

# Save the image
cv2.imwrite('From Camera.jpg',frame)

# Close and exit
'''Release the camera'''
cap.release()
cv2.waitKey(3000)
cv2.destroyAllWindows()
