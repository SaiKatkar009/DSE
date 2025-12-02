import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
df = pd.read_csv("Iris.csv")
print("First 5 rows of dataset:\n", df.head())
print("\nShape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
data = df[['SepalLengthCm', 'SepalWidthCm', 'Species']]
print("\nAfter Feature Selection:\n", data.head())
data = data.copy()
data['sepal_ratio'] = data['SepalLengthCm'] / data['SepalWidthCm']
print("\nAfter Feature Extraction:\n", data.head())
encoder = LabelEncoder()
data['Species'] = encoder.fit_transform(data['Species'])
print("\nAfter Encoding:\n", data.head())
scaler = StandardScaler()
data[['SepalLengthCm', 'SepalWidthCm', 'sepal_ratio']] = scaler.fit_transform(
    data[['SepalLengthCm', 'SepalWidthCm', 'sepal_ratio']]
)
print("\nFinal Processed Data:\n", data.head())
