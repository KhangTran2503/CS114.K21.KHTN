from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD

from preprocessing.imagetoarraypreprocessor import ImageToArrayPreprocessor
from preprocessing.simplepreprocessor import SimplePreprocessor

from dataloader.simpledatasetloader import SimpleDatasetLoader

from imutils import paths
import os
import numpy as np 

# grab the list of images 
print("[INFO] loading images...")
imagePaths = list(paths.list_images('Dataset Leaf'))

classNames = [pt.split(os.path.sep)[-2] for pt in imagePaths]
classNames = [str(x) for x in np.unique(classNames)]

# initialize the image preprocessors
sp = SimplePreprocessor(32,32)
iap = ImageToArrayPreprocessor()

sdl = SimpleDatasetLoader(preprocessors=[sp,iap])
(data, labels) = sdl.load(imagePaths, verbose=100)
data = data.astype("float") / 255.0
data = data.reshape((data.shape[0], 3072))

# partition the data into training:75% and testing:25% 
(trainX, testX, trainY, testY) = train_test_split(data, labels,
test_size=0.25, random_state=42)

# convert the labels from integers to vectors
trainY = LabelBinarizer().fit_transform(trainY)
testY = LabelBinarizer().fit_transform(testY)

# define the 3072-1024-512-32 architecture using keras
model = Sequential()
model.add(Dense(1024, input_shape=(3072,), activation="relu"))
model.add(Dense(512, activation="relu"))
model.add(Dense(32, activation="softmax"))

# initialize the optimizer and model
print("[INFO] compiling model...")
#opt= SGD(lr=0.05)
opt = SGD(lr=0.01, decay=0.01 / 80, momentum=0.9, nesterov=True)
model.compile(loss="categorical_crossentropy", optimizer=opt,
             metrics=["accuracy"])

# train the network
print("[INFO] training network...")
model.fit(trainX, trainY, validation_data=(testX,testY),
          batch_size=32, epochs=80, verbose=1)


# evaluate the network
print("[INFO] evaluating network used decay=0.01/80...")
predictions = model.predict(testX, batch_size=32)
print(classification_report(testY.argmax(axis=1),
      predictions.argmax(axis=1),
      target_names=classNames))
