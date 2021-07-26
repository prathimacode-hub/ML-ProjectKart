import pandas as pd

data = pd.read_csv('D:/Python/ML/Market Basket Analysis/data.csv')
print(data)

#Build Correlation Matrix for the Customer-Product relations (using User-User based recommendation)

# Find the total qty purchased by each customer of each product
prod_cust_qty = data.groupby(['Product','Party']).agg({'Qty':'sum'})

# Reset the index by converting the Party and Product into columns
prod_cust_qty.reset_index(inplace=True)


# Find the no of unique customers purchased each product
prod_cust_count = data.groupby(['Product']).agg({'Party':'nunique'})

# Set the customer count column
prod_cust_count.columns=['No_of_Customers']

# Reset the index by converting the Party and Product into columns
prod_cust_count.reset_index(inplace=True)


# Merge the unique customer count and qty purchased of each product
product_customer = pd.merge(prod_cust_qty , prod_cust_count,how='inner',on='Product')


# Create a pivot table with all Customers on columns and Products on rows, and Qty as values
prod_cust_pivot = product_customer.pivot(index='Product',columns='Party',values='Qty').fillna(0)

# Find the correlation between every two customers and build a correlation matrix using corr() method
# Used Spearman method in identifying the correlation. Pearson was not providing better results and Kendall is taking a long time for execution.
cust_correlation = prod_cust_pivot.corr(method='spearman',min_periods=5)

print(cust_correlation.head(10))

#Write the Customer to Customer Correlation Matrix to a .csv file
cust_correlation.to_csv('Customer-Customer-Correlation-Matrix.csv')

import pickle
#Create a Pickle (.pkl) file with the Correlation Matrix dataframe
pickle.dump(cust_correlation, open('cust_correlation_model.pkl','wb'))





##Build Correlation Matrix for the Product-Customer relations (using Item-Item based recommendation)

# Find the total qty purchased by each customer of each product
prod_cust_qty = data.groupby(['Product','Party']).agg({'Qty':'sum'})

# Reset the index by converting the Party and Product into columns
prod_cust_qty.reset_index(inplace=True)


# Find the no of unique customers purchased each product
prod_cust_count = data.groupby(['Product']).agg({'Party':'nunique'})

# Set the customer count column
prod_cust_count.columns=['No_of_Customers']

# Reset the index by converting the Party and Product into columns
prod_cust_count.reset_index(inplace=True)


# Merge the unique customer count and qty purchased of each product
prod_cust = pd.merge(prod_cust_qty , prod_cust_count,how='inner',on='Product')


# Create a pivot table with all Products on columns and Customers on rows, and Qty as values
prod_cust_pivot = prod_cust.pivot(index='Party',columns='Product',values='Qty').fillna(0)

# Find the correlation between every two products and build a correlation matrix using corr() method
# Used Spearman method in identifying the correlation. Pearson was not providing better results and Kendall is taking a long time for execution.
prod_correlation = prod_cust_pivot.corr(method='spearman',min_periods=5)
print(prod_correlation.head(10))

# To Csv file
prod_correlation.to_csv('Product-Product-Correlation-Matrix.csv')

#To Pickle File
pickle.dump(prod_correlation, open('prod_correlation_model.pkl','wb'))









