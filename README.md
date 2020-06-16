# llSPS-INT-2868-University-Admission-Prediction
University Admission Prediction

The objective is to explore what kind of data is provided, determine the most important factors that contribute to a student's chance of admission, and select the most accurate model to predict the probability of admission.

The dataset contains information about a student's:
•	GRE Score
•	TOEFL Score
•	University Ratings
•	Statement of Purpose Score
•	Letter of Recommendation Score
•	CGPA
•	Whether the Student Has Done Any Research
•	Chance of Admission (What We're Trying to Predict)

Importing following libraries
import numpy as np
import pandas as pd
#import os
from matplotlib import pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import seaborn as sns

We have used Random Forest algorithm because it gives more accuracy then Linear Regression and Decision Tree. Accuracy of this project is 82.62%
