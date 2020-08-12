import cv2
import imutils
import numpy as np

def resize_ratio(img,self_width = 256,self_height = 256,self_inter = cv2.INTER_AREA):
    # get size of image
    (h,w) = img.shape[:2]
    dW = 0
    dH = 0
    if w < h:
        img = imutils.resize(img,width=self_width,inter=self_inter)
        dH = int((img.shape[0] - self_height)/2.0)
    else:
        img = imutils.resize(img,height=self_height,inter=self_inter)
        dW = int((img.shape[1] - self_width)/2.0)

    (h,w) = img.shape[:2]
    img = img[dH:h - dH,dW:w - dW]

    return cv2.resize(img,(self_width,self_height),interpolation=self_inter)

def preprocessing(Image,w=256,h=256):
    # covert to grayscale
    Image = cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
    
    # Equalize Histogram
    Image = cv2.equalizeHist(Image)
    
    # Bilateral Filter
    Image = cv2.bilateralFilter(Image,9,75,75)
    
    # Sharpening images 
    kernel = np.array([[-1,-1,-1],
                   [-1, 9,-1],
                   [-1, -1,-1]])
    Image = cv2.filter2D(Image,-1,kernel)
    
    # Resize aspect ratio
    Image = resize_ratio(Image,w,h)
    return Image