from skimage import feature
import numpy as np

def Img_to_Vec(Img):
    return np.array(Img).flatten()/255.

def HOG(Img,self_orientations=9,self_pixels_per_cell=(8, 8),
			                self_cells_per_block=(2, 2), self_transform_sqrt=True, 
							self_block_norm="L2-Hys"):
    return feature.hog(Img, orientations=self_orientations, 
                       pixels_per_cell=self_pixels_per_cell,
			            cells_per_block=self_cells_per_block, transform_sqrt=self_transform_sqrt, 
							block_norm=self_block_norm,feature_vector=True)
    

def LocalBinaryPatterns(Img,numPoints=24,radius=8,eps=1e-7):
    # compute the Local Binary Pattern representation
    # of the image, and then use the LBP representation
    # to build the histogram of patterns
    lbp = feature.local_binary_pattern(Img,numPoints,radius, method="uniform")
    (hist, _) = np.histogram(lbp.ravel(),
                                 bins=np.arange(0, numPoints + 3),
                                 range=(0, numPoints + 2))
    # normalize the histogram
    hist = hist.astype("float")
    hist /= (hist.sum() + eps)
    # return the histogram of Local Binary Patterns
    return hist 