import os
import scipy as scp
import PIL
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

#Versionen von Scipy, Pillow und Tensorflow abfragen
#print("scipy version: ", scp.__version__) #only works after loading: source /mount/packs/tensorflow/bin/activate
#print("Pillow version: ", PIL.__version__)
#print("TensorFlow version:", tf.__version__)


path = r"C:\Users\sebi6\TuberculosisNNnoGitHubShare\AllData\data\all\preprocessed"

filenames = []
for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            filenames.append(os.path.join(root, name))

#Infos über die Daten
images = []
image_data = []
for image_path in filenames:
    images.append(Image.open(image_path))
    image_data.append(np.asarray(images[-1]))
print("Number of files: ", len(images))
print("File dimensions: ", image_data[0].shape)
print("Type images: ", type(images[0]))
print("Type image_data: ", type(image_data[0]))

#Preprocessing der Daten
#Remove mean
image_data = np.array(image_data)
mean_value = np.mean(image_data)
print("Global Mean des Datensatzes: ", mean_value)
image_data = image_data - mean_value

# Divide by standard deviation
std_value = np.std(image_data)
print("Standard Daviation Value:", std_value)
image_data = image_data /std_value

# Add dummy channel layer
image_data = image_data[:,:,:,np.newaxis] #Gegeben im Jupiter Notebook

print("Image data shape: ", image_data.shape)
print("Expected shape: (138, 512, 512, 1)") #Trotzdem noch 1104 Bilder und nicht 138 warum?



labels = []
print("Exemplary filename: ",filenames[0]) #Gibt Name des ersten Bildes im Datesatz aus (Letze Zahl vor dem .png gibt an ob der Patient Tuberkulose hat (1) oder gesund ist (0).


# Append labels of each image to labels list (JNB)
for filename in filenames:
    #Überprüft ob Datei in Ordner (parent directory) "1" oder "0" gespeichert ist
    label = int(os.path.basename(os.path.dirname(filename)))
    labels.append(label)
if len(labels) != len(images):
    print("Error: not same number of images and labels!")
print("Percentage of 'tbc' in all images: ", np.sum(labels)/len(labels))
print("Percentage of 'nothing' in all images: ", (len(labels) -np.sum(labels))/len(labels)) #Auch überprüfbar wenn man auf "Eigenschaften" klickt bei den jeweiligen Ordnern


# Visualize some examples (JNB)
plt.figure(figsize=(12, 12))
#Auswählen von 9 random Bildern
random_indices = np.random.randint(0, len(images), 9)
for idx, img_idx in enumerate(random_indices):
    #3x3 Anzeige der Bilder
    plt.subplot(3, 3, idx + 1)
    plt.imshow(np.array(images[img_idx]), cmap='gray') #plt.imshow(np.array(images[img_idx])) so werden sie in Blau zu Grün Tönen angezeigt
    #Titel der Bilder
    label_text = "Tuberkulose" if labels[img_idx] == 1 else "Gesund"
    plt.title(f"{label_text} (Label: {labels[img_idx]})")
plt.tight_layout()
plt.show()
