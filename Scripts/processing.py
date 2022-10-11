import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# Define Preprocessor class
class Preprocessor:

    def __init__(self):
        self.country_medians = pd.DataFrame()
        self.year_medians = pd.DataFrame()

    def fit(self, X, y=None):
        '''
        Learn information from the training data to transform the test data. 
        Only call fit on train data.
        '''
        #Calculate median values by country and year
        self.country_medians = X.groupby('Country').median().reset_index()
        self.year_medians = X.groupby('Year').median().reset_index()

        return self

    def transform(self, X, y=None):
        '''
        Use fit information if applicable and impute values to train and test data.
        '''
        X_new = X.copy()
        X_new.reset_index(inplace=True) # Temporarily reset indices

        # Replace illogical values with NaNs for later imputation
        X_new['infant deaths'] = X_new['infant deaths'].replace(0, np.nan)
        X_new['under-five deaths '] = X_new['under-five deaths '].replace(0, np.nan)

        # Drop columns with >50% missing values
        X_new.drop(' BMI ', inplace=True, axis=1)

        X_new.update(X_new[['Country']].merge(self.country_medians, on='Country',  how='left'), overwrite=False)
        X_new.update(X_new[['Year']].merge(self.year_medians, on='Year',  how='left'), overwrite=False)

        # Restore original indices
        X_new.set_index('index', inplace=True)
        X_new.index.name = None

        return X_new

    def fit_transform(self, X, y=None):
        '''
        Combines fit and transform for use in sklearn pipelines
        '''
        return self.fit(X).transform(X)
    

# Define EngineerFeatures class
class EngineerFeatures():

    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None): 
        X_new = X.copy()

        # Drop uncorrelated or unimportant features
        cols_to_drop = [
            'Country', # This column has been encoded and used for processing. It can be dropped now. 
            'Population' # Very weak correaltion to target variable
            ]
        
        X_new = X_new.drop(cols_to_drop, axis=1)

        # Feature transformations for numeric features
        # Note that skewed columns will have to be entered manually here 
        skewed_cols = [
            'Adult Mortality',
            'infant deaths', 
            'percentage expenditure', 
            'Hepatitis B',
            'Measles ', 
            'under-five deaths ',
            'Polio',
            'Diphtheria ', 
            ' HIV/AIDS', 
            'GDP',
            ' thinness  1-19 years', 
            ' thinness 5-9 years',
            'Income composition of resources'
        ]

        for col in skewed_cols:
            X_new[col] = np.log1p(X_new[col])

        # Feature encoding
        cols_to_encode = [
            'Status'
        ]
        
        X_new = pd.get_dummies(X_new, columns=cols_to_encode, drop_first=True)

        return X_new

    def fit_transform(self, X, y=None):
        return self.fit(X).transform(X)