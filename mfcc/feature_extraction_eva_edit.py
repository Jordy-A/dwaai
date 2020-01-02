no_mfcc_bands = 120

# Load various imports 
import pandas as pd
import os
import librosa
import numpy as np
import os

'''
from pydub import AudioSegment

# Convert mp3 to WAV
src1 = "C:\\Users\\s157874\\Documents\\GitHub\\dwaai\\mfcc\\example_datas\\Dutch\\dutch1.mp3"
dst1 = "C:\\Users\\s157874\\Documents\\GitHub\\dwaai\\mfcc\\example_datas\\Dutch_wav\\dutch1.wav"
# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src1)
sound.export(dst1, format="wav")
print(sound.export)

'''

# Define a function that will generate MFCC from a given audio file
def extract_features(file_name):
    # Print current audio file
    # print('Loading: "', file_name, '"')
    try:
        # Load audio file into librosa
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 

        # Generate MFCC
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=no_mfcc_bands)
        mfccsscaled = np.mean(mfccs.T,axis=0)
        
    except Exception as e:
        print("Error encountered while parsing file: ", e)
        return None 

    # Return the MFCC
    return mfccsscaled

# Create an empty array with the features that are about to be generated
features = []

# =========================================================================================================
# THE FOLLOWING THING IS A 'WINDOWS' THING'. WHEN USING MAC OR LINUX, COPY PASTE THE FOLLOWING CODE IN HERE
# =========================================================================================================

'''
for className in os.listdir('./samples'):
    # Every directory is a classifier
    # Then loop through every audio file in that directory
    for fileName in os.listdir('./samples/' + className):
        # Generate the MFCC for the given audio file
        data = extract_features('./samples/' + className + '/' + fileName)

        # Then store the resulting MFCC in the feature array under the
        # classification of the parent classifier
        features.append([data, className])

# Retrieve current working directory
path = os.getcwd() 
print(path)

# Apparently on Windows, this is the root path, therefore we change it to the right path
os.chdir("C:\\Users\\s157874\\Documents\\GitHub\\dwaai\\mfcc\\samples")
path = os.getcwd() 
print(path)

# Get the list of all files and directories 
# in current working directory 
dir_list = os.listdir(path) 

for className in os.listdir(os.getcwd()):
	
	print(className)
	# Navigate to the map called english (which contain all our english accent samples)
	if className == "english":
		for fileName in os.listdir(os.getcwd() + "\\english"):
			# Generate the MFCC for the given audio file
			data = extract_features(os.getcwd() + "\\english\\" + fileName)
			# Then store the resulting MFCC in the feature array under the
			# classification of the parent classifier
			features.append([data, className])

	# Navigate to the map called korean (which contain all our korean accent samples)
	if className == "korean":

		for fileName in os.listdir(os.getcwd() + "\\korean"):
			# Generate the MFCC for the given audio file
			data = extract_features(os.getcwd() + "\\korean\\" + fileName)
			# Then store the resulting MFCC in the feature array under the
			# classification of the parent classifier
			features.append([data, className])

# ============================================
# END OF THE 'WINDOWS THING' 
# =============================================

'''

# =========================================================================================================
# DIFFERENT DATASET: EXAMPLES DATASET: 47 DUTCH WAV FILES AND 50 ENGLISH WAVS. (THIS IS ALSO FOR WINDOWS)
# =========================================================================================================

# Retrieve current working directory
path = os.getcwd() 
print(path)

# Apparently on Windows, this is the root path, therefore we change it to the right path
os.chdir("C:\\Users\\s157874\\Documents\\GitHub\\dwaai\\mfcc\\example_datas")
path = os.getcwd() 
#print(path)

# Get the list of all files and directories 
# in current working directory 
dir_list = os.listdir(path) 

for className in os.listdir(os.getcwd()):
	
	print(className)
	# Navigate to the map called english (which contain all our english accent samples)
	if className == "Dutch_wav":
		for fileName in os.listdir(os.getcwd() + "\\Dutch_wav"):
			# Generate the MFCC for the given audio file
			data = extract_features(os.getcwd() + "\\Dutch_wav\\" + fileName)
			# Then store the resulting MFCC in the feature array under the
			# classification of the parent classifier
			features.append([data, className])

	# Navigate to the map called korean (which contain all our korean accent samples)
	if className == "English_wav":

		for fileName in os.listdir(os.getcwd() + "\\English_wav"):
			# Generate the MFCC for the given audio file
			data = extract_features(os.getcwd() + "\\English_wav\\" + fileName)
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

#===================================
#   GRADIENT BOOSTING
#===================================

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder

# Convert features and corresponding classification labels into numpy arrays
X = np.array(featuresdf.feature.tolist())
y = np.array(featuresdf.class_label.tolist())

# Split our dataset into training and testing sets
state = 0  
test_size = 0.2

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=state)
print(len(X_train), 'training instances,', len(X_test), 'testing instances')

# Scale the features on the X sets, this is a different scaler compared to RandomForest
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#Setting different learning rates and compare them afterwards
lr_list = [0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1]

for learning_rate in lr_list:

	gradient_booster_classifier = GradientBoostingClassifier(n_estimators=20, learning_rate=learning_rate, max_features=2, max_depth=2, random_state=0)
	gradient_booster_classifier.fit(X_train, y_train)
	print("Learning rate: ", learning_rate)
	print("Accuracy score (training): {0:.2f}".format(gradient_booster_classifier.score(X_train, y_train)))
	print("Accuracy score (validation): {0:.2f}".format(gradient_booster_classifier.score(X_test, y_test)))

#Evaluate the classifier by checking its accuracy and creating a confusion matrix
	gradient_booster__evaluation_classifier = GradientBoostingClassifier(n_estimators=100, learning_rate=0.5, max_features=2, max_depth=2, random_state=0)
	gradient_booster__evaluation_classifier.fit(X_train, y_train)
	predictions = gradient_booster__evaluation_classifier.predict(X_test)

	print("Confusion Matrix:")
	print(confusion_matrix(y_test, predictions))

	print("Classification Report")
	print(classification_report(y_test, predictions))


#==============================================================================
#   NEURAL NETWORK
#   ==============
#   The following code documents an attempt at making the MFCC array work with
#   Keras' 1D Convolutional Neural Network. The attempt was fruitless.
#==============================================================================

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv1D, MaxPooling1D
from keras.utils import np_utils
from keras.utils import to_categorical
from keras.layers import GaussianNoise

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

from sklearn.preprocessing import LabelEncoder

# Convert features and corresponding classification labels into numpy arrays
X = np.array(featuresdf.feature.tolist())
y = np.array(featuresdf.class_label.tolist())

# Encode the classification labels
le = LabelEncoder()
yy = to_categorical(le.fit_transform(y)) 

# split the dataset 
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, yy, test_size=0.15)

print(X_train.shape, 'After first row')
print(y_train.shape, 'y')

xts = X_train.shape
xtss = X_test.shape

X_train = np.reshape(X_train, (xts[0], xts[1], 1))
X_test = np.reshape(X_test, (xtss[0], xtss[1], 1))

print(len(X_train), 'training sequences, ', len(X_test), 'test sequences')
print(X_train.shape)

# Y_train = np_utils.to_categorical(y_train, nb_classes)
# Y_test = np_utils.to_categorical(y_test, nb_classes)

# yts = Y_train.shape
# Y_train = np.reshape(y_train, (yts[0], 1))
# ytss = y_test.shape
# Y_test = np.reshape(y_test, (ytss[0], 1))

cat = LabelEncoder()


print(y_train.shape)

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