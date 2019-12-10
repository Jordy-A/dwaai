# Load various imports 
import pandas as pd
import os
import librosa
import numpy as np

# Define a function that will generate MFCC from a given audio file
def extract_features(file_name):
    # Print current audio file
    print('Loading: "', file_name, '"')
    try:
        # Load audio file into librosa
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 

        # Generate MFCC
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        mfccsscaled = np.mean(mfccs.T,axis=0)
        
    except Exception as e:
        print("Error encountered while parsing file: ", e)
        return None 
     
    # Return the MFCC
    return mfccsscaled

# Create an empty array with the features that are about to be generated
features = []

# Loop through any directories in ./samples
for className in os.listdir('./samples'):
    # Every directory is a classifier
    # Then loop through every audio file in that directory
    for fileName in os.listdir('./samples/' + className):
        # Generate the MFCC for the given audio file
        data = extract_features('./samples/' + className + '/' + fileName)

        # Then store the resulting MFCC in the feature array under the
        # classification of the parent classifier
        features.append([data, className])

# Lastly, put the resulting array in a pandas DataFrame
featuresdf = pd.DataFrame(features, columns=['feature', 'class_label'])
print('Finished feature extraction from ', len(featuresdf), ' files')

#===================================
#   RANDOM FOREST
#===================================

from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Convert features and corresponding classification labels into numpy arrays
X = np.array(featuresdf.feature.tolist())
y = np.array(featuresdf.class_label.tolist())

# Split our dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Log training and test instances
print(len(X_train), 'training instances,', len(X_test), 'testing instances')

# Scale the features on the X sets
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Then, setup the RandomForest classifier
classifier = RandomForestClassifier(n_estimators=100)

# Train the algorithm on the current data
classifier.fit(X_train, y_train)

# Then evaluate the predictions on the test data...
y_pred = classifier.predict(X_test)

# ...and log the output from the test evaluation
feature_imp = pd.Series(classifier.feature_importances_).sort_values(ascending=False)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Feature importance:", feature_imp)

#==============================================================================
#   NEURAL NETWORK
#   ==============
#   The following code documents an attempt at making the MFCC array work with
#   Keras' 1D Convolutional Neural Network. The attempt was fruitless.
#==============================================================================

# from sklearn.model_selection import train_test_split
# from sklearn.metrics import classification_report

# from keras.preprocessing import sequence
# from keras.models import Sequential
# from keras.layers.core import Dense, Dropout, Activation, Flatten
# from keras.layers.normalization import BatchNormalization
# from keras.layers.convolutional import Convolution1D, MaxPooling1D
# from keras.utils import np_utils
# from keras.layers import GaussianNoise

# test_dim = 2999
# maxlen = 100
# batch_size = 100
# nb_filter = 64
# filter_length_1 = 50
# filter_length_2 = 25
# hidden_dims = 250
# nb_epoch = 8
# nb_classes = 2

# from sklearn.preprocessing import LabelEncoder
# from keras.utils import to_categorical

# # Convert features and corresponding classification labels into numpy arrays
# X = np.array(featuresdf.feature.tolist())
# y = np.array(featuresdf.class_label.tolist())

# # Encode the classification labels
# le = LabelEncoder()
# yy = to_categorical(le.fit_transform(y)) 

# # split the dataset 
# from sklearn.model_selection import train_test_split 

# X_train, X_test, y_train, y_test = train_test_split(X, yy, test_size=0.15)



# xts = X_train.shape
# xtss = X_test.shape
# yts = y_train.shape
# ytss = y_test.shape

# X_train = X_train.reshape(17, 40, 1)
# X_test = X_test.reshape(3, 40, 1)

# print(len(X_train), 'training sequences, ', len(X_test), 'test sequences')

# Y_train = np_utils.to_categorical(y_train, nb_classes)
# Y_test = np_utils.to_categorical(y_test, nb_classes)

# print('Build model...')
# model = Sequential()

# # we start off with an efficient embedding layer which maps
# # our vocab indices into embedding_dims dimensions
# # model.add(Embedding(max_features, embedding_dims, input_length=maxlen))
# # model.add(Dropout(0.25))

# model.add(GaussianNoise(0.1, input_shape=(40,1)))

# # we add a Convolution1D, which will learn nb_filter
# # word group filters of size filter_length:
# model.add(Convolution1D(nb_filter=nb_filter,
#                         filter_length=filter_length_1,
#                         input_shape=(40, 1),
#                         border_mode='valid',
#                         activation='relu'
#                         ))
# # we use standard max pooling (halving the output of the previous layer):
# model.add(BatchNormalization())

# model.add(Convolution1D(nb_filter=nb_filter,
#                         filter_length=filter_length_2,
#                         border_mode='same',
#                         activation='relu'
#                         ))

# model.add(BatchNormalization())

# model.add(MaxPooling1D(pool_length=2))

# model.add(Convolution1D(nb_filter=nb_filter,
#                         filter_length=filter_length_2,
#                         border_mode='same',
#                         activation='relu'
#                         ))

# model.add(BatchNormalization())

# model.add(MaxPooling1D(pool_length=2))

# # We flatten the output of the conv layer,
# # so that we can add a vanilla dense layer:
# model.add(Flatten())

# # We add a vanilla hidden layer:
# # model.add(Dense(hidden_dims))
# model.add(Dropout(0.25))
# # model.add(Activation('relu'))

# # We project onto a single unit output layer, and squash it with a sigmoid:
# model.add(Dense(2))
# model.add(Activation('softmax'))

# model.compile(loss='binary_crossentropy', optimizer='rmsprop')
# model.fit(X_train, Y_train, batch_size=batch_size, nb_epoch=nb_epoch, verbose=1, validation_data=(X_test, Y_test))

# #y_preds = model.predict(X_test)

# score = model.evaluate(X_test, Y_test,  verbose=1)

# #print(classification_report(y_test, y_preds))