"""Example: Forecasting Employee Outflow."""

# # Employee Churn Prediction

# +
import io
import os
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

# import plotly.express as px
import seaborn as sns
from dotenv import load_dotenv
from scipy.stats import f_oneway

# LDA model
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier

# selector object that will use the random forest classifier
# to identify feature importance > 0.10
from sklearn.feature_selection import SelectFromModel

# Logistic Regression
from sklearn.linear_model import LogisticRegression

# performance measurement
# performance measurement
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

# feature scaling
# transforming 'salary' catogories into 'int'
# trying Yeo-Johnson transformation
from sklearn.preprocessing import LabelEncoder, PowerTransformer, StandardScaler

# fmt: off
from statsmodels.stats.outliers_influence import variance_inflation_factor
# -

# ## Introduction

# ### Project outline
#
# The purpose of this project is to create a model that will predict whether an employee is likely to stay with the company or leave it based on some of his or her characteristics. The features are given in the Codebook.
#
# As the response variable is a dichotomous categorical variable, three models will be used to predict the outcome: Linear Discriminant Analysis (LDA), Logistic Regression and Random Forest Classifier and then the performance of these models will be compared.

# ### Codebook
#
# ```markdown
# Feature                 | Description
# ------------------------|------------------
# `satisfaction_level`    | Employee satisfaction level
# `Last_evaluation`       | Last evaluation score
# `number_projects`       | Number of projects assigned to
# `average_monthly_hours` | Average monthly hours worked
# `time_spend_company`    | Time spent at the company
# `work_accident`         | Whether they have had a work accident
# `left`                  | Whether or not employee left company
# `promotion_last_5years` | Whether they have had a promotion in the last 5 years
# `department`            | Department name
# `salary`                | Salary category
# ```

# ## EDA and preprocessing

# ### Loading and inspecting the data

# +
load_dotenv()

hr_csv_url = os.environ.get("HR_CSV_URL", "")
response = requests.get(hr_csv_url)
df = pd.read_csv(io.BytesIO(response.content))
df.head()
# -

df.info()

# missing values per feature
np.round(df.isna().sum() / len(df), 2)

# **Conclusion**. This dataset contains eight explanatory variables and one response variable with information on 14,999 employees. There are no missing values in this dataset.

# ### Categorical features

# #### Work accident

# +
# Work_accident vs. left in percentages
outcome_work_accident = pd.crosstab(
    index=df["left"], columns=df["Work_accident"], normalize="index"
)  # percentages based on index

outcome_work_accident.index = pd.Index(["Did not leave", "Left"])
outcome_work_accident

# +
outcome_work_accident.plot(kind="bar", stacked=True)

plt.title("Work_accident vs. left")
plt.xlabel("Outcome")
plt.ylabel("Employees")
plt.xticks(rotation=0, horizontalalignment="center")

plt.show()
# -

# Fewer accidents among those who left

# #### Promotion in the last 5 years

# +
# promotion_last_5years vs. left in percentages
outcome_promotion_last_5years = pd.crosstab(
    index=df["left"], columns=df["promotion_last_5years"], normalize="index"
)

outcome_promotion_last_5years.index = pd.Index(["Did not leave", "Left"])
outcome_promotion_last_5years

# +
outcome_promotion_last_5years.plot(kind="bar", stacked=True)

plt.title("promotion_last_5years vs. left")
plt.xlabel("Outcome")
plt.ylabel("Employees")
plt.xticks(rotation=0, horizontalalignment="center")

plt.show()
# -

# Almost no promotion among those who left.

# #### Department

# +
# department vs. left in percentages
outcome_department = pd.crosstab(
    index=df["left"], columns=df["department"], normalize="index"
)

outcome_department.index = pd.Index(["Did not leave", "Left"])
outcome_department

# +
outcome_department.plot.barh(stacked=True)

plt.title("department vs. left")
plt.xlabel("Employees")
plt.ylabel("Outcome")
plt.xticks(rotation=0, horizontalalignment="center")
plt.show()
# -

# number of employees by department
df["department"].value_counts()

# +
plt.figure(figsize=(10, 5))

chart = sns.countplot(data=df, x="department")

chart.set_xticks(list(range(1, len(df["department"].value_counts()) + 1)))
chart.set_xticklabels(
    chart.get_xticklabels(),
    rotation=45,
    horizontalalignment="right",
    fontweight="light",
    fontsize="large",
)

