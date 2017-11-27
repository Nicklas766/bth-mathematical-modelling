import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import UnivariateSpline




def back_diff(y_array, t_array):
   "Differenskvot bakåt"
   new_list = []

   for index, item in enumerate(y_array, start=0):
        # print(index, item)

        # x2 - x1
        h = t_array[index] - t_array[index - 1]
        # get f(index)
        f1 = y_array[index]
        # get f(index - h)
        f2 = y_array[index - h]
        # calculation
        k = (f1 - f2) / h

        if index == 0:
            k = float('NaN')
        new_list.append(k)
   return new_list

def forward_diff(y_array, t_array):
   "Differenskvot framåt"
   new_list = []

   for index, item in enumerate(y_array, start=0):
        if index != 4:
            # print(index, item)

            # x2 - x1
            h = t_array[index + 1] - t_array[index]
            print("H:", h)
            # get f(index)
            f1 = y_array[index + h]
            print("f(a + h):",f1)
            # get f(index)
            f2 = y_array[index]
            print("f(a):",f2)
            # calculation
            k = (f1 - f2) / h
            print("ANSWER:", k)
            print("---------------------")
            new_list.append(k)
        else:
            k = float('NaN')
            new_list.append(k)
   return new_list



t = range(0, 5)
# t = [0, 1, 2, 3, 4]
y = [0, 20, 15, 30, 45]

print(back_diff(y, t));

print(forward_diff(y, t));

df = pd.DataFrame({'Minuter': t, 'Antal personer i kö': y})
dt = pd.DataFrame({'Minuter': t, 'Derivative': back_diff(y, t)})
dt2 = pd.DataFrame({'Minuter': t, 'Derivative': forward_diff(y, t)})

ax1= df.plot(x='Minuter', y='Antal personer i kö', style='ro-')
dt.plot(ax=ax1, x='Minuter', y='Derivative', style='bo-', secondary_y=False)
dt2.plot(ax=ax1, x='Minuter', y='Derivative', style='go-', secondary_y=False)

plt.grid(True)

# plt.ylabel('Antal personer i kö')
# plt.xlabel('Minuter')
# # plt.axis(t)
# plt.show()

plt.grid(True)

plt.savefig('timeseries_derivative.png')
plt.show()
