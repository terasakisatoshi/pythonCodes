import tensorflow as tf
from klas import layers, Sequential
def


def main():
    model = Sequential(layers.flatten(input_shape=(28, 28)),
                       layers.Dense(128, activation='relu'),
                       layers.Dense(10, activation='softmax'))
    fashion_mnist = keras.datasets.fashion_mnist

    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


if __name__ == '__main__':
    main()
