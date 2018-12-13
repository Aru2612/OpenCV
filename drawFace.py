import numpy as np
import cv2

# Create the image
img = np.zeros((500,500,3), np.uint8)

# Draw an ellispe
cv2.ellipse(img,(250,150),(250,150),0,180,360,(0,255,0),-1)
cv2.ellipse(img,(250,150),(250,350),0,0,180,(148,205,255),-1)

# Draw a rectangle
cv2.rectangle(img,(0,140),(500,170),(238,130,238),-1)

# Draw a line
cv2.line(img,(0,155),(500,155),(211,0,148),5)

# Draw a circle
cv2.circle(img,(150,260), 55, (255,255,255), -1)
cv2.circle(img,(360,260), 55, (255,255,255),  -1)

# Draw an ellispe
cv2.ellipse(img,(150,260),(10,30),0,0,360,(0,0,0),-1)
cv2.ellipse(img,(360,260),(10,30),0,0,360,(0,0,0),-1)
cv2.ellipse(img,(250,300),(150,150),0,30,150,(0,0,255),5)

# Show the image
cv2.imshow('image',img)

# Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
