## wav_to_mfcc.py
This is a demo demonstrating a simple way of generating MFCCs using a CLI input

1. Install packages
```
pip3 install python_speech_features numpy scipy
```

2. Run file!
```
python3 wav_to_mfcc.py <file>
```

## feature_extraction.py
A lousy attempt at building a model from a set of extracted features. Currently
using RandomForest.

### Installing stuff
```
pip3 install sklearn librosa pandas numpy scipy
```

### Running it
```
python3 feature_extraction.py
```

The script will look in a subdirectory called `samples/`. This directory should
contain multiple other directories, which are named according to their class.
These folders then contain audio files which should be transformed. After
becoming an MFCC these are used to buld a model using RandomForest.