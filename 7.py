import pandas as pd
import os
df = pd.read_csv("train.csv", encoding="latin1")  
print("Dataset Loaded")
print(df.shape)
print(df.head())
os.makedirs("data_warehouse", exist_ok=True)
os.makedirs("data_lake", exist_ok=True)
os.makedirs("data_lakehouse", exist_ok=True)
df.to_csv("data_warehouse/sales_warehouse.csv", index=False)
print("Saved to Data Warehouse (CSV)")
df.to_json("data_lake/sales_lake.json", orient="records", lines=True)
print("Saved to Data Lake (JSON)")
try:
    df.to_parquet("data_lakehouse/sales_lakehouse.parquet")
    print("Saved to Data Lakehouse (Parquet)")
except:
    print("Parquet not supported. Install pyarrow to enable it.")
print("Warehouse CSV size:", os.path.getsize("data_warehouse/sales_warehouse.csv"), "bytes")
print("Lake JSON size:", os.path.getsize("data_lake/sales_lake.json"), "bytes")

if os.path.exists("data_lakehouse/sales_lakehouse.parquet"):
    print("Lakehouse Parquet size:", os.path.getsize("data_lakehouse/sales_lakehouse.parquet"), "bytes")
print("Process Completed")
