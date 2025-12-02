import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("USA_Housing.csv")
df = df.rename(columns={
    'Avg. Area Income': 'Income',
    'Avg. Area House Age': 'HouseAge',
    'Avg. Area Number of Rooms': 'Rooms',
    'Avg. Area Number of Bedrooms': 'Bedrooms',
    'Area Population': 'Population',
    'Price': 'Price',
    'Address': 'Address'
})
print("Columns:", df.columns, "\n")
print(df.head(), "\n")
print(df.info(), "\n")
print(df.describe(), "\n")
plt.figure(figsize=(6, 4))
plt.hist(df['Price'], bins=20, edgecolor='black')
plt.title('Price Distribution')
plt.show()
plt.figure(figsize=(6, 4))
plt.scatter(df['HouseAge'], df['Price'], alpha=0.5)
plt.xlabel("House Age")
plt.ylabel("Price")
plt.title("House Age vs Price")
plt.show()
sns.pairplot(df[['Income', 'Population', 'Price']])
plt.show()
plt.figure(figsize=(7, 5))
sns.heatmap(
    df[['Income', 'HouseAge', 'Rooms', 'Bedrooms', 'Population', 'Price']].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title('Correlation Heatmap')
plt.show()
plt.figure(figsize=(7, 5))
sns.boxplot(data=df[['Income', 'HouseAge', 'Rooms', 'Bedrooms', 'Population', 'Price']])
plt.title("Boxplot of Numerical Features")
plt.xticks(rotation=45)
plt.show()
