
import pandas as pd

# Load the sales dataset
df = pd.read_csv("sales_data.csv")

# Display basic information
print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn information:")
print(df.info())

# Calculate revenue for each order
df["Revenue"] = df["Quantity"] * df["Unit_Price"]

print("\nTotal Sales Revenue:")
print(df["Revenue"].sum())

print("\nRevenue by Product:")
print(
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)


# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Extract month
df["Month"] = df["Date"].dt.to_period("M")

# Calculate monthly revenue
monthly_sales = df.groupby("Month")["Revenue"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Find top-selling products by quantity
top_products = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop Products by Quantity Sold:")
print(top_products)


import matplotlib.pyplot as plt

# Monthly revenue chart
monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(9, 5))
monthly_sales.plot(kind="bar")
plt.title("Monthly Sales Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

# Top products chart
plt.figure(figsize=(9, 5))
top_products.plot(kind="bar")
plt.title("Products by Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_products.png")
plt.show()



# Export analysis results to Excel
with pd.ExcelWriter("sales_analysis_report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Order_Data", index=False)

    monthly_sales.to_frame("Revenue").to_excel(
        writer, sheet_name="Monthly_Sales"
    )

    top_products.to_frame("Quantity_Sold").to_excel(
        writer, sheet_name="Top_Products"
    )

print("\nExcel report saved successfully!")
