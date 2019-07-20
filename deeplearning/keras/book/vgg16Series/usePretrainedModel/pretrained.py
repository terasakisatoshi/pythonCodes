from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import decode_predictions, preprocess_input
from keras.preprocessing.image import load_img, img_to_array
import numpy as np


model = VGG16()

dog = load_img('imgs/dog.jpg', target_size=(224, 224))
dog = img_to_array(dog)
cat = load_img('imgs/cat.jpg', target_size=(224, 224))
cat = img_to_array(cat)
goma = load_img('imgs/goma.jpeg', target_size=(224, 224))
goma = img_to_array(goma)

# convert RGB2BGR and centerize
dog = preprocess_input(dog)
cat = preprocess_input(cat)
goma = preprocess_input(goma)

input_array = np.stack([dog, cat, goma])

probs = model.predict(input_array)
results = decode_predictions(probs)

assume_dog = results[0]
assume_cat = results[1]
assume_goma = results[2]

print(assume_dog)
print(assume_cat)
print(assume_goma)
