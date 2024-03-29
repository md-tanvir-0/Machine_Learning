# -*- coding: utf-8 -*-
"""Task.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_FYeKVhBUQ8QWuv57BlNUmDtxpP7Mv3I
"""

import numpy as np
import matplotlib.pyplot as plt

# Data
semesters = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
cGPAs = np.array([2.73, 3.00, 2.00, 2.75, 3.00, 2.89, 3.12, 2.67, 3.32, 3.33])

# Linear regression
m, c = np.polyfit(semesters, cGPAs, 1)

# Plot data and regression line
plt.scatter(semesters, cGPAs)
plt.plot(semesters, m * semesters + c)

# Show plot
plt.show()

# Calculate R-squared
r_squared = np.corrcoef(semesters, cGPAs)[0, 1] ** 2

# Print R-squared
print("R-squared:", r_squared)

# Check if R-squared is close to 1
if r_squared > 0.9:
    print("The relationship is linear.")
else:
    print("The relationship is not linear.")

import numpy as np
import matplotlib.pyplot as plt

# Data
semesters = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
cGPAs = np.array([2.73, 3.00, 2.00, 2.75, 3.00, 2.89, 3.12, 2.67, 3.32, 3.33])

# Linear regression
m, c = np.polyfit(semesters, cGPAs, 1)

# Plot data and regression line
plt.scatter(semesters, cGPAs, label='Data points')
plt.plot(semesters, m * semesters + c, label=f'Regression Line: y = {m:.2f}x + {c:.2f}', color='red')

# Add labels and title
plt.xlabel('Semesters')
plt.ylabel('cGPAs')
plt.title('Linear Regression of cGPAs over Semesters')

# Display equation of the regression line
plt.legend()

# Show plot
plt.show()

# Calculate R-squared
r_squared = np.corrcoef(semesters, cGPAs)[0, 1] ** 2

# Print R-squared and interpret its value
print("R-squared:", r_squared)

if r_squared > 0.9:
    print("The relationship is strongly linear.")
elif 0.7 <= r_squared <= 0.9:
    print("The relationship is moderately linear.")
else:
    print("The relationship is weakly linear.")