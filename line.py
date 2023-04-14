#Purpose: Create Celsius plot comparing period 1 and period 2
#Name: Miguel Garces
#Date: 4/4/2022
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata.csv") #baseline data is period 1 (older)
df2 = pd.read_csv("formatdata2.csv") #data for period 2 (more recent)
plt.figure(); df1.Humidity.plot(label = 'Period 1'); df2.Humidity.plot(label = 'Period 2'); plt.legend(loc='best'); plt.suptitle('Humidity')
plt.show()