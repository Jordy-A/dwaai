#==============================================================================
#   NEURAL NETWORK
#   ==============
#   The following code documents an attempt at making the MFCC array work with
#   Keras' 1D Convolutional Neural Network. The attempt was fruitless.
#==============================================================================

import pickle
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv1D, MaxPooling1D 
from keras.utils import np_utils
from keras.utils import to_categorical
from keras.layers import GaussianNoise, GlobalAveragePooling1D
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import f1_score

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

no_mfcc_bands = 120
test_dim = 1
maxlen = 100
batch_size = 97
nb_filter = 150
nb_filter_2 = 200
filter_length_1 = 20
filter_length_2 = 10
hidden_dims = 250
nb_epoch = 20
nb_classes = 2

# Get dataframes from folder C:\Users\s157874\Documents\GitHub\dwaai\mfcc\example_datas. Change this to your own path. 
featuresdf = pd.read_pickle('C:\\Users\\s157874\\Documents\\GitHub\\dwaai\\mfcc\\example_datas\\mffc_extracted_WINDOWS') 
print(featuresdf)

# Convert features and corresponding classification labels into numpy arrays
X = np.array(featuresdf.feature.tolist())
y = np.array(featuresdf.class_label.tolist())

# Encode the classification labels
le = LabelEncoder()
yy = to_categorical(le.fit_transform(y)) 

# Split the dataset in training and testing
X_train, X_test, y_train, y_test = train_test_split(X, yy, test_size=0.30)

print(X_train.shape, 'After first row')
print(y_train.shape, 'y')

xts = X_train.shape
xtss = X_test.shape

X_train = np.reshape(X_train, (xts[0], xts[1], 1))
X_test = np.reshape(X_test, (xtss[0], xtss[1], 1))

print(len(X_train), 'training sequences, ', len(X_test), 'test sequences')
print(X_train.shape)
print(y_train.shape)

cat = LabelEncoder()

print('Build model...')
model = Sequential()
print(X_train.shape, 'After buidling model')

# We add GaussianNoise to increase our data
model.add(GaussianNoise(0.1, input_shape=(no_mfcc_bands,1)))
model.summary()
model.get_config()
print('Added noise...')

print(X_train.shape, 'After adding noise')

# The first Convolution1D layer. Before the layer, we have a matrix of 120 x 1. 120 is the length of the dataset, our number of MFCC bans (height), and a single timestamp (width).
# With a height of 120 and a kernel size of 20 , the window will slice through the data for 111 steps (120+1-20). 
# The Convolutional Layer has 150 feauture detectors, resulting in a 101 x 150 window. 
model.add(Conv1D(input_shape=(no_mfcc_bands, 1),
                        activation="relu",
						filters=nb_filter,
						kernel_size=filter_length_1, 
                        padding="valid",
                        ))
print('Added the first Conv1D layer...')

# The second Convolutional layer. Having a second layer prior pooling allows the model to learn more features.
# Adding a second 1D Conv layer with kernel size 10 will result in a matrix of 92 x 150 (101+1-10).
model.add(Conv1D(activation="relu",
						filters=nb_filter,
						kernel_size=filter_length_2, 
                        padding="valid",
                        ))
print('Added the second Conv1D layer...')

# We use standard max pooling for halving the output of the previous layer and prevent overfitting. The output of this layer is only a third of the input layer. 
# We now have a matrix of 30 x 150 
model.add(MaxPooling1D(pool_size=3))
print('Used Max Pooling..')

model.add(BatchNormalization())
print('Used Batch Normalization..')

# The thrid and fourth Convolutional layer in order to learn more high level features. 
# Adding a thirds 1D Conv layer with kernel size 10, and 200 feature detectors, will result in a matrix of 21 x 200 (30+1-10).
# Adding a fourth 1D Conv layer with kernel size 10, and 200 feature detectors, will result in a matrix of 12 x 200 (210+1-10).
model.add(Conv1D(activation="relu",
						filters=nb_filter,
						kernel_size=filter_length_2, 
                        padding="valid",
                        ))

model.add(Conv1D(activation="relu",
						filters=nb_filter,
						kernel_size=filter_length_2, 
                        padding="valid",
                        ))                        

print('Added the third and fourth Conv1D layers...')

model.add(GlobalAveragePooling1D())
print('Added Global average pooling...')
model.summary()
model.get_config()

# We add a vanilla hidden layer.. Why?
model.add(Dense(hidden_dims, activation='relu'))
print('Added a vanilla layer')

# We add a Dropout layer, it will randomly assign 0 weights to the neurons the network. 
# The output of the layer is ... 
model.add(Dropout(0.25))

model.summary()
model.get_config()

# We project onto a single unit output layer, and squash it with a sigmoid:
model.add(Dense(2, activation='softmax'))
model.compile(loss='binary_crossentropy', optimizer='rmsprop')

# Train the model:
model.fit(X_train, y_train, batch_size=batch_size, epochs=nb_epoch, verbose=1, validation_data=(X_test, y_test))
y_preds = model.predict(X_test)
score = model.evaluate(X_test, y_test, verbose=1)

# print score and print classification report with accuracy
print("Score:", score)
print(classification_report(y_test.argmax(axis=1), y_preds.argmax(axis=1), target_names=le.classes_))