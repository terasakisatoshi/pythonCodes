from imageio import imread
from keras.datasets import mnist
from matplotlib import pyplot as plt
import numpy as np


def load_normalized_data():
    (x_train, _), (x_test, _) = mnist.load_data()
    x_train = x_train.reshape(-1, 28, 28, 1) / 255.
    x_test = x_test.reshape(-1, 28, 28, 1) / 255.
    return x_train, x_test


def make_masking_noise_data(data_x, percent=0.1):
    size = data_x.shape
    masking = np.random.binomial(n=1, p=percent, size=size)
    return data_x * masking


def make_gaussian_noise_data(data_x, scale=0.8):
    size = data_x.shape
    gaussian_data_x = data_x + np.random.normal(loc=0, scale=scale, size=size)
    gaussian_data_x = np.clip(gaussian_data_x, 0, 1)
    return gaussian_data_x


def main():
    x_train, x_test = load_normalized_data()

    x_train_masked = make_masking_noise_data(x_train)
    x_test_masked = make_masking_noise_data(x_test)

    x_train_gauss = make_gaussian_noise_data(x_train)
    x_test_gauss = make_gaussian_noise_data(x_test)

    original_image = x_train[0]
    masked_image = x_train_masked[0]
    gauss_image = x_train_gauss[0]

    fig, [ax1, ax2, ax3] = plt.subplots(nrows=1, ncols=3)

    ax1.imshow(original_image.reshape(28, 28), cmap="gray")
    ax2.imshow(masked_image.reshape(28, 28), cmap="gray")
    ax3.imshow(gauss_image.reshape(28, 28), cmap="gray")
    plt.show()

if __name__ == '__main__':
    main()
