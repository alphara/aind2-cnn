from keras.models import Sequential
from keras.layers import Conv2D

model = Sequential()

# model.add(Conv2D(filters=16, kernel_size=2, strides=2, padding='valid',
#    activation='relu', input_shape=(200, 200, 1)))

# model.add(Conv2D(filters=16, kernel_size=2, strides=2, padding='valid',
#    activation='relu', input_shape=(200, 200, 1)))

model.add(Conv2D(filters=32, kernel_size=3, strides=2, padding='same',
    activation='relu', input_shape=(128, 128, 3)))

# from math import ceil
# H_in = 128
# W_in = 128
# S = 2
# height = ceil(float(H_in) / float(S))
# width = ceil(float(W_in) / float(S))
# print('height:', height)
# print('width:', width)

model.summary()
