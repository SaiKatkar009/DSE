import pandas as pd
import sqlite3
df = pd.read_csv("ecommerce (2).csv", encoding='latin1')
print("Raw Data Loaded Successfully!")
print("Shape:", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nMissing Values:\n", df.isnull().sum())
rows_before = df.shape[0]
df = df.dropna(subset=['CustomerID'])
print(f"\nAfter dropping missing CustomerID: {df.shape[0]} rows (removed {rows_before - df.shape[0]})")
rows_before = df.shape[0]
df = df[df['Quantity'] > 0]
print(f"After removing Quantity <= 0: {df.shape[0]} rows (removed {rows_before - df.shape[0]})")
rows_before = df.shape[0]
df = df[df['UnitPrice'] > 0]
print(f"After removing UnitPrice <= 0: {df.shape[0]} rows (removed {rows_before - df.shape[0]})")
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
df['Description'] = df['Description'].astype(str).str.strip()
print("\nData Information After Cleaning:")
print(df.info())
print("\nSample of Cleaned Data:\n", df.head())
print("\n=== LOADING INTO SQLITE DATABASE ===")
conn = sqlite3.connect("ecommerce.db")
df.to_sql("ecommerce_table", conn, if_exists="replace", index=False)
preview_query = """
SELECT InvoiceNo, Description, Quantity, UnitPrice, TotalPrice, CustomerID
FROM ecommerce_table
LIMIT 5;
"""
preview = pd.read_sql_query(preview_query, conn)
print("\nPreview of Data in SQLite Database:\n")
print(preview)
count = pd.read_sql_query("SELECT COUNT(*) AS total FROM ecommerce_table;", conn)
print("\nTotal Records Loaded:", count['total'][0])
conn.close()
cleaned_filename = "ecommerce_cleaned.csv"
df.to_csv(cleaned_filename, index=False)

print(f"\n=== CLEANED CSV SAVED SUCCESSFULLY AS: {cleaned_filename} ===")
