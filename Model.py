# import the necessary packages
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2

from mtcnn import MTCNN

weightsPath = 'Model/res_expr.h5'

model = load_model(weightsPath)

# model.summary()

labels = ['anger', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
detector = MTCNN()


def detect_and_plot(image_path):
    # reading image
    image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

    results = detector.detect_faces(image)

    # Result is an array with all the bounding boxes detected. We know that for 'ivan.jpg' there is only one.
    bounding_box = results[0]['box']
    (x, y, w, h) = bounding_box
    # face = image[startY:endY, startX:endX]
    face = image[y:y + h, x:x + w]
    # plt.imshow(face)

    face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
    face = cv2.resize(face, (224, 224))
    face = img_to_array(face)
    face = preprocess_input(face)
    face = np.expand_dims(face, axis=0)

    # pass the face through the model to determine if the face has a mask or not
    result = model.predict(face)[0]
    # print(result)

    index_label = np.argmax(result, axis=0)
    label = labels[index_label]
    #print(label)
    if label == "happy" or label == "neutral":
        #print(1)
        return ({
            "Result" : "Happy"
        })
    else:
        #print(0)
        return ({
            "Result": "Not_happy"
        })

#detect_and_plot('Model/p14.jpg')