plt.show()
# -

# Most people work for sales, technical and support departments. Broken down by department, fairly similar distribution among those who left and those who did not leave.

# #### Salary

# salary counts
df["salary"].value_counts()

sns.countplot(x="salary", data=df)
plt.show()

# +
# salary vs. department in percentages
salary_dept = pd.crosstab(
    index=df["department"], columns=df["salary"], normalize="index"
)

salary_dept

# +
salary_dept.plot.barh(stacked=True)

plt.title("salary vs. department")
plt.xlabel("Salary")
plt.ylabel("Department")
plt.xticks(rotation=0, horizontalalignment="center")

plt.show()

# +
# salary vs. left in percentages
outcome_salary = pd.crosstab(index=df["left"], columns=df["salary"], normalize="index")

outcome_salary.index = pd.Index(["Did not leave", "Left"])
outcome_salary

# +
outcome_salary.plot(kind="bar", stacked=True)

plt.title("salary vs. left")
plt.xlabel("Outcome")
plt.ylabel("Employees")
plt.xticks(rotation=0, horizontalalignment="center")

plt.show()
# -

# Low and medium level salary employees significantly outnumber high salary employees. More or less equal distribution of salaries across departments except for managers who have a larger proportion of high salaries. Fewer people with high and medium salary leave.

# #### Time spent in the company

# +
# time_spend_company vs. left in percentages
outcome_time_spend_company = pd.crosstab(
    index=df["left"], columns=df["time_spend_company"], normalize="index"
)

outcome_time_spend_company.index = pd.Index(["Did not leave", "Left"])
outcome_time_spend_company

# +
outcome_time_spend_company.plot.barh(stacked=True)

plt.title("time_spend_company vs. left")
plt.xlabel("Time spent, in years")
plt.ylabel("Outcome")

plt.show()
# -

# Those who work for 2, 7, 8 and 9 years almost always stay.

# #### Number of projects

# mean number_project vs. left
proj_left = df.groupby("left").number_project.mean()
proj_left

# +
proj_left.plot(kind="bar", stacked=True)

plt.title("number_project vs. left")
plt.xlabel("Left")
plt.ylabel("number_project")
plt.xticks(rotation=0, horizontalalignment="center")

plt.show()
# -

# Mean number of projects' bar plot not very informative.

# +
# number_project vs. left in percentages
outcome_number_project = pd.crosstab(
    index=df["left"], columns=df["number_project"], normalize="index"
)

outcome_number_project.index = pd.Index(["Did not leave", "Left"])
outcome_number_project

# +
outcome_number_project.plot.barh(stacked=True)

plt.title("number_project vs. left")
plt.xlabel("Number of projects")
plt.ylabel("Outcome")

plt.show()
# -

# **Conclusion for categorical variables:** among categorical variables `promotion_last_5years`, `salary`, `time_spend_company`, `number_project` may become good predictors for the model. It is interesting to note that people who had more work related accidents tend to stay more often.

# ### Numerical features

# #### Summary statistics

df[["satisfaction_level", "last_evaluation", "average_montly_hours"]].describe()

# Mean and median are quite close. It appears there is no significant skew or ouliers in the distributions.

# #### Satisfaction level

# +
a_var, (ax_box, ax_hist) = plt.subplots(
    2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)}
)

sns.boxplot(x=df["satisfaction_level"], ax=ax_box)
sns.histplot(x=df["satisfaction_level"], ax=ax_hist, bins=10, kde=True)

ax_box.set(xlabel="")
ax_hist.set(xlabel="satisfaction_level distribution")
ax_hist.set(ylabel="frequency")

plt.show()
# -

# Quite a lot of unsatisfied employees.

# +
# trying log transformation
a_var, (ax_box, ax_hist) = plt.subplots(
    2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)}
)

sns.boxplot(x=df["satisfaction_level"], ax=ax_box)
sns.histplot(x=df["satisfaction_level"], ax=ax_hist, bins=10, kde=True).set_yscale(
    "log"
)

ax_box.set(xlabel="")
ax_hist.set(xlabel="satisfaction_level distribution (log)")
ax_hist.set(ylabel="frequency")

plt.show()

# +
power = PowerTransformer(method="yeo-johnson", standardize=True)
sat_trans = power.fit_transform(df[["satisfaction_level"]])
sat_trans = pd.DataFrame(sat_trans)
sat_trans.hist(bins=20)

