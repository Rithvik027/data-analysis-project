import pandas as pd
import matplotlib.pyplot as plt
import os

# Create folders if not present
os.makedirs("visualizations", exist_ok=True)
os.makedirs("report", exist_ok=True)

# Load CSV file
try:
    df = pd.read_csv("data/sales_data.csv")
    print("File loaded successfully")
except:
    print("Error: Cannot find sales_data.csv")
    exit()

# Clean data
df.dropna(inplace=True)

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

# Top products analysis
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(5)

# Sales trend chart
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    trend = df.groupby("Date")["Revenue"].sum()

    plt.figure()
    plt.plot(trend.index, trend.values)
    plt.title("Sales Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("visualizations/sales_trend.png")
    plt.close()

# Top products bar chart
plt.figure()
top_products.plot(kind="bar")
plt.title("Top 5 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("visualizations/top_products.png")
plt.close()

# Save report
with open("report/sales_analysis_report.txt", "w") as f:
    f.write("SALES PERFORMANCE ANALYSIS\n")
    f.write("Top products generate most revenue\n")
    f.write("Sales change over time\n")
    f.write("Focus on high-performing products\n")

print("Project completed")
