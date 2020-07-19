from keras.applications import VGG16

# load the VGG16 network
print("[INFO] loading network...")
model = VGG16(weights="imagenet")

# loop over the layers in the network and display them to the console
print("[INFO] showing layers...")
for (i, layer) in enumerate(model.layers):
    print("[INFO] {}\t{}".format(i, layer.__class__.__name__))