plt.show()
# -

# satisfaction level vs. left
sat_left = df.groupby("left").satisfaction_level.mean()
sat_left

# +
sat_left.plot(kind="bar", stacked=True)

plt.title("satisfaction_level vs. left")
plt.xlabel("Left")
plt.ylabel("satisfaction_level")
plt.xticks(rotation=0, horizontalalignment="center")

plt.show()
# -

# Those who left are significantly less satisfied.

# satisfaction level by department
sat_dept = df.groupby("department").satisfaction_level.mean().sort_values()
sat_dept

sat_dept.plot.barh(stacked=True)
plt.title("satisfaction_level by department")
plt.xlabel("satisfaction_level")
plt.ylabel("department")
plt.xticks(rotation=0, horizontalalignment="center")
plt.xlim(0.55, 0.65)
plt.show()

# Accountants, HR and technical people are visibly less satisfied.

# #### Last evaluation

# +
a_var, (ax_box, ax_hist) = plt.subplots(
    2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)}
)

sns.boxplot(x=df["last_evaluation"], ax=ax_box)
sns.histplot(x=df["last_evaluation"], ax=ax_hist, bins=15, kde=True)

ax_box.set(xlabel="")
ax_hist.set(xlabel="last_evaluation distribution")
ax_hist.set(ylabel="frequency")

plt.show()
# -

# Bimodal distribution.

# +
# trying log transformation
a_var, (ax_box, ax_hist) = plt.subplots(
    2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)}
)

sns.boxplot(x=df["last_evaluation"], ax=ax_box)
sns.histplot(x=df["last_evaluation"], ax=ax_hist, bins=15, kde=True).set_yscale("log")

ax_box.set(xlabel="")
ax_hist.set(xlabel="last_evaluation distribution (log)")
ax_hist.set(ylabel="frequency")

plt.show()

# +
# trying Yeo-Johnson transformation
power = PowerTransformer(method="yeo-johnson", standardize=True)

eval_trans = power.fit_transform(df[["last_evaluation"]])
eval_trans = pd.DataFrame(eval_trans)
eval_trans.hist(bins=20)

plt.show()
# -

# last_evaluation vs. left
eval_left = df.groupby("left").last_evaluation.mean()
eval_left

# +
eval_left.plot(kind="bar", stacked=True)

plt.title("last_evaluation  vs. left")
plt.xlabel("left")
plt.ylabel("last_evaluation")
plt.xticks(rotation=0, horizontalalignment="center")
plt.ylim(0.7, 0.74)

plt.show()
# -

# The difference is extremely small.

# #### Average monthly hours

# +
a_var, (ax_box, ax_hist) = plt.subplots(
    2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)}
)

sns.boxplot(x=df["average_montly_hours"], ax=ax_box)
sns.histplot(x=df["average_montly_hours"], ax=ax_hist, bins=15, kde=True)

ax_box.set(xlabel="")
ax_hist.set(xlabel="average_montly_hours distribution")
ax_hist.set(ylabel="frequency")

plt.show()
# -

# Bimodal distribution.

# +
# trying log transformation
a_var, (ax_box, ax_hist) = plt.subplots(
    2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)}
)

sns.boxplot(x=df["average_montly_hours"], ax=ax_box)
sns.histplot(x=df["average_montly_hours"], ax=ax_hist, bins=15, kde=True).set_yscale(
    "log"
)

ax_box.set(xlabel="")
ax_hist.set(xlabel="average_montly_hours distribution (log)")
ax_hist.set(ylabel="frequency")

plt.show()

# +
# trying Yeo-Johnson transformation
power = PowerTransformer(method="yeo-johnson", standardize=True)

hours_trans = power.fit_transform(df[["average_montly_hours"]])
hours_trans = pd.DataFrame(hours_trans)
hours_trans.hist(bins=20)

plt.show()
# -

# average_montly_hours vs. left
hours_left = df.groupby("left").average_montly_hours.mean()
hours_left

# +
hours_left.plot(kind="bar", stacked=True)

plt.title("average_montly_hours vs. left")
plt.xlabel("left")
plt.ylabel("average_montly_hours")
plt.xticks(rotation=0, horizontalalignment="center")
plt.ylim(150, 220)

plt.show()
# -

