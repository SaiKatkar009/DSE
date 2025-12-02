import pandas as pd
import numpy as np
df = pd.read_csv("loan.csv.csv")
print(df.head())
print(df.isnull().sum())
df['Gender'] = df['Gender'].fillna("Not Available")
df['Married'] = df['Married'].fillna("Unknown")
df['Dependents'] = df['Dependents'].fillna("Not Mentioned")
df['Education'] = df['Education'].fillna("Not Available")
df['Self_Employed'] = df['Self_Employed'].fillna("Not Available")
df['Property_Area'] = df['Property_Area'].fillna("Not Specified")
df['Loan_Status'] = df['Loan_Status'].fillna("Not Known")
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].mean())
df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].median())
df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mode()[0])
df['ApplicantIncome'] = df['ApplicantIncome'].fillna(df['ApplicantIncome'].mean())
df['CoapplicantIncome'] = df['CoapplicantIncome'].fillna(df['CoapplicantIncome'].mean())
print("\n=== AFTER FILLING MISSING VALUES ===")
print(df.isnull().sum())
df = df.rename(columns={
    'ApplicantIncome': 'Income',
    'CoapplicantIncome': 'CoIncome'
})
print("\n=== AFTER RENAMING COLUMNS ===")
print(df.head())
df['LoanAmount'] = df['LoanAmount'].astype(int)
df['Loan_Amount_Term'] = df['Loan_Amount_Term'].astype(int)
df['Credit_History'] = df['Credit_History'].astype(int)
print("\n=== DATA TYPES AFTER CONVERSION ===")
print(df.dtypes)
print("\n=== FINAL CLEANED DATA ===")
print(df.head())
print("\nShape:", df.shape)
loan_extra = pd.DataFrame({
    'Loan_ID': df['Loan_ID'].head(10),             
    'Officer': ['Amit', 'Sara', 'John', 'Priya', 'David',
                'Karan', 'Meena', 'Ali', 'Riya', 'Tom'],
    'Branch': ['Mumbai', 'Delhi', 'Chennai', 'Kolkata', 'Pune',
               'Bangalore', 'Hyderabad', 'Jaipur', 'Goa', 'Surat']
})
print("\n=== EXTRA DATAFRAME TO MERGE ===")
print(loan_extra)
merged_df = pd.merge(df, loan_extra, on="Loan_ID", how="left")
print("\n=== MERGED DATAFRAME ===")
print(merged_df.head(15))
print("\nMerged Shape:", merged_df.shape)
