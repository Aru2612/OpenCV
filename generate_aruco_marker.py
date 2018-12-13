import numpy as np
import math
import cv2
import cv2.aruco as aruco

# DICT_<Bit size>X<Bit size>_<Number of IDs>
'''In general, Lower Bit sizes and higher number of combinations increase the inter-marker
distance and vice-versa.'''
# If Number of IDs is n the marker ids can be from 0 to n-1
aruco_dict=aruco.Dictionary_get(aruco.DICT_5X5_250)
print(aruco_dict) # Ouptput was: <aruco_Dictionary 072C5AB0>

# aruco.drawMarker(dictionary object,marker id,total image size)
'''If parameter total image size is n then, image size will be nxn pixels. The number n chosen should never be less than
the number of bits. Ideally it should be more than (number of bits + border size). However, a way higher number
will make deformations insignificant.'''
img=aruco.drawMarker(aruco_dict,11,400)

#cv2.imwrite("test_marker.jpg", img)
cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
