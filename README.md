# life-expectancy
Predicting life expectancy based on [WHO data](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who).

---

# Instructions for use

1. Navigate to the [`Scripts`](https://github.com/s-mushnoori/life-expectancy/tree/main/Scripts) folder and download the contents into your working directory. 
2. Ensure that `processing.py`, `create_model.py`, and `evaluate.py` are in the same location.
3. Run `pcreate_model.py` in your preferred IDE to create the model.
4. Run `evaluate.py` to get the evaluation metrics for the model. 

---

# Table of Contents
1. &nbsp; **Thought Process**

2. &nbsp; **Data Cleaning**

3. &nbsp; **Exploratory Data Analysis**

4. &nbsp; **Feature Engineering**
  
    4.1. &nbsp;&nbsp;&nbsp; abc
    
    4.2. &nbsp;&nbsp;&nbsp; abcd

5. &nbsp; **Model Training**

6. &nbsp; **Thoughts and Future Considerations**

---
## 1. &nbsp; Thought Process
For this take-home assignment, we are tasked with building a linear regression model to predict the life expectancy of a country, and test it on the most recent data. The dataset contains life expectancy data along with several other features for 193 countries over a 15 year period. However, not all countries have data for all 15 years. 

#### The problem statement can be interpreted as:
1. _predict the life expectancy of a country_ : We should combine the data for all years but the most recent, and
2. _test it on the most recent data_ : Use the test set as the subset of the data where the year is 2015 (most recent year in the dataset)

#### However, there are a few issues with this approach:
1. If we were to aggregate data from 14 years for the train set and use data from the most recent year for the test set, we are reducing the number of training samples we have available by  a factor of 10: from >2000 to <200.
2. If we were to leave `'Country'` as a variable, we would have to encode it, meaning we'd be adding 192 extra features. We could start running into dimensionality issues at this point.

#### In light of this, we will choose a simpler approach to the problem:
1. We will ignore `'Country'` as a feature for now, and create a model based on the entire dataset. 
    - Since index values are preserved, we can later associate the datapoints with the country if required.
2. We will also not aggregate yearly data and preserve the size of our dataset. 
3. The problem statement will hence be interpreted as "predict the life expectancy based on available features," and we will ignore the country specific and year specific components. 


---
## 2. &nbsp; Data Cleaning


---
## 3. &nbsp; Exploratory Data Analysis


---
## 4. &nbsp; Feature Engineering


---
## 5. &nbsp; Model Training


---
## 6. &nbsp; Thoughts and Future Considerations

