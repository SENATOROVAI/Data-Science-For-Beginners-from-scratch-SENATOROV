"""Linear Regression(Boston dataset)."""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split

boston = fetch_openml("boston", version=1)
boston.data

boston.target
boston.data.shape

data = pd.DataFrame(boston.data)
data.head()
data.columns = boston.feature_names
data

data["Price"] = boston.target
data.head()

data.describe()

data.info()

# +
X = boston.data
y = boston.target

X["CHAS"] = X["CHAS"].astype("float64")
X["RAD"] = X["RAD"].astype("float64")

X.info()
# -

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

X_train.shape, X_test.shape

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

plt.scatter(y_test, y_pred, c="green")
plt.show()

mean_squared_error(y_pred=y_pred, y_true=y_test), mean_absolute_error(
    y_pred=y_pred, y_true=y_test
)
