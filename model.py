import pandas as pd
import numpy as np
import pickle

df = pd.read_csv('Dataframe.csv')

x = np.array(df.iloc[:, :-1])
y = np.array(df.iloc[:, -1])

from sklearn.model_selection import train_test_split

# Import library
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=0)

# Fit predictor and target variable
x, y = smote.fit_resample(x, y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0, stratify = y)

from sklearn.ensemble import RandomForestClassifier
# Random Forest
print('\n --- Random Forest Model --- ')

# criterion (gini, entropy), max_depth (none, 5)
random_forest = RandomForestClassifier(n_estimators = 100, criterion = 'gini', random_state = 0)
random_forest.fit(x_train, y_train)

pickle.dump(random_forest, open('model.pkl', 'wb'))