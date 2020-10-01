# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:25:06 2020

@author: HOME
"""

import keras
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
import matplotlib.pyplot as plt
plt.imshow(x_train[0]) #training image
plt.show()
print(y_train[0])
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
input_shape = (28, 28, 1)

#Normalize the pixel values from a scale out of 255 to a scale out of 1
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print(y_train[0])
#Then, we convert the y values (numbers) into ones and zeros, making each number categorical

y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

print(y_train[0])
#bulding our cnn model
model = keras.models.Sequential()
model.add(keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu',
                              input_shape=input_shape))

model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(keras.layers.Dropout(0.25))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(128, activation='relu'))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(10, activation='softmax'))

# Next we need to train the network
model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizers.Adadelta(),metrics=['accuracy'])

model.fit(x_train, y_train,batch_size=128,epochs=1,validation_data=(x_test, y_test))
model.fit(x_train, y_train,batch_size=128,epochs=1,validation_data=(x_test, y_test))

#run the model on the test data and print the results. The first number is the loss and the second number is the accuracy out of 1.
print(model.evaluate(x_test, y_test))