# **Conclusion for numerical variables:**. Numerical variables require log transformation for better prediction. Yeo-Johnson transformation did not show good results. `satisfaction_level` and `average_montly_hours` may propably be used in the model.

# #### Outliers

# +
# satisfaction_level outliers
q1 = df.satisfaction_level.quantile(0.25)
q3 = df.satisfaction_level.quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
print(lower_bound, upper_bound)

outliers_sat = df[
    (df.satisfaction_level < lower_bound) | (df.satisfaction_level > upper_bound)
]
outliers_sat.head()
# -

# There are no outliers as boundaries exceed min and max values.

# +
# last_evaluation outliers
q1 = df.last_evaluation.quantile(0.25)
q3 = df.last_evaluation.quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
print(lower_bound, upper_bound)

eval_outliers = df[
    (df.last_evaluation < lower_bound) | (df.last_evaluation > upper_bound)
]
eval_outliers.head()
# -

# There are no outliers as boundaries exceed min and max values.

# +
# average_montly_hours outliers
q1 = df.average_montly_hours.quantile(0.25)
q3 = df.average_montly_hours.quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
print(lower_bound, upper_bound)

hours = df[
    (df.average_montly_hours < lower_bound) | (df.average_montly_hours > upper_bound)
]
hours.head()
# -

# There are no outliers as boundaries exceed min and max values.

# ### Data investigation

# #### Hypothesis 1
#
# We will test the hypothesis that people with high `salary` have higher `average_montly_hours`.

# looking at the means
sal_hours = df.groupby("salary").average_montly_hours.mean().sort_values()
sal_hours

# +
sal_hours.plot.barh(stacked=True)

plt.title("average_montly_hours by salary")
plt.xlabel("average_montly_hours")
plt.ylabel("salary")
plt.xticks(rotation=0, horizontalalignment="center")
plt.xlim(190, 208)

plt.show()
# -

# Actually, those who have a medium salary appear to work slightly longer hours being the difference though quite small. We can test whether there is a statistically significant difference with ANOVA.

# +
# splitting data into three samples
low = df[df["salary"] == "low"]
low = low[["average_montly_hours"]]

medium = df[df["salary"] == "medium"]
medium = medium[["average_montly_hours"]]

high = df[df["salary"] == "high"]
high = high[["average_montly_hours"]]
# -

# size of each sample
print(len(low), len(medium), len(high))

f_oneway(low, medium, high)

# The size of the samples is quite significant so we would expect the test to detect even small differences. Nevertheless, p-value is still greater than 0.05 and thus ANOVA shows that there is no significant difference between `average_montly_hours` in terms of salary.

# ### Data Transformation

# +
# basic assumption for LDA is that numeric variables have to be normal
# log transformation of numerical variables
df["sat_level_log"] = np.log(df["satisfaction_level"])
df["last_eval_log"] = np.log(df["last_evaluation"])
df["av_hours_log"] = np.log(df["average_montly_hours"])

# changing column order
columns_titles = [
    "satisfaction_level",
    "sat_level_log",
    "last_evaluation",
    "last_eval_log",
    "number_project",
    "average_montly_hours",
    "av_hours_log",
    "time_spend_company",
    "Work_accident",
    "promotion_last_5years",
    "department",
    "salary",
    "left",
]
df = df.reindex(columns=columns_titles)
# -

labelencoder = LabelEncoder()
df["salary"] = labelencoder.fit_transform(df["salary"])

# transforming 'deparment' catogories into 'int'
labelencoder = LabelEncoder()
df["department"] = labelencoder.fit_transform(df["department"])

df.head()

# ### Correlation Analysis

# Kendall correlation method will be used for the correlation analysis.

# +
df_c = df[
    [
        "satisfaction_level",
        "sat_level_log",
        "last_evaluation",
        "last_eval_log",
        "number_project",
        "average_montly_hours",
        "av_hours_log",
        "time_spend_company",
        "Work_accident",
        "promotion_last_5years",
        "salary",
    ]
]

# df_c.corr()

# +
# Kendall Correlation matrix
plt.figure(figsize=(12, 10))

cor = df_c.corr(method="kendall")

ax = sns.heatmap(
    cor, annot=True, vmin=-1, vmax=1, center=0, cmap=plt.cm.Reds
)  # cmap = sns.diverging_palette(20, 220, n = 200)

ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment="right")

plt.show()
# -

