import cv2
import numpy as np

n=input('Enter the size of the board: ')
n=int(n)
img=np.zeros((n*100,n*100),np.uint8)

for i in range(0,n):
    for j in range(0,n,2):
        if(i%2==0):
            img[i*100:(i+1)*100,j*100:(j+1)*100]=255
        else:
            if(j+2<=n):
                img[i*100:(i+1)*100,(j+1)*100:(j+2)*100]=255

# Show the images
cv2.imshow('Chessboard',img)

# Close and exit
cv2.waitKey(0) # 0 makes it wait infinitely
cv2.destroyAllWindows()
