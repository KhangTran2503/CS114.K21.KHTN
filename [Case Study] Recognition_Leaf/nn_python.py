from nn.neuralnetwork import NeuralNetwork
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from dataloader.simpledatasetloader import SimpleDatasetLoader
from preprocessing.simplepreprocessor import SimplePreprocessor
from imutils import paths
import os
import numpy as np

# grab the list of images 
print ("[INFO] loading images ...")
imagePaths = list(paths.list_images("Dataset Leaf"))
#print(len(imagePaths))

classNames = [pt.split(os.path.sep)[-2] for pt in imagePaths]
classNames = [str(x) for x in np.unique(classNames)]

# initialize the image preprocessor, load the data set from disk
# and reshape the data matrix
sp = SimplePreprocessor(32,32)
sdl = SimpleDatasetLoader(preprocessors=[sp])
(data, labels) = sdl.load(imagePaths, verbose=100)
data = data.astype("float")
data = (data - data.min()) / (data.max() - data.min())

# construct the training and testing splits
(trainX, testX, trainY, testY) = train_test_split(data, labels, test_size=0.25)

# convert the labels from string to vertors
trainY = LabelBinarizer().fit_transform(trainY)
testY  = LabelBinarizer().fit_transform(testY)

# train the network
print("[INFO] training network...")
nn = NeuralNetwork([trainX.shape[1], 64, 16, 32])
print("[INFO] {}".format(nn))
nn.fit(trainX, trainY, epochs=1000)

# evaluate the network
print("[INFO] evaluating network...")
predictions = nn.predict(testX)
print(classification_report(testY.argmax(axis=1), predictions.argmax(axis=1),
    target_names=classNames))
