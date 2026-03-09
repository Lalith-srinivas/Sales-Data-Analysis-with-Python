# ===============================
# SALES DATA ANALYSIS PROJECT
# ===============================

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1. Load Dataset
# -------------------------------

print("Loading dataset...")

df = pd.read_csv("superstore.csv", encoding='latin1')

print("\nFirst 5 Rows")
print(df.head())

# -------------------------------
# 2. Dataset Overview
# -------------------------------

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nDataset Info")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

# -------------------------------
# 3. Check Missing Values
# -------------------------------

print("\nMissing Values")
print(df.isnull().sum())

# -------------------------------
# 4. Remove Duplicates
# -------------------------------

df = df.drop_duplicates()

print("\nShape After Removing Duplicates")
print(df.shape)

# -------------------------------
# 5. Convert Date Columns
# -------------------------------

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# -------------------------------
# 6. Create New Columns
# -------------------------------

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.month_name()

# -------------------------------
# 7. Total Sales & Profit
# -------------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("\nTotal Sales:", total_sales)
print("Total Profit:", total_profit)

# -------------------------------
# 8. Sales by Category
# -------------------------------

sales_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print("\nSales by Category")
print(sales_category)

# -------------------------------
# 9. Sales by Region
# -------------------------------

sales_region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

print("\nSales by Region")
print(sales_region)

# -------------------------------
# 10. Top 10 Products
# -------------------------------

top_products = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Products by Sales")
print(top_products)

# -------------------------------
# 11. Top 10 Customers
# -------------------------------

top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Customers")
print(top_customers)

# -------------------------------
# 12. Monthly Sales Trend
# -------------------------------

monthly_sales = df.groupby("Month Name")["Sales"].sum()

print("\nMonthly Sales")
print(monthly_sales)

# -------------------------------
# 13. Visualization
# -------------------------------

# Sales by Category
plt.figure(figsize=(8,5))
sns.barplot(x=sales_category.index, y=sales_category.values)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.savefig("Sales_By_Category.png")
plt.show()

# Sales by Region
plt.figure(figsize=(8,5))
sns.barplot(x=sales_region.index, y=sales_region.values)
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.savefig("Sales_By_Region.png")
plt.show()

# Monthly Sales Trend
plt.figure(figsize=(10,5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("Monthly_Sales_Trend.png")
plt.show()

# Profit by Category
profit_category = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
profit_category.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.savefig("Profit_By_Category.png")
plt.show()

# -------------------------------
# 14. Save Clean Dataset
# -------------------------------

df.to_csv("cleaned_superstore.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("\nSales Data Analysis Project Completed!")