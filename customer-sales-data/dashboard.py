import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os


os.makedirs("visualizations", exist_ok=True)


df = pd.read_csv("sales_data (3).csv")

df['Date'] = pd.to_datetime(df['Date'])

sns.set_style("whitegrid")
sns.set_palette("deep")


plt.figure(figsize=(10,5))
monthly_sales = df.groupby(df['Date'].dt.to_period("M"))['Sales'].sum()
monthly_sales.index = monthly_sales.index.to_timestamp()

sns.lineplot(x=monthly_sales.index, y=monthly_sales.values)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/sales_trend.png")
plt.close()


plt.figure(figsize=(8,5))
sns.barplot(x='Category', y='Sales', data=df, estimator=sum)
plt.title("Total Revenue by Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/category_distribution.png")
plt.close()



plt.figure(figsize=(8,5))
sns.boxplot(x='Category', y='Price', data=df)
plt.title("Price Distribution by Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/boxplot_price.png")
plt.close()



plt.figure(figsize=(8,5))
sns.countplot(x='Customer_Segment', data=df)
plt.title("Customer Segment Distribution")
plt.tight_layout()
plt.savefig("visualizations/customer_segment.png")
plt.close()



plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig("visualizations/heatmap.png")
plt.close()




fig1 = px.line(
    df.groupby(df['Date'].dt.to_period("M"))['Sales'].sum().reset_index(),
    x='Date',
    y='Sales',
    title="Interactive Monthly Sales Trend"
)
fig1.show()


fig2 = px.pie(
    df,
    names='Customer_Segment',
    title="Customer Segment Breakdown"
)
fig2.show()


fig3 = px.bar(
    df,
    x='Product',
    y='Sales',
    color='Category',
    title="Product Performance"
)
fig3.show()

print("Dashboard Visualizations Created Successfully ✅")
plt.figure(figsize=(10,5))

top_products = (
    df.groupby('Product')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

sns.barplot(
    x=top_products.values,
    y=top_products.index
)

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("visualizations/top_products.png")
plt.close()
