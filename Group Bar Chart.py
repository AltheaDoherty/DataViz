import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('SalesData.csv')

data.plot(x='Month', kind='bar', stacked=False)

plt.xlabel('Month')
plt.ylabel('Sales')

plt.title('Monthly Sales of Product A, B, and C')

plt.grid(True, linewidth=0.1)
plt.xticks(rotation=45)  
plt.tight_layout()  
plt.show()
