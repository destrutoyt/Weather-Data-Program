#Purpose: Create box plot for period 2 data
#Name: Miguel Garces
#Date: 4/4/2022
import pandas as pd
import matplotlib.pyplot as plt
df2 = pd.read_csv("formatdata2.csv")
df2.boxplot(); plt.suptitle('Period 2 box plot')
plt.show()
