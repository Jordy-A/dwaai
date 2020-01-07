no_mfcc_bands = 120

# Load various imports 
import pandas as pd
import os
import librosa
import numpy as np
import os

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
# LINE 36 T/M 87 ARE SPECIFICALLY FOR MAC OR LINUX. WHEN USING MAC OR LINUX, COPY PASTE THE FOLLOWING CODE IN HERE
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