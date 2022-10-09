import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from processing import Preprocessor, EngineerFeatures

# Read in the data
path = "raw_data/Life Expectancy Data.csv"
df = pd.read_csv(path)

# Drop rows with null values in target variable
df.dropna(subset=['Life expectancy '], inplace=True)

# Train test split
from sklearn.model_selection import train_test_split
X = df.drop('Life expectancy ', axis=1)
y = df['Life expectancy ']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# Clean data
prep = Preprocessor()
X_train_clean = prep.fit_transform(X_train)
X_test_clean = prep.transform(X_test)

# Engineer features
engg = EngineerFeatures()
X_train_engineered = engg.fit_transform(X_train_clean)
X_test_engineered = engg.transform(X_test_clean)

# Create and train linear regression model
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train_engineered, y_train)

# Save model
import pickle
pickle.dump(lm, open('model.pkl', 'wb'))

# Save engineered data and target variable
X_train_engineered.to_pickle('modified_data/X_train_engineered.pkl')
X_test_engineered.to_pickle('modified_data/X_test_engineered.pkl')
y_train.to_pickle('modified_data/y_train.pkl')
y_test.to_pickle('modified_data/y_test.pkl')