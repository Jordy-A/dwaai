#==============================================================================
#   NEURAL NETWORK
#   ==============
#   The following code documents an attempt at making the MFCC array work with
#   Keras' 1D Convolutional Neural Network. The attempt was fruitless.
#==============================================================================

import pickle
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
from keras.layers import GaussianNoise
from sklearn.preprocessing import LabelEncoder

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

test_dim = 1
maxlen = 100
batch_size = 82
nb_filter = 256
#kernelsize
filter_length_1 = 20
filter_length_2 = 10
hidden_dims = 250
nb_epoch = 20
nb_classes = 2

# Get dataframe from folder C:\Users\s157874\Documents\GitHub\dwaai\mfcc\example_datas
featuresdf = pd.read_pickle('C:\\Users\\s157874\\Documents\\GitHub\\dwaai\\mfcc\\example_datas\\mffc_extracted_WINDOWS') 
print(featuresdf)

# Convert features and corresponding classification labels into numpy arrays
X = np.array(featuresdf.feature.tolist())
y = np.array(featuresdf.class_label.tolist())

# Encode the classification labels
le = LabelEncoder()
yy = to_categorical(le.fit_transform(y)) 

# Split the dataset in training and testing
X_train, X_test, y_train, y_test = train_test_split(X, yy, test_size=0.15)

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

# # we start off with an efficient embedding layer which maps
# # our vocab indices into embedding_dims dimensions

# model.add(Embedding(max_features, embedding_dims, input_length=maxlen))
# model.add(Dropout(0.25))

model.add(GaussianNoise(0.1, input_shape=(no_mfcc_bands,1)))
print('Added noise...')

print(X_train.shape, 'After adding noise')

# we add a Convolution1D, which will learn nb_filter
# word group filters of size filter_length:
model.add(Conv1D(input_shape=(no_mfcc_bands, 1),
                        activation="relu",
						filters=nb_filter,
						kernel_size=filter_length_1, 
                        padding="valid",
                        ))

model.summary()
model.get_config()

print('Added a  Conv1D layer...')
# we use standard max pooling (halving the output of the previous layer):
model.add(BatchNormalization())

model.summary()
model.get_config()

print('Used Batch Normalization..')

model.add(Conv1D(activation="relu",
						filters=nb_filter,
						kernel_size=filter_length_2, 
                        padding="valid",
                        ))

model.summary()
model.get_config()

print('Added a  Conv1D layer...')

model.add(BatchNormalization())

print('Used Batch Normalization...')

model.add(MaxPooling1D(pool_size=1))

model.summary()
model.get_config()

print('Added standard pooling...')
model.add(Conv1D(activation="relu",
						filters=nb_filter,
						kernel_size=filter_length_2, 
                        padding="valid",
                        ))
model.add(BatchNormalization())
print('Used Batch Normalization...')
model.add(MaxPooling1D(pool_size=1))
print('Added standard pooling...')
# We flatten the output of the conv layer,
# so that we can add a vanilla dense layer:
model.add(Flatten())
print('Flatten...')
# We add a vanilla hidden layer:
model.add(Dense(hidden_dims, activation='relu'))
model.add(Dropout(0.25))
# model.add(Activation('relu'))
model.summary()
model.get_config()
print('Added a vanilla layer')
# We project onto a single unit output layer, and squash it with a sigmoid:
model.add(Dense(2, activation='softmax'))
model.summary()
model.get_config()
model.compile(loss='binary_crossentropy', optimizer='rmsprop')
model.summary()
model.get_config()
model.fit(X_train, y_train, batch_size=batch_size, epochs=nb_epoch, verbose=1, validation_data=(X_test, y_test))

y_preds = model.predict(X_test)
score = model.evaluate(X_test, y_test, verbose=1)
print("Score:", score)
print(classification_report(y_test.argmax(axis=1), y_preds.argmax(axis=1), target_names=le.classes_))