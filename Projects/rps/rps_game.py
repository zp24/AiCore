import cv2
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import random
import time

# Load the model
model = load_model("keras_model.h5")

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
#data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Replace this with the path to your image
#image = Image.open('<IMAGE_PATH>')
#image = False
#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
#size = (224, 224)
#image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
#image_array = np.asarray(image)
# Normalize the image
#normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# Load the image into the array
#data[0] = normalized_image_array

# run the inference
#prediction = model.predict(data)
#print(prediction)


#model = load_model('YOUR_MODEL.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()