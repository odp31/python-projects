import pandas as pd
import matplotlib.pyplot as plt 

# Load dataset
df = pd.read_csv('used_cars_data.csv')

# Explore data 
print(df.head())
print(df.info())
print(df.describe())

# Data Cleaning (if necessary); handle missing values, convert data types, remove outliers 
# Exploratory Data Analysis (EDA)
# Visualize distribution of prices
plt.hist(df['Price'], bins = 30)
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Distribution of Car Prices')
plt.show()

# Analyze relatioinship between mileage and price 
plt.scatter(df['Mileage'], df['Price'])
plt.xlabel('Mileage')
plt.ylabel('Price')
plt.title('Mileage vs. Price')
plt.show()

# Explore distribution of car ages 
df['Age'] = 2023 - df['Year']
plt.hist(df['Age'], bins=15)
plt.xlabel('Age (Years)')
plt.ylabel('Frequency')
plt.title('Distribution of Car Ages')
plt.show()

# Analyze impact of fuel type on price 
plt.boxplot([df[df['Fuel_Type'] == 'Petrol']['Price'],
             df[df['Fuel_Type'] == 'Diesel']['Price'],
             df[df['Fuel_Type] == 'CNG']['Price']])
plt.xticks([1, 2, 3], ['Petrol', 'Diesel', 'CNG'])
plt.ylabel('Price')
plt.title('Price Distribution by Fuel Type')
plt.show()

             




