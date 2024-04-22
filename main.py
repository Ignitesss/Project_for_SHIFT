# это штуковина для графика для задания по логированию от ШИФТ
# я не справилась с экселем и пришла сюда, жесть

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


# inserting the data to the dataframe from Excel file
data = pd.read_excel('log_fix.xlsx', dtype={'Column1': str, 'Column2': str, 'Column3': int})

# let's draw columns 1 and 3, which are timestamps and behaviour's type
x = data['Column1']
y = data['Column3']
plt.plot(x, y, color='green', marker='o', markersize=3)
plt.show()