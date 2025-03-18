"""Titanic - Machine Learning from Disaster."""

# Uploaded on kaggle in competition

# ! pip install seaborn
# ! pip install pandas
# ! pip install numpy
# ! pip install scikit-learn

# +
# import library
# fmt: off
import pandas as pd
# to build graphs we will use the new library seaborn
import seaborn as sns
# import logistic regression from sklearn's linear_model module
from sklearn.linear_model import LogisticRegression
# import accuracy metric
# build confusion matrix
from sklearn.metrics import accuracy_score, confusion_matrix
# import StandardScaler class
from sklearn.preprocessing import StandardScaler

# fmt: on
# read train data
train = pd.read_csv("/kaggle/input/titanic/train.csv")
train.head(3)
# -

# read test data
test = pd.read_csv("/kaggle/input/titanic/test.csv")
test.head(3)

# ### Model building and forecasting
#
# #### Step 1 Data processing and analysis

# ##### Exploratory Data Analysis (EDA)

# look at the data
train.info()

# let's see how important the ticket class is for the passenger's survival
# using x and hue we can fit two categorical variables on one graph
sns.countplot(x="Pclass", hue="Survived", data=train)

# who survived more often, men or women?
sns.countplot(x="Sex", hue="Survived", data=train)

# Пропущенные значения

# identify missing values ​​using .isnull() and count them using sum()
train.isnull().sum()

# the Cabin variable (cabin number) is probably not the most important
# let's get rid of it using the .drop() method
train.drop(columns="Cabin", axis=1, inplace=True)

# but Age is more important, replace empty ​​with the arithmetic mean
train["Age"] = train["Age"].fillna(train["Age"].mean())

# we have two empty lines left in Embarked, let's delete them
train.dropna(inplace=True)

# let's see the result
train.isnull().sum()

# Категориальные переменные

# apply one-hot encoding to the variable Sex using the pd.get_dummies()
pd.get_dummies(train["Sex"]).head(3)

# download the Sex column from the train dataset again in dataframe format
previous = pd.read_csv("/kaggle/input/titanic/train.csv")[["Sex"]]
previous.head()

# encode the variable using 0 and 1
pd.get_dummies(previous["Sex"], dtype=int).head(3)

# remove the first column, it is redundant
sex = pd.get_dummies(train["Sex"], drop_first=True)
sex.head(3)

# let's do the same for the Pclass and Embarked variables
embarked = pd.get_dummies(train["Embarked"], drop_first=True)
pclass = pd.get_dummies(train["Pclass"], drop_first=True)

# append variables encoded via one-hot encoding
# to the original dataframe via the .concat() function
train = pd.concat([train, pclass, sex, embarked], axis=1)
train.head(3)

# Отбор признаков

# delete those columns that we don't need anymore
field_to_drop = ["PassengerId", "Pclass", "Name", "Sex", "Ticket", "Embarked"]
train.drop(field_to_drop, axis=1, inplace=True)
train.head(3)

# Нормализация данных

# +
# create an instance of this class
scaler = StandardScaler()

# select columns that we want to scale
cols_to_scale = ["Age", "Fare"]

# calculate mean and standard deviation for data scaling
scaler.fit(train[cols_to_scale])

# apply them
train[cols_to_scale] = scaler.transform(train[cols_to_scale])

# look at the result
train.head(3)
# -

# some column names are now numbers, this shouldn't be the case
train.columns

# convert these variables to str type using map() function
train.columns = train.columns.map(str)
train.columns

# #### Step 2 Splitting the training set into X_train and y_train

# +
# put everything except the Survived column into X_train
X_train = train.drop("Survived", axis=1)

# the 'Survived' column will be our target variable (y_train)
y_train = train["Survived"]
# -

X_train.head(3)

# #### Step 3 Training the logistic regression model

# ##### Model learning

# +
# create an instance of this class and store it in the model variable
model = LogisticRegression()

# train our model
model.fit(X_train, y_train)
# -

# ##### Make prediction on train data

y_pred_train = model.predict(X_train)

# ##### Estimation quality on test data

# +
# pass actual and predicted values to it
conf_matrix = confusion_matrix(y_train, y_pred_train)

# convert to dataframe
conf_matrix_df = pd.DataFrame(conf_matrix)
conf_matrix_df
# -

conf_matrix_labels = pd.DataFrame(
    conf_matrix,
    columns=["Прогноз погиб", "Прогноз выжил"],
    index=["Факт погиб", "Факт выжил"],
)
conf_matrix_labels

# accuracy calculation
round((479 + 237) / (479 + 237 + 70 + 103), 3)

# +
# pass actual and predicted values to it
model_accuracy = accuracy_score(y_train, y_pred_train)

# round to 3 decimal places
round(model_accuracy, 3)
# -

# ##### Step 4 Plot test data for prediction

test.info()

test.head(3)

# now we need to create a test set with the same features
# and first let's give the dataset a familiar name
X_test = test

# fill missing values in Age and Fare variables with mean values
X_test["Age"] = X_test["Age"].fillna(test["Age"].mean())
X_test["Fare"] = X_test["Fare"].fillna(test["Fare"].mean())

# perform one-hot encoding of categorical variables
sex = pd.get_dummies(X_test["Sex"], drop_first=True)
embarked = pd.get_dummies(X_test["Embarked"], drop_first=True)
pclass = pd.get_dummies(X_test["Pclass"], drop_first=True)

# +
# join new columns to the original dataframe
X_test = pd.concat([test, pclass, sex, embarked], axis=1)

# and remove data that is no longer needed
X_test.drop(
    ["PassengerId", "Pclass", "Name", "Sex", "Cabin", "Ticket", "Embarked"],
    axis=1,
    inplace=True,
)

# look at the result
X_test.head(3)
# -

# apply mean and standard deviation from training data to scale test data
X_test[cols_to_scale] = scaler.transform(X_test[cols_to_scale])
X_test.head(3)

X_test.columns = X_test.columns.map(str)

# make predictions on the test set
y_pred_test = model.predict(X_test)

# let's look at the first 10 predicted values
y_pred_test[:10]

# ##### Step 4 Save new file

# +
ids = test["PassengerId"]


result = pd.DataFrame({"PassengerId": ids, "Survived": y_pred_test})

result.head()

# +
result.to_csv("result.csv", index=False)

print("File saved successfully!")
