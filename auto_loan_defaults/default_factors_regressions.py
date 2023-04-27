import pandas as pd
import numpy as np
import math

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import StandardScaler


# Regression for primary/secondary loan info
print("\nPRIMARY-SECONDARY LOAN INFO:")
df = pd.read_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\\"
                 r"Capstone Project\Loan Defaults\Datasets\Datasets\disbursals_dt_frame_csv.csv")

# Shuffling Data
df = df.sample(frac=1)

# Dropping unnecessary columns
df.drop(["Unnamed: 0"], axis=1, inplace=True)

# Checking for correlation among IV's
corr = df.corr()
corr.to_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\\"
            r"Capstone Project\Loan Defaults\Datasets\Datasets\pri_sec_correlations.csv")

# Dropping columns too closely correlated with those deemed more indicative of default status
df.drop(["PRI.NO.OF.ACCTS", "SEC.NO.OF.ACCTS", "SEC.DISBURSED.AMOUNT"], axis=1, inplace=True)

# Creating variables
x_raw = df.copy()
x_raw.drop(["loan_default"], axis=1, inplace=True)
y = np.ravel(df[["loan_default"]])

# Standardizing independent variables
s_scaler = StandardScaler()
x = s_scaler.fit_transform(x_raw)

# Implementing logistic regression
lr = LogisticRegression()

# Splitting data into training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

# fitting model
lr.fit(x_train, y_train)

# predicting
y_pred = lr.predict(x_test)

# Results
print("Regression results with standardized variables: \nConfusion matrix:")

cnf_mat = metrics.confusion_matrix(y_test, y_pred)
print(cnf_mat)

tp, fp, fn, tn = cnf_mat[0][0], cnf_mat[0][1], cnf_mat[1][0], cnf_mat[1][1]

reg_accuracy = round((tp + tn) / (tp + fp + fn + tn) * 100, 2)

print(f"The confusion matrix indicates prediction accuracy of {reg_accuracy}%.")

print("Intercept:")

intercept = float(lr.intercept_)

odds_at_intercept = round((math.e ** intercept/(1 + math.e ** intercept)) * 100, 2)

print(f"The intercept is {intercept}, meaning that when all variables have a value of 0, there is a "
      f"{odds_at_intercept}% chance of default.", "\n\n")

print("Coefficients:")

coefficients = list(lr.coef_)

coef_list = []
for i in coefficients:
    for val in i:
        coef_list.append(val)

variables = list(x_raw.columns)

zipped_results = (zip(variables, coef_list))

percentages = []
for a, b in zipped_results:
       pct_change = round((math.e ** b - 1) * 100, 2)
       percentages.append(pct_change)
       print(f"The coefficient of {a} is {b}, meaning that every increase of 1 standard deviation  in {a} "
             f"implies a change of {pct_change}% in the likelihood of default.")

# Creating frame to use for Tableau Visualization
indices = range(0, len(variables))
list_of_tuples = list(zip(indices, variables, coef_list, percentages))
loans_coef_frame = pd.DataFrame(list_of_tuples, columns=["Column1", "Variable", "Coefficient", "Pct.Change"])
loans_coef_frame.to_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\\"
                        r"Capstone Project\Loan Defaults\Datasets\Datasets\loan_coefficients.csv")
print("\n\n")

# Regression for credit history
print("CREDIT HISTORY:")

df = pd.read_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\\"
                 r"Capstone Project\Loan Defaults\Datasets\Datasets\cred_hist_csv.csv")

# Shuffling Data
df = df.sample(frac=1)

# Dropping unnecessary columns
df.drop(["Unnamed: 0"], axis=1, inplace=True)

# Creating variables
x_raw = df.copy()
x_raw.drop(["loan_default"], axis=1, inplace=True)
y = np.ravel(df[["loan_default"]])

# Standardizing independent variables
s_scaler = StandardScaler()
x = s_scaler.fit_transform(x_raw)

# Implementing logistic regression
lr = LogisticRegression()

# Splitting data into training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

# fitting model
lr.fit(x_train, y_train)

# predicting
y_pred = lr.predict(x_test)

# Results
print("Regression results with standardized variables: \nConfusion matrix:")

cnf_mat = metrics.confusion_matrix(y_test, y_pred)
print(cnf_mat)

