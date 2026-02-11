import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl

# Load the data
df = pd.read_excel(r'C:\sales_performance1.xlsx')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')


# 1. Monthly Revenue Trend
monthly_revenue = df.groupby('Month')['Revenue'].sum()
monthly_revenue.plot(title='Monthly Revenue Trend')
plt.show()

# 2. Top 3 Performing Salespersons
top_salespersons = df.groupby('SalesPerson')['Revenue'].sum().nlargest(3)
print("Top 3 Salespersons:\n", top_salespersons)
