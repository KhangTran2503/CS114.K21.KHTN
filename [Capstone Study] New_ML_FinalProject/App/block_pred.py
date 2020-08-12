import cv2
import imutils
import joblib
import numpy as np
from Preprocessing.Preprocessor import preprocessing
from FeatureExtraction.ExtractFeature import *


def predict():
    class_name = ['B','C','D','E','CT']
    model_path = 'model/TuningHOG.sav'
    image_path = 'static/image/new_image'
    model = joblib.load(model_path)
    image = cv2.imread(image_path)
    image = preprocessing(image,128,128)
    
    data = np.array([HOG(image)])
    preds = model.predict(data)
    return preds
