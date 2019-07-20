
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, UpSampling2D


def define_autoencoder():
    # encoder
    autoencoder = Sequential()
    autoencoder.add(Conv2D(16, (3, 3), strides=1, activation="relu",
                           padding="same", input_shape=(28, 28, 1)))
    autoencoder.add(MaxPooling2D((2, 2), padding="same"))
    autoencoder.add(Conv2D(8, (3, 3), strides=1,
                           activation="relu", padding="same"))
    autoencoder.add(MaxPooling2D((2, 2), padding="same"))
    # decoder
    autoencoder.add(Conv2D(8, (3, 3), strides=1,
                           activation="relu", padding="same"))
    autoencoder.add(UpSampling2D((2, 2)))
    autoencoder.add(Conv2D(16, (3, 3), strides=1,
                           activation="relu", padding="same"))
    autoencoder.add(UpSampling2D((2, 2)))
    autoencoder.add(Conv2D(1, (3, 3), strides=1,
                           activation="sigmoid", padding="same"))

    autoencoder.compile(optimizer="adam", loss="binary_crossentropy")
    initial_weights = autoencoder.get_weights()
    return initial_weights, autoencoder
