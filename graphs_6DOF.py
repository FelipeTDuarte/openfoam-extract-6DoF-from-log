# -*- coding: utf-8 -*-
"""
Created on Wed May 25 20:20:11 2022

@author: FelipeDuarte
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


dto = pd.read_csv('orientation.csv')
dtcm= pd.read_csv('centre_of_mass.csv')

dto ['roll'] = np.arctan(dto['t32']/dto['t33'])
dto ['pitch'] = np.arctan(-dto['t31']/(np.arctan(dto['t32']) + np.square(dto['t33'])))
dto ['yaw'] = np.arctan(dto['t21']/dto['t11'])


print(dto)


plt.scatter(dtcm['Time'], dtcm['x'])
plt.show()
plt.scatter(dtcm['Time'], dtcm['y'])
plt.show()
plt.scatter(dtcm['Time'], dtcm['z'])
plt.show()
plt.scatter(dtcm['Time'], dto ['roll'])
plt.show()
plt.scatter(dtcm['Time'], dto ['pitch'])
plt.show()
plt.scatter(dtcm['Time'], dto ['yaw'])
plt.show()