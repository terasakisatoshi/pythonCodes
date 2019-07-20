from keras.datasets import cifar10
from keras.utils import to_categorical
from keras.callbacks import TensorBoard
from keras.layers import Conv2D, Dense, Dropout, Flatten, MaxPooling2D
from keras.models import Sequential
# load data
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# normalize
x_train = x_train / 255
x_test = x_test / 255

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# define model
model = Sequential()
model.add(Conv2D(filters=32,
                 input_shape=(32, 32, 3),
                 kernel_size=(3, 3),
                 strides=(1, 1),
                 padding='same',
                 activation='relu'))
model.add(Conv2D(filters=32,
                 input_shape=(32, 32, 3),
                 kernel_size=(3, 3),
                 strides=(1, 1),
                 padding='same',
                 activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(filters=64,
                 input_shape=(32, 32, 3),
                 kernel_size=(3, 3),
                 strides=(1, 1),
                 padding='same',
                 activation='relu'))
model.add(Conv2D(filters=64,
                 input_shape=(32, 32, 3),
                 kernel_size=(3, 3),
                 strides=(1, 1),
                 padding='same',
                 activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(units=512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(units=10, activation='softmax'))

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'])

tsb = TensorBoard(log_dir='logs')
history_model = model.fit(
    x_train,
    y_train,
    batch_size=32,
    epochs=20,
    validation_split=0.2,
    callbacks=[tsb])
