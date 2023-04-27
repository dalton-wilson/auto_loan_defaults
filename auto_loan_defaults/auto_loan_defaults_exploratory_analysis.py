import pandas as pd
import numpy as np
import datetime


df = pd.read_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\Capstone Project\\"
                 r"Loan Defaults\Datasets\Datasets\auto loan default data for exploration.csv")

df.info()
print()

# Task 4: Provide the statistical description of the quantitative data variables
# "AVERAGE.ACCT.AGE" and "CREDIT.HISTORY.LENGTH" would appear to be relevant measurables, but are currently in
# "Xyrs Ymos" string format. Converting to Int64 data type as numbers of months
print(df["AVERAGE.ACCT.AGE"].value_counts(), "\n")
print(df["CREDIT.HISTORY.LENGTH"].value_counts(), "\n")

# Splitting strings into years and months
new_acct_age = df["AVERAGE.ACCT.AGE"].str.split(" ", n=1, expand=True)
df["acct.age.yrs"] = new_acct_age[0]
df["acct.age.mos"] = new_acct_age[1]

new_cred_hist_len = df["CREDIT.HISTORY.LENGTH"].str.split(" ", n=1, expand=True)
df["cred.hist.yrs"] = new_cred_hist_len[0]
df["cred.hist.mos"] = new_cred_hist_len[1]

# Removing letters from strings:
df["acct.age.yrs"] = df["acct.age.yrs"].str.replace("yrs", "")
df["acct.age.mos"] = df["acct.age.mos"].str.replace("mon", "")
df["cred.hist.yrs"] = df["cred.hist.yrs"].str.replace("yrs", "")
df["cred.hist.mos"] = df["cred.hist.mos"].str.replace("mon", "")

print(df["acct.age.yrs"].value_counts())
print(df["acct.age.mos"].value_counts())
print(df["cred.hist.yrs"].value_counts())
print(df["cred.hist.mos"].value_counts())

# Changing data types of new columns:
df["acct.age.yrs"] = df["acct.age.yrs"].astype("int64")
df["acct.age.mos"] = df["acct.age.mos"].astype("int64")
df["cred.hist.yrs"] = df["cred.hist.yrs"].astype("int64")
df["cred.hist.mos"] = df["cred.hist.mos"].astype("int64")

# Converting years to months
df["acct.age.yrs.conv"] = df["acct.age.yrs"] * 12
df["cred.hist.yrs.conv"] = df["cred.hist.yrs"] * 12

# Renaming original columns
df.rename(columns={"AVERAGE.ACCT.AGE": "AVG.ACCT.AGE(MOS)", "CREDIT.HISTORY.LENGTH": "CRED.HIST.LEN(MOS)"},
          inplace=True)

# Replacing values in original columns
df["AVG.ACCT.AGE(MOS)"] = df["acct.age.yrs.conv"] + df["acct.age.mos"]
df["CRED.HIST.LEN(MOS)"] = df["cred.hist.yrs.conv"] + df["cred.hist.mos"]

# Removing extra columns created during conversion
df.drop(columns=["acct.age.yrs", "acct.age.mos", "cred.hist.yrs", "cred.hist.mos", "acct.age.yrs.conv",
                 "cred.hist.yrs.conv"], inplace=True)

# Confirming changes
df.info()
print(df["AVG.ACCT.AGE(MOS)"].value_counts())
print(df["CRED.HIST.LEN(MOS)"].value_counts())

# Descriptive statistics
# Changing data types of non-quantitative variables
df["UniqueID"] = df["UniqueID"].astype(str)
df["branch_id"] = df["branch_id"].astype(str)
df["supplier_id"] = df["supplier_id"].astype(str)
df["manufacturer_id"] = df["manufacturer_id"].astype(str)
df["Current_pincode_ID"] = df["Current_pincode_ID"].astype(str)
df["State_ID"] = df["State_ID"].astype(str)
df["Employee_code_ID"] = df["Employee_code_ID"].astype(str)

# Adding Age information
df["Date.of.Birth"] = pd.to_datetime(df["Date.of.Birth"])
today = datetime.datetime.today()

ages = []
for dob in df["Date.of.Birth"]:
    ages.append(today - dob)

df["Loan.holder.age(yrs)"] = ages
df["Loan.holder.age(yrs)"] = df["Loan.holder.age(yrs)"].astype(str)

split_age_data = df["Loan.holder.age(yrs)"].str.split(" ", n=1, expand=True)
df["Loan.holder.age(yrs)"] = split_age_data[0]
df["Loan.holder.age(yrs)"] = df["Loan.holder.age(yrs)"].astype("int64")
df["Loan.holder.age(yrs)"] = round(df["Loan.holder.age(yrs)"]/365, 1)

col_to_move = df.pop("Loan.holder.age(yrs)")
df.insert(10, "Loan.holder.age(yrs)", col_to_move)

df["defaultYes/No"] = df["loan_default"]
df["defaultYes/No"] = df["defaultYes/No"].replace(0, "No")
df["defaultYes/No"] = df["defaultYes/No"].replace(1, "Yes")




# Writing to csv for import into Tableau
try:
    df.to_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\Capstone Project\\"
              r"Datasets\Datasets\auto_loan_default_final.csv", mode='x')
except:
    FileExistsError

# Showing descriptive statistics
desc_stats = df.describe(percentiles=None, include=np.number)
#print(desc_stats)

# Creating a data frame to write to Excel
stats_frame = pd.DataFrame(desc_stats)

try:
    stats_frame.to_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\Capstone Project\\"
                       r"Datasets\Datasets\desc_stats.csv", mode='x')
except:
    FileExistsError
