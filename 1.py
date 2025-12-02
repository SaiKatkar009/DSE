import pandas as pd
import requests
import json
from sklearn.datasets import load_iris


print("structured data example (csv file):")


structured_data = pd.read_csv('Iris.csv')

print("Data successfully loaded from CSV file")
print("structured_data")
print(structured_data.head())


print("semi-structured data example (Restaurant Inspection XLSX):")

df_inspect = pd.read_excel("Restaurant_Inspection.xlsx", engine='openpyxl')

print("\nRestaurant Inspection Data (Preview)")
print(df_inspect.head(), "\n")

print("Dataset Shape:", df_inspect.shape)
print("Columns:", df_inspect.columns.tolist(), "\n")


print("semi-structured data example (NYC Restaurant CSV):")


df_rest = pd.read_csv("Restaurant_Inspection.csv", encoding='latin1',on_bad_lines='skip',engine='python')

print("\nNYC Restaurant Data (Preview)")
print(df_rest.head(), "\n")

print("Dataset Shape:", df_rest.shape)
print("Columns:", df_rest.columns.tolist())


print("\nsemi-structured data example (API):")

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)


data_api = response.json()
df_api = pd.DataFrame(data_api)

print("\nAPI Data (Posts)")
print(df_api.head(), "\n")

# Basic Info
print("Dataset Shape:", df_api.shape)
print("Columns:", df_api.columns.tolist())  


print("\nunstructured data example (CSV file):")


with open("spam.csv", "r", encoding="latin1") as file:
    text_data = file.readlines()

print("CSV file loaded successfully!")
print("\nunstructured_data (raw text content):")

for line in text_data[:10]:   
    print(line.strip())


print("\nunstructured data example (Text file):")

with open("sample_text.txt", "w") as file:
    file.write("data science is amazing!\n")
    file.write("It includes structured, semi-structured and unstructured data\n")
    file.write("python helps in processing all types effectively\n")


with open("sample_text.txt", "r") as file:
    text_data = file.readlines()

print("Text file loaded successfully!")
print("\nunstructured_data (raw text content):")

for line in text_data:
    print(line.strip())
