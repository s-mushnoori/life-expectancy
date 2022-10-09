import numpy as np
import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore')


# Read in the data
X_train = pd.read_pickle('modified_data/X_train_engineered.pkl')
X_test = pd.read_pickle('modified_data/X_test_engineered.pkl')
y_train = pd.read_pickle('modified_data/y_train.pkl')
y_test = pd.read_pickle('modified_data/y_test.pkl')


# Import the trained model
model = pickle.load(open('model.pkl', 'rb'))


# Make predictions
y_pred = model.predict(X_test)

# Evaluate results
from sklearn.metrics import mean_squared_error, r2_score

print("MSE Score:", format(mean_squared_error(y_test, y_pred),'.3f'))
print("R2 Score:", format(r2_score(y_test, y_pred),'.3f'))