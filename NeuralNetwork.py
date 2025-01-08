import keras
import os
import random
import matplotlib as plt
import matplotlib.image as mpimg
from keras import *
import numpy as np
path = r"C:\Users\sebi6\TuberculosisNNnoGitHubShare\AllData\data\all\preprocessed"
filenames = []
imgdata=[]
tuberc=[]
for root, dirs, files in os.walk(path, topdown=False):
        for name in files:

            filename=os.path.join(root, name)
            filenames.append(filename)
            boolifTurbecolosis=os.path.basename(os.path.normpath(root))
            imgdata.append(mpimg.imread(filename))
            tuberc.append(float(boolifTurbecolosis))

tuberc=np.array(tuberc)
imgdata=np.array(imgdata)
print(imgdata.shape)

model = keras.Sequential(
    [   layers.Input(shape=(512,512,1)),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(1, activation="softmax")])



model.summary()
model.compile(loss="mean_squared_error", optimizer="adam", metrics=["accuracy"])
model.fit(imgdata, tuberc, batch_size=10, epochs=10, validation_split=0.1)
