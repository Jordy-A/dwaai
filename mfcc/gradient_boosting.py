#===================================
#   GRADIENT BOOSTING
#===================================

import pandas as pd
import numpy as np
import os
import pickle
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder

# Get dataframe from folder C:\Users\s157874\Documents\GitHub\dwaai\mfcc\example_datas
featuresdf = pd.read_pickle('C:\\Users\\s157874\\Documents\\GitHub\\dwaai\\mfcc\\example_datas\\mffc_extracted_WINDOWS') 
print(featuresdf)

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
