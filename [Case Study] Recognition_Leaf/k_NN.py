from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

from preprocessing.simplepreprocessor import SimplePreprocessor
from preprocessing.imagetoarraypreprocessor import ImageToArrayPreprocessor

from dataloader.simpledatasetloader import SimpleDatasetLoader

from sklearn.neighbors import KNeighborsClassifier

from imutils import paths
import os
import numpy as np 

# grab the list of images 
print ("[INFO] loading images ...")
imagePaths = list(paths.list_images("Dataset Leaf"))
#print(len(imagePaths))

classNames = [pt.split(os.path.sep)[-2] for pt in imagePaths]
classNames = [str(x) for x in np.unique(classNames)]


# initialize the image preprocessors
sp = SimplePreprocessor(32,32)
iap = ImageToArrayPreprocessor()

# load data and reshape (N, 3072) with N = len(imagePaths)
sdl = SimpleDatasetLoader(preprocessors=[sp,iap])
(data, labels) = sdl.load(imagePaths, verbose=100)
data = data.astype("float") / 255.0
data = data.reshape((data.shape[0], 3072))

# partition the data into training: 75%, testing: 25%
(trainX, testX, trainY, testY) = train_test_split(data, labels, 
                                 test_size=0.25, random_state=42)

# convert the labels from intergers to vectors
trainY = LabelBinarizer().fit_transform(trainY)
testY  = LabelBinarizer().fit_transform(testY)

# train the k_NN
print("[INFO] training k_NN...")
model = KNeighborsClassifier(n_neighbors=1, n_jobs=-1)
model.fit(trainX, trainY)

# evaluate a k-NN 
print("[INFO] evaluating K_NN...")
predictions = model.predict(testX)
print(classification_report(testY.argmax(axis=1),
     predictions.argmax(axis=1),
     target_names=classNames))

