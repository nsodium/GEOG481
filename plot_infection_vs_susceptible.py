import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

_infection_data = pd.read_csv(r'/Users/shijinyang/Desktop/infection_rate.csv')
_infection = _infection_data['number_of_infection']
_susceptible = _infection_data['number_of_susceptible']

plt.plot(_infection, label="infected students")
plt.plot(_susceptible, label="susceptible students")
plt.title("number of infected students vs. number of susceptible students")
plt.xlabel("sections")
plt.ylabel("number of students")
plt.legend(loc='upper right')
plt.show()