import pandas as pd

data_2017 = pd.read_csv("D:/Python/ML/Market Basket Analysis/Dataset/Sales Transactions-2017.csv")
print(data_2017)
data_2018 = pd.read_csv("D:/Python/ML/Market Basket Analysis/Dataset/Sales Transactions-2018.csv")
print(data_2018)
data_2019 = pd.read_csv("D:/Python/ML/Market Basket Analysis/Dataset/Sales Transactions-2019.csv")
print(data_2019)


data = pd.concat([data_2017, data_2018, data_2019], ignore_index=True, sort=False)
print(data)

data = data.drop(columns=['Gross','Disc','Voucher Amount'],axis=1)
print(data)

data = data[data['Date'] != ' '].dropna(subset=['Date'])
print(data)

data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
print(data['Date'])

data['Voucher'] = data['Voucher'].str.slice(start=4, stop=None, step=1).astype(int)
print(data['Voucher'])

data['Party'] = data['Party'].str.upper()
data['Product'] = data['Product'].str.upper()

print(data['Party'])
print(data['Product'])

# Convert the Qty column into an integer 
#(Data has the entries with ',' and '.00') - Assuming Quantity can only be an integer
data['Qty'] = data['Qty'].str.replace(',','').astype(float).astype(int)
print(data['Qty'])

# Eliminate ',' in the Rate column
data['Rate'] = data['Rate'].str.replace(',','').astype(float)
print(data['Rate'])

# Sort the Sales Transaction file in the order of Date and Voucher
data = data.sort_values(['Date','Voucher'])
print(data)

# Understand the Data
print(data.shape)
print(data.describe())
print(data.info())

from pandas_profiling import ProfileReport
profile = ProfileReport(data, title= "Report", explorative=True)
profile.to_file("report.html")

# Top Selling Products
# Find the no of units sold of each product
# Find the unit price of each product (max of price considered, may required to be changed to median or mean)
top_selling_items = data.groupby('Product').agg({'Qty':'sum', 'Rate':'max'})
print(top_selling_items)

# Reset the index by converting the Product into a column
top_selling_items.reset_index(inplace=True)


# Rank the product by most Qty sold
top_selling_items['Top_Sell_Rank'] = top_selling_items['Qty'].rank(method='min',ascending=False).astype(int)


# List the top 20 items sold
top_selling_items.sort_values('Qty', ascending=False).head(20)

# Considered Date column instead of Voucher, in counting the no of orders placed for a product.
# This ignores the multiple no of orders created in a single day.
# Here the understanding is that, this being a wholesale business,
#      a customer places a 2nd order of the same product in a day, only when he/she notices a wrong qty placed on the order.
# If the business considers to have Voucher column, instead of Date column, all the Date column below needs to be replaced.


# Remove duplicate records at Product, Date and Party level
unique_items = data.drop_duplicates(['Product','Date','Party'])


# Find the no of orders placed and the unique no of customers placed orders, of each product
popular_items = unique_items.groupby('Product').agg({'Date':'count', 'Party':'nunique'})
popular_items.columns=['No_of_Orders','No_of_Customers']

# Reset the index by converting the Product into a column
popular_items.reset_index(inplace=True)
print(popular_items.head(10))

# Products with high no of orders can be considered as most frequently purchased items
# To find the most popular items, include the no of customers purchased and provide more weightage to products purchased by more customers

# Weighted No_of_Orders (W) = O * (C / M)

# No_of_Orders - O
Orders = popular_items['No_of_Orders']
# No_of_Customers purchased the product - C
Customers_Purchased = popular_items['No_of_Customers']
# Maximum no of customers made transactions in the entire period - M
Max_cust = popular_items['No_of_Customers'].max()

popular_items['Weighted_No_of_Orders'] = Orders * (Customers_Purchased / Max_cust)

# Finding Rank of the product by weighted no of orders
popular_items['Popularity_Rank'] = popular_items['Weighted_No_of_Orders'].rank(method='min',ascending=False).astype(int)


# List of top 20 most popular items sold
popular_items.sort_values('Popularity_Rank',ascending=True).head(20)

# Merge Top Selling Items Rank and Popularity Rank dataframes
product_rankings = pd.merge( top_selling_items, popular_items, how='inner', on='Product')
print(product_rankings)

# Get only the Product, Price and Rank columns
product_rankings = product_rankings[['Product','Rate','Top_Sell_Rank','Popularity_Rank']]


# List the Product Rankings
product_rankings.sort_values('Popularity_Rank',ascending=True).head(20)

product_rankings.to_csv('Product_Rankings.csv', index=False)

# Create a Pickle (.pkl) file with the Ranking dataframe
import pickle
pickle.dump(product_rankings, open('prod_ranking_model.pkl','wb'))




