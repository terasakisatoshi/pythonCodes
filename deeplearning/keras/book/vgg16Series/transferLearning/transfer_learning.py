from keras.applications.vgg16 import VGG16
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.optimizers import SGD


def build_transfer_model(vgg16):
    model = Sequential(vgg16.layers)
    for layer in model.layers[:15]:
        layer.trainable = False
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))
    return model


def get_model():
    vgg16 = VGG16(include_top=False, input_shape=(224, 224, 3))
    model = build_transfer_model(vgg16)
    model.compile(
        loss='binary_crossentropy',
        optimizer=SGD(lr=1e-4, momentum=0.9),
        metrics=['accuracy'])
    return model


def main():
    model = get_model()
    model.summary()


if __name__ == '__main__':
    main()
