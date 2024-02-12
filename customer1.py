import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


dataset = 'dataset_1.csv'

df = pd.read_csv(dataset)

print(df.info())


#Removing empty data

new_df = df.dropna()
# print(new_df.to_string())


# Sort DataFrame by Total Spend in descending order
df = new_df.sort_values(by="Total Spend",ascending=False)

# Total Spend for each customer
plt.figure(figsize=(10,6))
plt.bar(df["Customer ID"],df["Total Spend"],color = "skyblue")
plt.xlabel("Customer ID")
plt.ylabel("Total Spend")
plt.title('Total Spend by Customer')
plt.xticks(df['Customer ID'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#relationship between Age and Total Spend
plt.figure(figsize=(8, 6))
plt.scatter(df['Age'], df['Total Spend'], color='skyblue')
plt.xlabel('Age')
plt.ylabel('Total Spend ($)')
plt.title('Relationship between Age and Total Spend')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

#total spend for each combination of gender and city
grouped = df.groupby(['Gender', 'City'])['Total Spend'].sum().reset_index()

plt.figure(figsize=(10, 6))
x = range(len(grouped))
plt.bar(x, grouped['Total Spend'], color='skyblue')
plt.xlabel('Gender-City Combination')
plt.ylabel('Total Spend ($)')
plt.title('Total Spend by Gender and City')
plt.xticks(x, [f"{gender}-{city}" for gender, city in zip(grouped['Gender'], grouped['City'])], rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


#relationship between Discount , City , Membership and Total Spend
grouped = df.groupby(['Discount Applied', 'City', 'Membership Type'])['Total Spend'].sum().reset_index()

fig, ax = plt.subplots(figsize=(12, 8))

for idx, group in grouped.groupby(['Discount Applied', 'City']):
    city, membership_type = idx[1], group['Membership Type'].unique()[0]
    ax.bar(f'{city} - {membership_type}', group['Total Spend'], label=f"Discount Applied: {idx[0]}", alpha=0.7)

ax.set_xlabel('City - Membership Type')
ax.set_ylabel('Total Spend ($)')
ax.set_title('Total Spend by Discount Applied, City, and Membership Type')

ax.legend()

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()