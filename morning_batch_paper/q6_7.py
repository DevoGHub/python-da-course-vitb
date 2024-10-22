import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Department": ["Marketing", "Sales", "IT", "HR", "Finance"],
    "Budget": [120,150,200,80,100]
}

df = pd.DataFrame(data=data)
print(df)

plt.bar(df['Department'],df['Budget'])
plt.xlabel("Department")
plt.ylabel("Budget")
plt.show()