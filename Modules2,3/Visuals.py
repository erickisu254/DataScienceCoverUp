# import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducability
np.random.seed(100)

# Generate a data set of 200 retirement age values
age = 5*np.random.randn(200) + 65
gpa = 4*np.random.randn(200) + 3.5

#Plot the histogram with hist() function
plt.bar(age, gpa)

plt.xlabel('Retirement Age')
plt.ylabel('Frequency of Values')
plt.title('Bar Chart in Matplotlib')
plt.show()
