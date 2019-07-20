from keras.datasets import mnist
from keras.utils import to_categorical
from keras.layers import Input, Dense
from keras.models import Model
from keras.callbacks import TensorBoard
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# normalize
x_train = x_train.reshape(-1, 28 * 28) / 255
x_test = x_test.reshape(-1, 28 * 28) / 255
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# define model
input_layer = Input(shape=(28 * 28, ))
middle_layer = Dense(units=64, activation='relu')(input_layer)
output_layer = Dense(units=10, activation='softmax')(middle_layer)
model = Model(inputs=[input_layer], outputs=[output_layer])
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
# prepare tensorboard
tsb = TensorBoard(log_dir='logs')

history_adam = model.fit(x_train,
                         y_train,
                         batch_size=32,
                         epochs=20,
                         validation_split=0.2,
                         callbacks=[tsb])
