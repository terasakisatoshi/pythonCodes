import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import numpy as np

BATCH_SIZE = 128
NUM_CLASSES = 10
EPOCHS = 20
IMG_ROW = 28
IMG_COL = 28


def get_dataset(input_shape):
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = x_train.reshape(x_train.shape[0], *input_shape)
    x_test = x_test.reshape(x_test.shape[0], *input_shape)

    x_train = x_train.astype(np.float32)/255
    x_test = x_test.astype(np.float32)/255

    # create one hot vector
    y_train = keras.utils.to_categorical(y_train, NUM_CLASSES)
    y_test = keras.utils.to_categorical(y_test, NUM_CLASSES)
    return x_train, y_train, x_test, y_test


def define_model(input_shape):
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3),
                     activation='relu', input_shape=input_shape))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(NUM_CLASSES, activation='softmax'))
    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adadelta(),
                  metrics=['accuracy'])
    return model


def main():
    if K.image_data_format() == 'channels_first':
        input_shape = (1, IMG_ROW, IMG_COL)
    else:
        input_shape = (IMG_ROW, IMG_COL, 1)
    x_train, y_train, x_test, y_test = get_dataset(input_shape)
    model = define_model(input_shape)
    model.fit(x_train, y_train, batch_size=BATCH_SIZE, epochs=EPOCHS,
              verbose=True, validation_data=(x_test, y_test))
    score=model.evaluate(x_test,y_test,verbose=False)
    print('Test loss',score[0])
    print('Test accuracy',score[1])


if __name__ == '__main__':
    main()
