#===================================
#   RANDOM FOREST
#===================================

import pickle
import pandas as pd
import numpy as np
import os
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Get dataframe from folder C:\Users\s157874\Documents\GitHub\dwaai\mfcc\example_datas
featuresdf = pd.read_pickle('C:\\Users\\s157874\\Documents\\GitHub\\dwaai\\mfcc\\example_datas\\mffc_extracted_WINDOWS') 
print(featuresdf)

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
