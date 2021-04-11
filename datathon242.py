"""
Stanford Open Datathon 2021
Team No. 242 
Track 2

author: Nina Carlson
4/10/21

"""

# import necessary python libraries 

import matplotlib.pyplot as plt
#import pandas as pd
import numpy as np 
import csv


    
labels = []

year1rates = [] # 2020 admissions rates 

year2rates = [] # 2019 admissions rates 


# read in and parse csv file 
    
f = open('admissionsdata.csv', newline = '')

for row in f:
    elements = row.split(',')

    labels.append(elements[0])

    year1rates.append(float(elements[1]))

    year2rates.append(float(elements[2]))



# configure plot 

x = np.arange(len(labels))

width = 0.35

fig, ax = plt.subplots(num = None, figsize = (20,15), dpi = 80, facecolor = 'w', edgecolor = 'k')

rects1 = ax.bar(x-width/2, year1rates, width, label = '2020 admissions rates (%)')

rects2 = ax.bar(x+width/2, year2rates, width, label = '2019 admissions rates (%)')

ax.set_ylabel('Admission Rates')
ax.set_title('Comparing 2019 and 2020 Admission Rates at 18 Institution Across the US')
ax.set_xticks(x)
ax.set_xticklabels(labels) 
ax.set_xticklabels(labels = labels, rotation= 90)
ax.legend()

def autolabel(rects):

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height), xy = (rect.get_x() + rect.get_width()/2, height), xytext = (0,3), textcoords="offset points", ha = 'center', va = 'bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()





