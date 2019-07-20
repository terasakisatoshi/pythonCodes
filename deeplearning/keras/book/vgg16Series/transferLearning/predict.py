from keras.applications.vgg16 import preprocess_input

from dataset import image_iter_train
from utils import load_random_imgs, show_test_samples

test_data_dir = 'img/shrine_temple/test/unknown/'
x_test, true_labels = load_random_imgs(
    test_data_dir,
    seed=1)

x_test_preproc = preprocess_input(x_test.copy()) / 255.0
probs = model.predict(x_test_preproc)

show_test_samples(x_test, probs, image_iter_train.class_indices, true_labels)
