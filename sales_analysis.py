# Import pandas library
import pandas as pd

# Load the dataset
df = pd.read_csv('sales_data.csv')

# ------------------ BASIC DATA EXPLORATION ------------------

# Print number of rows and columns (rows, columns)
print("Dataset Shape:", df.shape)

# Print column names
print("\nColumns in Dataset:")
print(df.columns)

# Print data types of each column
print("\nData Types:")
print(df.dtypes)

# ------------------ DATA CLEANING ------------------

# Count missing values in each column
print("\nMissing Values:")
print(df.isnull().sum())

# Count duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# ------------------ DATA ANALYSIS ------------------

# Create a new column 'Revenue' = Quantity × Price
df['Revenue'] = df['Quantity'] * df['Price']

# Calculate total revenue
total_revenue = df['Revenue'].sum()

# Find best-selling product (based on total quantity sold)
best_product = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)

# Get top product name and quantity
top_product_name = best_product.index[0]
top_product_quantity = best_product.iloc[0]

# ------------------ FINAL REPORT ------------------

print("\n" + "="*40)
print("         SALES REPORT SUMMARY")
print("="*40)

# Total Revenue
print(f"\n💰 Total Revenue: Rs {total_revenue:,.2f}")

# Best Selling Product
print(f"\n🏆 Best Selling Product: {top_product_name}")
print(f"📦 Quantity Sold: {top_product_quantity}")

# Top 5 Products
print("\n🔥 Top 5 Products by Sales:")
print(best_product.head())

# Average Revenue per Sale
avg_revenue = df['Revenue'].mean()
print(f"\n📊 Average Revenue per Sale: Rs {avg_revenue:,.2f}")

# Total Orders
total_orders = len(df)
print(f"\n🧾 Total Orders: {total_orders}")

print("\n" + "="*40)

# ------------------ INSIGHTS ------------------

print("\n📌 INSIGHTS:")

# Insight 1: High performing product
print(f"- '{top_product_name}' is the top-performing product with highest sales.")

# Insight 2: Revenue observation
print("- Total revenue shows overall business performance.")

# Insight 3: Average sale
print("- Average revenue helps understand per-order value.")

# Insight 4: Business suggestion
print("- Focus more on best-selling products to increase profit.")

print("\nReport Generated Successfully ✅")