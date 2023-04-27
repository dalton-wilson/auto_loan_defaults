import pandas as pd

df = pd.read_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\Capstone Project\\"
                 r"Loan Defaults\Datasets\Datasets\auto_loan_default_final_wkbk csv.csv")

df.info()
print()

# CREATING A DATA FRAME OF ALL RECORDS WITH VIABLE CREDIT SCORES TO USE IN CREDIT SCORE DISTRIBUTION
cb_scores = df[df["PERFORM_CNS.SCORE"] > 18]

cb_scores.info()

cb_scores.to_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\Capstone Project\\"
                 r"Loan Defaults\Datasets\Datasets\cb_scores csv.csv")

# CREATING A FRAME OF ALL PRIMARY AND SECONDARY ACCOUNT DETAILS FOR LOGISTIC REGRESSION
df_disbursals_tree = df[["PRI.NO.OF.ACCTS", "PRI.ACTIVE.ACCTS", "PRI.OVERDUE.ACCTS", "PRI.CURRENT.BALANCE",
                         "PRI.DISBURSED.AMOUNT", "PRIMARY.INSTAL.AMT", "SEC.NO.OF.ACCTS",
                         "SEC.ACTIVE.ACCTS", "SEC.OVERDUE.ACCTS", "SEC.CURRENT.BALANCE",
                         "SEC.DISBURSED.AMOUNT", "SEC.INSTAL.AMT", "loan_default"]]

df_disbursals_tree.info()
df_disbursals_tree.head()

# Getting rid of any rows in the data set with no disbursal information (all 0's)

df_disbursals_tree["SUM.DISB.INFO"] = (df_disbursals_tree["PRI.NO.OF.ACCTS"] +
                                       df_disbursals_tree["PRI.ACTIVE.ACCTS"] +
                                       df_disbursals_tree["PRI.OVERDUE.ACCTS"] +
                                       df_disbursals_tree["PRI.CURRENT.BALANCE"] +
                                       df_disbursals_tree["PRI.DISBURSED.AMOUNT"] +
                                       df_disbursals_tree["PRIMARY.INSTAL.AMT"] +
                                       df_disbursals_tree["SEC.NO.OF.ACCTS"] +
                                       df_disbursals_tree["SEC.ACTIVE.ACCTS"] +
                                       df_disbursals_tree["SEC.OVERDUE.ACCTS"] +
                                       df_disbursals_tree["SEC.CURRENT.BALANCE"] +
                                       df_disbursals_tree["SEC.DISBURSED.AMOUNT"] +
                                       df_disbursals_tree["SEC.INSTAL.AMT"])

df_disbursals_tree.info()
df_disbursals_tree.head()

df_disbursals_tree.to_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\\"
                          r"Capstone Project\Loan Defaults\Datasets\Datasets\df_disbursals_tree_csv.csv")

dt_disb = pd.read_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\\"
                      r"Capstone Project\Loan Defaults\Datasets\Datasets\df_disbursals_tree_csv.csv")

dt_disb.tail()
dt_frame = dt_disb[dt_disb["SUM.DISB.INFO"] != 0]
dt_frame.info()
dt_frame.drop(["Unnamed: 0", "SUM.DISB.INFO"], axis=1, inplace=True)
dt_frame.info()

dt_frame.to_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\\"
                r"Capstone Project\Loan Defaults\Datasets\Datasets\disbursals_dt_frame_csv.csv")

# CREATING DATA FRAME TO ANALYZE CREDIT ENQUIRIES
inquiries = df[["NO.OF_INQUIRIES", "loan_default"]]
inquiries.info()
inquiries.to_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\\"
                 r"Capstone Project\Loan Defaults\Datasets\Datasets\inquiries_csv.csv")

# CREATING A DATA FRAME OF CREDIT HISTORY INFORMATION FOR LOGISTIC REGRESSION
cred_hist = df[["NEW.ACCTS.IN.LAST.SIX.MONTHS", "DELINQUENT.ACCTS.IN.LAST.SIX.MONTHS", "AVG.ACCT.AGE(MOS)",
                "CRED.HIST.LEN(MOS)", "NO.OF_INQUIRIES", "loan_default"]]
cred_hist.info()

# Getting rid of all rows with no credit history info
cred_hist["SUM"] = (cred_hist["NEW.ACCTS.IN.LAST.SIX.MONTHS"] +
                    cred_hist["DELINQUENT.ACCTS.IN.LAST.SIX.MONTHS"] +
                    cred_hist["AVG.ACCT.AGE(MOS)"] +
                    cred_hist["CRED.HIST.LEN(MOS)"] +
                    cred_hist["NO.OF_INQUIRIES"])
cred_hist = cred_hist[cred_hist["SUM"] > 0]
cred_hist.info()
cred_hist.drop(["SUM"], axis=1, inplace=True)
cred_hist.info()

# Writing to csv
cred_hist.to_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\\"
                 r"Capstone Project\Loan Defaults\Datasets\Datasets\cred_hist_csv.csv")

# CREATING A FRAME OF NUMERIC DATA ONLY FOR OVERALL REGRESSION
numeric_data = df._get_numeric_data()
numeric_data.info()
numeric_data.drop(["Column1", "Unnamed: 0", "UniqueID"], axis=1, inplace=True)
numeric_data.info()

# Writing to csv
numeric_data.to_csv(r"C:\Users\dalto\OneDrive\Desktop\Data Analysis Training\Simplilearn_DA_PGP\\"
                    r"Capstone Project\Loan Defaults\Datasets\Datasets\numeric_data_csv.csv")

