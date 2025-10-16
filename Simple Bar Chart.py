import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('SalesData.csv’)  

fig, ax = plt.subplots()

data.plot(x='Month', y='Product_A_Sales', kind='bar', ax=ax, color='skyblue’)

plt.xlabel('Month’)
plt.ylabel('Product A Sales’)
plt.title('Monthly Sales of Product A’)
plt.xticks(rotation=45)  
plt.tight_layout()
plt.show()
