import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['figure.figsize'] = (20,12)
plt.rcParams["figure.autolayout"] = True

# Load dataset
df = pd.read_csv('zomato.csv', encoding='latin-1')

print(df.shape)
print(df.head())

print(df.columns)
print(df.info())
print(df.describe())

# Check missing values
print(df.isnull().sum())

# Visualize missing values
plt.bar(df.columns, df.isnull().sum())
plt.xticks(rotation=45)
plt.title("Missing Values Count")
plt.show()

# Load country code dataset
df_country = pd.read_excel('Country-Code.xlsx')

# Merge datasets
final_df = pd.merge(df, df_country, on="Country Code", how="left")

print(final_df.head())

# Correlation analysis
final_df_numeric = final_df.select_dtypes(exclude='object')

print(final_df_numeric.corr())

# Country distribution
country_names = final_df.Country.value_counts().index
country_values = final_df.Country.value_counts().values

plt.pie(country_values[:3], labels=country_names[:3], autopct='%.2f%%')
plt.title("Top 3 Countries Distribution")
plt.show()

# Ratings analysis
ratings = final_df.groupby(
    ['Aggregate rating','Rating color','Rating text']
).size().reset_index().rename(columns={0:'Rating count'})

print(ratings.head())

plt.bar(
    ratings['Aggregate rating'],
    ratings['Rating count'],
    width=0.07
)

plt.title("Ratings Distribution")
plt.show()

# Online delivery availability
online_delivery = final_df.groupby(
    ['Country','Has Online delivery']
).size().reset_index()

print(online_delivery)

# Top cuisines
cuisines_count = final_df.groupby(
    ['Cuisines']
).size().reset_index().rename(columns={0:'Count'})

cuisines_count = cuisines_count.sort_values(
    by='Count',
    ascending=False
)

plt.bar(
    cuisines_count['Cuisines'][:10],
    cuisines_count['Count'][:10]
)

plt.xticks(rotation=45)
plt.title("Top 10 Cuisines")
plt.show()

# Cost distribution in India
india_df = final_df[final_df['Country'] == 'India']

plt.hist(india_df['Average Cost for two'], bins=10)

plt.title("Cost Distribution for Two People in India")
plt.show()