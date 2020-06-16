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
1.import numpy as np
2.import pandas as pd
3.#import os
4.from matplotlib import pyplot as plt
5.from sklearn import preprocessing
6.from sklearn.preprocessing import StandardScaler
7.from sklearn.model_selection import train_test_split
8.from sklearn.linear_model import LinearRegression
9.from sklearn.tree import DecisionTreeRegressor
10.from sklearn.ensemble import RandomForestRegressor
11.import seaborn as sns

We have used Random Forest algorithm because it gives more accuracy then Linear Regression and Decision Tree. Accuracy of this project is 82.62%
