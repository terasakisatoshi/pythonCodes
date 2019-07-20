from keras.datasets import mnist

from dataset import load_normalized_data, make_gaussian_noise_data, make_masking_noise_data
from model import define_autoencoder


def main():
    x_train, x_test = load_normalized_data()

    x_train_masked = make_masking_noise_data(x_train)
    x_test_masked = make_masking_noise_data(x_test)

    x_train_gauss = make_gaussian_noise_data(x_train)
    x_test_gauss = make_gaussian_noise_data(x_test)

    initial_weights, autoencoder = define_autoencoder()
    autoencoder.fit(x_train_gauss, x_train, epochs=10,
                    batch_size=20, shuffle=True)

if __name__ == '__main__':
    main()
