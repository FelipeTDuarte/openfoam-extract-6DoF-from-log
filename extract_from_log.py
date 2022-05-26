# -*- coding: utf-8 -*-
"""
Created on Mon May 16 20:10:07 2022

@author: FelipeDuarte
"""


import re
import pandas as pd


remove ='():='

time_step = []
tensor =[]
centre_of_mass = []
centre_of_rotation = []
linear_velocity = []
angular_velocity = []


with open("log.overInterDyMFoam.txt", "r", encoding="utf=8") as file:
    text = file.readlines()

    for step in text:
      if "Time" in step:
          if step.startswith('Time = '):
              time = [float(s) for s in re.findall(r'-?\d+\.?\d*', step)]
              time_step.append(time)
    
    for parameter in text:
        if "Orientation" in parameter:
            for c in remove:
                parameter = parameter.replace(c,'')
                t = parameter.split()
                t.pop(0)
            tensor.append(t)
            
    for parameter in text:
        if "Centre of mass" in parameter:
            for c in remove:
                parameter = parameter.replace(c,'')
                cm = parameter.split()
            centre_of_mass.append(cm)
   
    for parameter in text:
        if "Centre of rotation" in parameter:
            for c in remove:
                parameter = parameter.replace(c,'')
                cr = parameter.split()
            centre_of_rotation.append(cr)
            
    for parameter in text:
        if "Linear velocity" in parameter:
            for c in remove:
                parameter = parameter.replace(c,'')
                lv = parameter.split()
            linear_velocity.append(lv) 
   
    for parameter in text:
        if "Angular velocity" in parameter:
            for c in remove:
                parameter = parameter.replace(c,'')
                av = parameter.split()
            angular_velocity.append(av)  
    
dt=pd.DataFrame(time_step)

do=pd.DataFrame(tensor)
dto = pd.concat([dt,do],axis = 1)
dto.columns = "Time", "t11", "t12","t13", "t21", "t22","t23", "t31", "t32","t33"
dto.to_csv('orientation.csv')

dcm=pd.DataFrame(centre_of_mass)
dcm.drop([0,1,2], axis=1, inplace=True)
dtcm = pd.concat([dt,dcm],axis = 1)
dtcm.columns = "Time", "x", "y","z"
dtcm.to_csv('centre_of_mass.csv')

dcr=pd.DataFrame(centre_of_rotation)
dcr.drop([0,1,2], axis=1, inplace=True)
dtcr = pd.concat([dt,dcr],axis = 1)
dtcr.columns = "Time", "x", "y","z"
dtcr.to_csv('centre_of_rotation.csv')

dlv=pd.DataFrame(linear_velocity)
dlv.drop([0,1], axis=1, inplace=True)
dtlv = pd.concat([dt,dlv],axis = 1)
dtlv.columns = "Time", "x", "y","z"
dtlv.to_csv('linear_velocity.csv')

dav=pd.DataFrame(angular_velocity)
dav.drop([0,1], axis=1, inplace=True)
dtav = pd.concat([dt,dav],axis = 1)
dtav.columns = "Time", "x", "y","z"
dtav.to_csv('angular_velocity.csv')