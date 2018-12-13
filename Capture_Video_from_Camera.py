import cv2
import numpy

# Initialise camera
cap= cv2.VideoCapture(0)
while(1):
    ret,frame=cap.read() # Read the image
    cv2.imshow('Video',frame) # Show the images

    if (cv2.waitKey(1)==27):  #Break if esc was pressed
        break

# Close and exit
'''Release the camera'''
cap.release()
cv2.destroyAllWindows()
