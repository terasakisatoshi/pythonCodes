import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
import numpy as np


BATCH_SIZE = 128
NUM_CLASSES = 10
EPOCHS = 20


def get_dataset():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = x_train.reshape(60000, 784)
    x_test = x_test.reshape(10000, 784)
    x_train = x_train.astype(np.float32)/255
    x_test = x_test.astype(np.float32)/255

    # create one hot vector
    y_train = keras.utils.to_categorical(y_train, NUM_CLASSES)
    y_test = keras.utils.to_categorical(y_test, NUM_CLASSES)

    return x_train, y_train, x_test, y_test


def define_model():
    model = Sequential()
    model.add(Dense(512, activation='relu', input_shape=(784,)))
    model.add(Dropout(0.2))
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(NUM_CLASSES, activation='softmax'))
    model.summary()

    model.compile(loss='categorical_crossentropy',
                  optimizer=RMSprop(),
                  metrics=['accuracy'])
    return model


def main():
    x_train, y_train, x_test, y_test = get_dataset()

    model = define_model()

    history = model.fit(x_train, y_train,
                        batch_size=BATCH_SIZE,
                        epochs=EPOCHS,
                        verbose=1,
                        validation_data=(x_test, y_test))
    score = model.evaluate(x_test,y_test,verbose=0)

    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

if __name__ == '__main__':
    main()
