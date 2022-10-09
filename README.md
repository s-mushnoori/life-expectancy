# life-expectancy
Predicting life expectancy based on [WHO data](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who).

Notebooks used for protoyping are available in the [`Notebooks`](https://github.com/s-mushnoori/life-expectancy/tree/main/Notebooks) folder.

Refactored scripts are available in the [`Scripts`](https://github.com/s-mushnoori/life-expectancy/tree/main/Scripts) folder. 

---

# Instructions for use

1. Navigate to the [`Scripts`](https://github.com/s-mushnoori/life-expectancy/tree/main/Scripts) folder and download the contents into your working directory. 
2. Ensure that [`processing.py`](https://github.com/s-mushnoori/life-expectancy/blob/main/Scripts/processing.py), [`create_model.py`](https://github.com/s-mushnoori/life-expectancy/blob/main/Scripts/create_model.py), and [`evaluate.py`](https://github.com/s-mushnoori/life-expectancy/blob/main/Scripts/evaluate.py) are in the same location.
3. Run `pcreate_model.py` in your preferred IDE to create the model.
4. Run `evaluate.py` to get the evaluation metrics for the model. 

---

# Table of Contents
1. &nbsp; **Thought Process**

2. &nbsp; **Data Cleaning**

3. &nbsp; **Exploratory Data Analysis**

4. &nbsp; **Feature Engineering**
  
5. &nbsp; **Model Training**

6. &nbsp; **Refactoring**

7. &nbsp; **Thoughts and Future Considerations**

---
## 1. &nbsp; Thought Process
For this take-home assignment, we are tasked with building a linear regression model to predict the life expectancy of a country, and test it on the most recent data. The dataset contains life expectancy data along with several other features for 193 countries over a 15 year period. However, not all countries have data for all 15 years. 

#### The problem statement can be interpreted as:
1. _predict the life expectancy of a country_ : We should combine the data for all years but the most recent, and
2. _test it on the most recent data_ : Use the test set as the subset of the data where the year is 2015 (most recent year in the dataset)

#### However, there are a few issues with this approach:
1. If we were to aggregate data from 14 years for the train set and use data from the most recent year for the test set, we are reducing the number of training samples we have available by  a factor of 10: from >2000 to <200.
2. If we were to leave `'Country'` as a variable, we would have to encode it, meaning we'd be adding 192 extra features. We could start running into dimensionality issues at this point.
3. If we were to explicitly choose data with `'Year'` as 2015 as the test set, our test set would only have 193 rows. This seems a little too low since typically tests sets are chosen to be around 25% to 33% of the dataset.

#### In light of this, we will choose a simpler approach to the problem:
1. We will ignore `'Country'` as a feature for now, and create a model based on the entire dataset. 
    - Since index values are preserved, we can later associate the datapoints with the country if required.
2. We will also not aggregate yearly data and preserve the size of our dataset. 
3. The problem statement will hence be interpreted as "predict the life expectancy based on available features," and we will ignore the country specific and year specific components. 


---
## 2. &nbsp; Data Cleaning
Prototyping and more in-depth explanations can be found in the Jupyter notebook [here](https://github.com/s-mushnoori/life-expectancy/blob/main/Notebooks/1_cleaning.ipynb).

We will now begin the data cleaning process, arguably the most important part of a data science pipeline. Descriptions for each of the features was not available so I made a best guess as to what the column represent. This information is useful to know how to potentially deal with anomalies in some features. 

Column values were modified to be logically consistent. One column was found to have >55% missing values, and was dropped. For all other columns, missing values were first imputed based on the median value for that _country_. The remaining missing values were imputed with the median value for that _year_ (across all countries). This was the best way to preserve data quality as well as avoid dropping too many rows. More detail can be found in the link above. 

Note that we always want to train test split the data BEFORE imputing missing values. This is to avoid data leakage. We want to calculate our median based _only_ on the training data, and impute that information to both the train and test set. 

To this end, a preprocessor class was written to efficiently calculate and impute missing values. 

---
## 3. &nbsp; Exploratory Data Analysis
EDA and in-depth explanations can be viewed [here](https://github.com/s-mushnoori/life-expectancy/blob/main/Notebooks/2_EDA.ipynb). The results of the EDA are summarized below:

The purpose of EDA is to understand our dataset better. Here we noticed some expected trends such as an inverse correlation between life expectancy and infant mortality rate. 
We also saw some unexpected trends such as a direct (albeit weak) correlation between net alcohol consumption per capita and life expectancy!

Next, we saw that several features are heavily skewed. This was later dealt with to improve model performance. 

We also noted that some of the independent features were strongly correlated. This will need further exploration, but for the purposes of this assignment, removing correlated features (multicollinearity) did not improve model performance, so they were ultimately left in the dataset. 

---
## 4. &nbsp; Feature Engineering
Prototyping for feature engineering can be found [here](https://github.com/s-mushnoori/life-expectancy/blob/main/Notebooks/3_feature_engineering.ipynb)

The next step is to use the information we gathered from EDA and engineer our features in some way to improve performance. We had two main components to our feature engineering process: **feature transformation** and **feature encoding**.

1. **Feature transformation:** As we saw in the EDA section, our features are pretty skewed. To deal with this, we applied a log transform which significantly reduced the skew and brought them closer to a normal distribution. 

2. **Feature encoding:** There was one feature `'Status'` which was encoded into two resulting columns, 'Developed' and 'Developing'. Arguably the feature `'Year`' is an ordinal variable and can also be encoded, but this was not done here. 

Once again a feature engineering class was written to achieve our egineering goals and also modularize the code. 

---
## 5. &nbsp; Model Training
For this assignment, we are only required to train a linear regression model. There is no hyperparameter tuning involved, so model training was a simple process. Mean squared error and R^2 were used as our evaluation metrics. 

An **MSE of ~15** years and an **R^2 of ~0.85** was consistently obtained. Not bad for a quick baseline model. 

As an added bonus, the prototyping notebook found [here](https://github.com/s-mushnoori/life-expectancy/blob/main/Notebooks/4_model_training.ipynb) also has some additional code to train, hyperparameter tune, and evaluate multiple models. This code can be built on at a later stage if we wish to productionalize the code in any capacity. 

---
## 6. &nbsp; Refactoring
With all our prototyping done, the code was modularized and refactored into python scripts, which can be found [here](https://github.com/s-mushnoori/life-expectancy/tree/main/Scripts). 

---
## 7. &nbsp; Thoughts and Future Considerations
Having worked on this end-to-end project, I have some thoughts for future iterations:

1. Column names in the dataset are quite odd, for example, inconsistent capitalization and spaces. This should be standardized in the event that we want to update the project with fresh incoming data. 
2. In the model evaluation phase, scaling did not seem to work. This is likely due to improper implementation on my end. In the interest of time, I did not fully debug this, but I would like to revisit this in the future and figure out why scaling did not immpact the results at all. 
3. I did not containerize this code, which could lead to issues running the scripts. Future projects should put some work into using virtual environments and containers to prevent software version conflicts. 
