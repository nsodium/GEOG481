import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


_infection_data = pd.read_csv(r'/Users/nahleen/Documents/GEOG481/infection_rate.csv')
peak_infection_ind = np.argmax(_infection_data['infection_rate'])
peak_rate = _infection_data['infection_rate'][peak_infection_ind]
peak_rate_building = _infection_data['building'][peak_infection_ind]

print(_infection_data[['building','infection_rate']])
print("peak infection happend at section: ", np.argmax(_infection_data['infection_rate']), "\n")
print("peak infection rate is: ", peak_rate, "\n")
print("peak infection rate happend in building: ", peak_rate_building, "\n")

'''
plt.plot(_infection_data['infection_rate'])
plt.title('infection rate at each section')
plt.xlabel('sections')
plt.ylabel('infection rates')
plt.show()
'''

_situ_data = pd.read_csv(r'/Users/nahleen/Documents/GEOG481/disease_csv.csv')
_situ_data.fillna(0, inplace=True)
_numeric_situ_data = _situ_data.select_dtypes(exclude=['object'])
#print(_numeric_situ_data)
'''
plt.plot(_numeric_situ_data)
plt.show()
'''
_situ_data_AHS = _numeric_situ_data['AHS 1'] + _numeric_situ_data['AHS 2'] + _numeric_situ_data['AHS 3']
_situ_data_ENG = _numeric_situ_data['ENG 1'] + _numeric_situ_data['ENG 2'] + _numeric_situ_data['ENG 3']
_situ_data_ENV = _numeric_situ_data['ENV 1'] + _numeric_situ_data['ENV 2'] + _numeric_situ_data['ENV 3']
_situ_data_ARTS = _numeric_situ_data['ARTS 1'] + _numeric_situ_data['ARTS 2'] + _numeric_situ_data['ARTS 3']
_situ_data_SCI = _numeric_situ_data['SCI 1'] + _numeric_situ_data['SCI 2'] + _numeric_situ_data['SCI 3']
_situ_data_MATH = _numeric_situ_data['MATH 1'] + _numeric_situ_data['MATH 2'] + _numeric_situ_data['MATH 3']

_agg_situ_data = pd.DataFrame([_situ_data_AHS,
                               _situ_data_ENG,
                               _situ_data_ENV,
                               _situ_data_ARTS,
                               _situ_data_SCI,
                               _situ_data_MATH]).transpose()
#print(_agg_situ_data)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(180, 60))
ax1.plot(_infection_data['infection_rate'], label='infection rate')
ax1.legend(loc='upper right')
ax1.set_title("infection rate at each section")
ax1.set_ylabel("infection rates")
ax2_x = np.arange(40)
ax2.bar(ax2_x+0.00, _agg_situ_data[0], width=0.1, color = 'b', label='AHS')
ax2.bar(ax2_x+0.1, _agg_situ_data[1], width=0.1, color = 'm', label='ENG')
ax2.bar(ax2_x+0.2, _agg_situ_data[2], width=0.1, color = 'g', label='ENV')
ax2.bar(ax2_x+0.3, _agg_situ_data[3], width=0.1, color = 'y', label='ARTS')
ax2.bar(ax2_x+0.4, _agg_situ_data[4], width=0.1, color = 'c', label='SCI')
ax2.bar(ax2_x+0.5, _agg_situ_data[5], width=0.1, color = 'r', label='MATH')

ax2.legend(loc='upper right')
ax2.set_title("number of infected students in each faculty")
ax2.set_xlabel("sections")
ax2.set_ylabel("number of infected students")
plt.show()
