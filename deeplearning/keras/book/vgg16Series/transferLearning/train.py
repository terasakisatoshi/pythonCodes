from datetime import datetime
import json
import math
import os
import pickle

from keras.callbacks import ModelCheckpoint, CSVLogger

from dataset import image_iter_train, image_iter_validation
from transfer_learning import get_model


def train():
    model = get_model()
    model_dir = os.path.join('models', datetime.now().strftime('%y%m%d_%H%M'))
    os.makedirs(model_dir, exist_ok=True)
    dir_weights = os.path.join(model_dir, 'weights')
    os.makedirs(dir_weights, exist_ok=True)

    model_json = os.path.join(model_dir, 'model.json')
    with open(model_json, 'w') as f:
        json.dump(model.to_json(), f)

    model_classes = os.path.join(model_dir, 'classes.pkl')
    with open(model_classes, 'wb') as f:
        pickle.dump(image_iter_train.class_indices, f)

    batch_size = 16
    steps_per_epoch = math.ceil(
        image_iter_train.samples / batch_size)
    validation_steps = math.ceil(
        image_iter_validation.samples / batch_size)

    ckpt_file_path = os.path.join(
        dir_weights, 'ep_{epoch:02d}_ls_{loss:.lf}.h5')
    ckpt = ModelCheckpoint(ckpt_file_path,
                           monitor='loss',
                           verbose=0,
                           save_best_only=False,
                           save_weights_only=True,
                           mode='auto',
                           period=5)
    csv_file_path = os.path.join(model_dir, 'loss.csv')
    csv = CSVLogger(csv_file_path, append=True)

    max_epochs = 30

    history = model.fit_generator(image_iter_train,
                                  steps_per_epoch=steps_per_epoch,
                                  epochs=max_epochs,
                                  validation_data=image_iter_train,
                                  validation_steps=validation_steps,
                                  callbacks=[ckpt, csv])


def main():
    train()

if __name__ == '__main__':
    main()
