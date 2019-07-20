from keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg16 import preprocess_input

image_data_train = ImageDataGenerator(
    rescale=1 / 255,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
    preprocessing_function=preprocess_input)

image_iter_train = image_data_train.flow_from_directory(
    'img/shrine_temple/train',
    target_size=(224, 224),
    batch_size=16,
    class_mode='binary')

image_iter_validation = image_data_train.flow_from_directory(
    'img/shrine_temple/validation',
    target_size=(224, 224),
    batch_size=16,
    class_mode='binary')
