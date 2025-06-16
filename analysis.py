import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('dataset.csv')

# Profit by City
city_profit = df.groupby('City')['Profit'].sum().sort_values(ascending=False)
print("Profit by City:\n", city_profit)

# Devices profit
device_profit = df.groupby('Product')['Profit'].sum()

# Bar chart: City vs Profit
plt.figure(figsize=(8, 5))
city_profit.plot(kind='bar', color='skyblue')
plt.title('Total Profit by City')
plt.ylabel('Profit')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('city_vs_profit.png')  # Saves chart to file
plt.close()

# Histogram: Least Sold Devices vs City
quantity = df.groupby(['Product', 'City'])['Quantity'].sum().reset_index()
least_sold = quantity[quantity['Quantity'] <= 2]

plt.figure(figsize=(10, 5))
for product in least_sold['Product'].unique():
    subset = least_sold[least_sold['Product'] == product]
    plt.bar(subset['City'], subset['Quantity'], label=product)
plt.title('Least Sold Devices by City')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('least_sold_devices.png')  # Saves chart to file
plt.close()
