import cv2
import imutils

class SimplePreprocessor:
    def __init__(self, width, height, inter=cv2.INTER_AREA):
        # store the target image width, height, interpolation 
        # method used when resizing
        self.width = width
        self.height = height
        self.inter = inter
    
    def preprocess(self, image):
     
        # grab the dimesions of the image and then initialize
        # the deltas to use when cropping
        (h, w) = image.shape[:2]
        dW = 0
        dH = 0

        # if the width is smller than the height,so resize
        # along the width and then update the deltas 
        # to crop the height to the desired demension
        if w < h:
            image =imutils.resize(image, width=self.width, inter=self.inter)
            dH = int((image.shape[0] - self.height) / 2.0)

        # otherwise, the height is smaller than the width so 
        # resize along the height and then update the deltas 
        # to crop along the width
        else:
            image = imutils.resize(image, height=self.height, inter=self.inter)
            dW = int((image.shape[1] - self.width) / 2.0)

        # now that our images have been resized, we need to 
        # re-grab the width and height, followed by performing
        # the crop
        (h,w) = image.shape[:2]
        image = image[dH:h -dH, dW:w-dW]

        # finally, resize the image to the provided spatial
        # demensions to ensure ourput image is slways a fixed
        # size
        return cv2.resize(image, (self.width, self.height), interpolation=self.inter)
