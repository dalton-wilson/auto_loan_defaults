import pandas as pd

df = pd.read_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\Capstone Project\\"
                 r"Loan Defaults\Datasets\Datasets\auto loan default data csv.csv")

# Preliminary Data Analysis
print("\nPRELIMINARY DATA ANALYSIS:")

# Task 1: Perform preliminary data inspection and report the findings as the structure of the data, missing values,
# duplicates, etc.
print("Data structure: 233,154 observations of 41 variables")
print(df.info, "\n")

# Checking for duplicates
print("No duplicate observations: length of unique count of customer ID's matches number of data frame rows:")
print("Number of rows in dataframe: ", len(df))
print("Number of unique values in ID column: ", df.UniqueID.nunique(), "\n")

# Checking for missing values
print("7661 rows with missing data for Employment.Type variable:")
print("Data frame by column(TRUE means missing values present):\n", df.isna().any())
print("Count of rows with missing data: ", df["Employment.Type"].isna().sum(), "\n")


# Task 2: Variable names in the data may not be in accordance with the identifier naming in Python,
# so change the variable names accordingly.
# No mismatches found

# Task 3: The presented data might also contain some missing values therefore, exploration will also lead to devising
# strategies to fill in the missing values while exploring the data
# Exploring strategies for filling in missing values for Employment.Type
print("Exploring strategies for filling in missing values for Employment.Type:")
# possible elimination:
print("Rows with missing data could be eliminated, as they make up only 3.29% of all data:")
# Showing values for "Salaried," "Self employed," and NaN
num_no_emp = df["Employment.Type"].isna().sum()
num_Salaried = len(df[df["Employment.Type"] == 'Salaried'])
num_Self_emp = len(df[df["Employment.Type"] == 'Self employed'])
# Showing values for observations with and without emp.type data and total observations
print(f"Total rows with employment type info: {num_Self_emp + num_Salaried}")
print(f"Observations with no employment type data: {num_no_emp}")
print("Total observations: ", len(df))
# Calculating pct of total observations with no emp.type data
pct_emp_NaN = round((num_no_emp / len(df)) * 100, 2)
print(f"Percent of data with no employment type information: {pct_emp_NaN}% \n")

# In an actual business setting, I'd likely just delete the observations with no employment type data given their
# scarcity, but for the sake of the exercise, I'll replace the missing values with "Salaried" or "Self employed" based
# on the percentages of salaried and self employed by loan status
# Exploring employment types by default status
print("Exploring employment types by default status:")
# Dropping observations with no emp.type data to get a total of complete observations
df_no_NaN = df.dropna()
print("Number of observations with employment type data:", len(df_no_NaN))
# Splitting frame by loan status
df_current = df_no_NaN[df_no_NaN["loan_default"] == 0]
df_default = df_no_NaN[df_no_NaN["loan_default"] == 1]
# Showing numbers of current and in default loans in complete observations
print("Number of accounts current:", len(df_current))
print("Number of defaults: ", len(df_default))

# Calculating percentage of current loans held by salaried employees
pct_current_salaried = round((len(df_current[df_current["Employment.Type"] == 'Salaried']) / len(df_current)) * 100, 2)
# Calculating percentage of current loans held by self employed people
pct_current_self_emp = round((len(df_current[df_current["Employment.Type"] == 'Self employed']) /
                              len(df_current)) * 100, 2)
# Calculating percentage of in default loans held by salaried employees
pct_default_salaried = round((len(df_default[df_default["Employment.Type"] == 'Salaried']) / len(df_default)) * 100, 2)
# Calculating percentage of in default loans held by self employed people
pct_default_self_emp = round((len(df_default[df_default["Employment.Type"] == 'Self employed']) /
                              len(df_default)) * 100, 2)
# Showing calculated values
print(f"Percentage of current loan holders on salary: {pct_current_salaried}%")
print(f"Percentage of current loan holders self employed: {pct_current_self_emp}%")
print(f"Percentage of loan defaulters on salary: {pct_default_salaried}%")
print(f"Percentage of loan defaulters self employed: {pct_default_self_emp}% \n")

# Separating observations with missing employment type data (A dataframe with no missing values already exists:
# df_no_NaN)
df_no_emp = df[df["Employment.Type"].isna()]
print("Number of observations with no employment type information: ", len(df_no_emp))
# Separating observations with no employment data into current and default
df_no_emp_current = df_no_emp[df_no_emp["loan_default"] == 0]
df_no_emp_default = df_no_emp[df_no_emp["loan_default"] == 1]
print("Number of current loan holders with no employment type info: ", len(df_no_emp_current))
print("Number of loan holders in default with no employment type info: ", len(df_no_emp_default))
# Confirming all observations with missing emp.type data are accounted for
print("Total: ", len(df_no_emp_current) + len(df_no_emp_default), "\n")

# Using probability Boolean generator to simulate values for "Employment.Type" column
from pyprobs import Probability as pr

# Creating a list of Booleans for current loans
no_emp_current_replacements = pr.prob(0.4416, num=6017)
# Confirming successful creation
print(type(no_emp_current_replacements))
print(no_emp_current_replacements.count(True))
print(no_emp_current_replacements.count(False))

# Replacing NaN values with list values for current loans
df_no_emp_current["Employment.Type"] = df_no_emp_current.loc[pd.isnull(df_no_emp_current["Employment.Type"]), "Employment.Type"] = no_emp_current_replacements
# Confirming replacement
print("Replacing NaN values:")
print(df_no_emp_current["Employment.Type"].value_counts())

# Creating a list of Booleans for in-default loans
no_emp_default_replacements = pr.prob(0.4066, num=1644)
# Confirming successful creation
print(type(no_emp_default_replacements))
print(no_emp_default_replacements.count(True))
print(no_emp_default_replacements.count(False))

# Replacing NaN values with list values for in-default loans
df_no_emp_default["Employment.Type"] = df_no_emp_default.loc[pd.isnull(df_no_emp_default["Employment.Type"]), "Employment.Type"] = no_emp_default_replacements
# Confirming replacement
print("Replacing NaN values:")
print(df_no_emp_default["Employment.Type"].value_counts())

# Replacing Booleans with corresponding strings for current loans
df_no_emp_current["Employment.Type"] = df_no_emp_current["Employment.Type"].replace(True, "Salaried")
df_no_emp_current["Employment.Type"] = df_no_emp_current["Employment.Type"].replace(False, "Self employed")
# Confirming replacement
print("Replacement of Booleans with corresponding strings for current loans:")
print(df_no_emp_current["Employment.Type"].value_counts())


# Replacing Booleans with corresponding strings for in-default loans
df_no_emp_default["Employment.Type"] = df_no_emp_default["Employment.Type"].replace(True, "Salaried")
df_no_emp_default["Employment.Type"] = df_no_emp_default["Employment.Type"].replace(False, "Self employed")
# Confirming replacement
print("Replacement of Booleans with corresponding strings for in-default loans:")
print(df_no_emp_default["Employment.Type"].value_counts())

# Creating final data frame with no missing values
df_for_exp = pd.concat([df_no_NaN, df_no_emp_current, df_no_emp_default])
# Confirming creation
print("Confirming creation of final data frame:")
print(len(df))
print(len(df_for_exp))
print(df_for_exp.isna().any())
print(df_for_exp["Employment.Type"].value_counts())

# Writing final data frame to csv
try:
    df_for_exp.to_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\Capstone Project\\"
                      r"Datasets\Datasets\auto loan default data for exploration.csv")
except:
    FileExistsError