# largest and smallest correlation
c_var = df_c.corr(method="kendall").abs()
d_var = c_var.unstack()
so = d_var.sort_values(kind="quicksort")  # type: ignore[call-overload]

print(so[-22:-17])

print(so[:4])

# The two lowest correlations include `salary` and `Work_accident`, and `number_project` and `Work_accident`.

# ### Multicollinearity analysis

# +
warnings.filterwarnings("ignore")

# Getting variables for which to compute VIF and adding intercept term
e_var = df[
    [
        "satisfaction_level",
        "last_eval_log",
        "number_project",
        "average_montly_hours",
        "time_spend_company",
        "Work_accident",
        "promotion_last_5years",
    ]
]

e_var["Intercept"] = 1

# +
# X.head()

# +
# Compute and view VIF
vif = pd.DataFrame()
vif['variables'] = e_var.columns
vif["VIF"] = [
    variance_inflation_factor(e_var.values, i)
    for i in range(e_var.shape[1])
]

# View results using print
print(vif)
# fmt: on
# -

# As VIF is closer to 1, we can say that there is moderate correlation between explanatory variables.

# ## Modelling

# ### Linear Discriminant Analysis

# trying different features
df_model = df[
    [
        "satisfaction_level",
        "last_eval_log",
        "number_project",
        "average_montly_hours",
        "time_spend_company",
        "Work_accident",
        "promotion_last_5years",
    ]
]

X_train, X_test, y_train, y_test = train_test_split(
    df_model, df["left"], test_size=0.30, random_state=42
)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)

# making prediction
lda.predict(X_test)

accuracy_score(y_test, lda.predict(X_test))

# ### Logistic Regression

# trying different features
df_model_2 = df[
    [
        "satisfaction_level",
        "last_eval_log",
        "number_project",
        "average_montly_hours",
        "time_spend_company",
        "Work_accident",
        "promotion_last_5years",
    ]
]

X_train, X_test, y_train, y_test = train_test_split(
    df_model_2, df["left"], test_size=0.30, random_state=42
)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

lr = LogisticRegression(random_state=42)
lr.fit(X_train, y_train)

print(confusion_matrix(y_test, lr.predict(X_test)))
print(accuracy_score(y_test, lr.predict(X_test)))

# ### Random Forest Classifier

# trying different features
df_model_3 = df[
    [
        "satisfaction_level",
        "last_eval_log",
        "number_project",
        "average_montly_hours",
        "time_spend_company",
        "Work_accident",
        "promotion_last_5years",
        "department",
        "salary",
    ]
]

X_train, X_test, y_train, y_test = train_test_split(
    df_model_3, df["left"], test_size=0.30, random_state=42
)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# +
classifier = RandomForestClassifier(
    criterion="gini",
    n_estimators=100,
    max_depth=9,
    random_state=42,
    n_jobs=-1,
)

classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
# -

# test performance measurement
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))

# Trying **feature selection** to reduce the variance of the model, and therefore overfitting.

feat_labels = [
    "satisfaction_level",
    "last_eval_log",
    "number_project",
    "average_montly_hours",
    "time_spend_company",
    "Work_accident",
    "promotion_last_5years",
    "department",
    "salary",
]

# name and gini importance of each feature
for feature in zip(feat_labels, classifier.feature_importances_):
    print(feature)

# +
sfm = SelectFromModel(classifier, threshold=0.10)

# training the selector
sfm.fit(X_train, y_train)
# -

# names of the most important features
for feature_list_index in sfm.get_support(indices=True):
    print(feat_labels[feature_list_index])

# transforming the data to create a new dataset containing only
# the most important features
X_important_train = sfm.transform(X_train)
X_important_test = sfm.transform(X_test)

# +
# new random forest classifier for the most important features
clf_important = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)

# new classifier on the new dataset containing the most important features
clf_important.fit(X_important_train, y_train)

# +
# applying the full featured classifier to the test data
y_important_pred = clf_important.predict(X_important_test)

# view the accuracy of limited feature model
accuracy_score(y_test, y_important_pred)
# -

# ## Conclusion

# In this research we decided to compare LDA, Logistic Regression and Random Forest Classifier models. As the data are highly skewed, sometimes bimodal and include categorical variables, the Random Forest Classifier model performed the best with an accuracy of 97.7%. Feature importance selection allowed to improve the accuracy up to 98.9% and at the same time reduced the complexity of the model.