tp, fp, fn, tn = cnf_mat[0][0], cnf_mat[0][1], cnf_mat[1][0], cnf_mat[1][1]

reg_accuracy = round((tp + tn) / (tp + fp + fn + tn) * 100, 2)

print(f"The confusion matrix indicates prediction accuracy of {reg_accuracy}%.")

print("Intercept:")

intercept = float(lr.intercept_)

odds_at_intercept = round((math.e ** intercept/(1 + math.e ** intercept)) * 100, 2)

print(f"The intercept is {intercept}, meaning that when all variables have a value of 0, there is a "
      f"{odds_at_intercept}% chance of default.", "\n\n")

print("Coefficients:")

coefficients = list(lr.coef_)

coef_list = []
for i in coefficients:
    for val in i:
        coef_list.append(val)

variables = list(x_raw.columns)

zipped_results = (zip(variables, coef_list))

percentages = []
for a, b in zipped_results:
       pct_change = round((math.e ** b - 1) * 100, 2)
       percentages.append(pct_change)
       print(f"The coefficient of {a} is {b}, meaning that every increase of 1 standard deviation  in {a} "
             f"implies a change of {pct_change}% in the likelihood of default.")

# Creating frame to use for Tableau Visualization
indices = range(0, len(variables))
list_of_tuples = list(zip(indices, variables, coef_list, percentages))
cred_hist_coef_frame = pd.DataFrame(list_of_tuples, columns=["Column1", "Variable", "Coefficient", "Pct.Change"])
cred_hist_coef_frame.to_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\\"
                            r"Capstone Project\Loan Defaults\Datasets\Datasets\cred_hist_coefficients.csv")
print("\n\n")

# Regression for all info
print("OVERALL REGRESSION:")

df = pd.read_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\\"
                 r"Capstone Project\Loan Defaults\Datasets\Datasets\numeric_data_csv.csv")

# Shuffling Data
df = df.sample(frac=1)

# Dropping unnecessary columns
df.drop(["Unnamed: 0"], axis=1, inplace=True)

# Creating variables
x_raw = df.copy()
x_raw.drop(["loan_default"], axis=1, inplace=True)
y = np.ravel(df[["loan_default"]])

# Standardizing independent variables
s_scaler = StandardScaler()
x = s_scaler.fit_transform(x_raw)

# Implementing logistic regression
lr = LogisticRegression()

# Splitting data into training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

# fitting model
lr.fit(x_train, y_train)

# predicting
y_pred = lr.predict(x_test)

# Results
print("Regression results with standardized variables: \nConfusion matrix:")

cnf_mat = metrics.confusion_matrix(y_test, y_pred)
print(cnf_mat)

tp, fp, fn, tn = cnf_mat[0][0], cnf_mat[0][1], cnf_mat[1][0], cnf_mat[1][1]

reg_accuracy = round((tp + tn) / (tp + fp + fn + tn) * 100, 2)

print(f"The confusion matrix indicates prediction accuracy of {reg_accuracy}%.")

print("Intercept:")

intercept = float(lr.intercept_)

odds_at_intercept = round((math.e ** intercept/(1 + math.e ** intercept)) * 100, 2)

print(f"The intercept is {intercept}, meaning that when all variables have a value of 0, there is a "
      f"{odds_at_intercept}% chance of default.", "\n\n")

print("Coefficients:")

coefficients = list(lr.coef_)

coef_list = []
for i in coefficients:
    for val in i:
        coef_list.append(val)

variables = list(x_raw.columns)

zipped_results = (zip(variables, coef_list))

percentages = []
for a, b in zipped_results:
       pct_change = round((math.e ** b - 1) * 100, 2)
       percentages.append(pct_change)
       print(f"The coefficient of {a} is {b}, meaning that every increase of 1 standard deviation  in {a} "
             f"implies a change of {pct_change}% in the likelihood of default.")

# Creating frame to use for Tableau Visualization
indices = range(0, len(variables))
list_of_tuples = list(zip(indices, variables, coef_list, percentages))
overall_coef_frame = pd.DataFrame(list_of_tuples, columns=["Column1", "Variable", "Coefficient", "Pct.Change"])
overall_coef_frame.to_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\\"
                          r"Capstone Project\Loan Defaults\Datasets\Datasets\overall_coefficients.csv")
