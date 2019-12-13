#!/usr/bin/env python3

from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav
import numpy as np
import sys
from keras.layers import GaussianNoise    

# GUARD: Check if someone has supplied an argument
if len(sys.argv) < 2:
    raise Exception('No input file')

# Read an input file from the first argument on the commandline
inputFile = sys.argv[1]

# Calculate MFCC
(rate,sig) = wav.read(inputFile)
mfcc_features = mfcc(sig, rate, nfft=2048)
# d_mfcc_feat = delta(mfcc_feat, 2)
# fbank_feat = logfbank(sig,rate)

# Normalize MFCC by subtracting the mean and using standard deviation 
# In the future, we should possibly do this only with the training data
mean = np.mean(mfcc_features, axis=0)
std = np.std(mfcc_features, axis=0)
mfcc_features = (mfcc_features - mean)/std

# Print MFCC
print(mfcc_features)