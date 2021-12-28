import pandas as p
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#Defines the key variables of the charts
Cycle_Name = ["Current Cycle","2015-2017","2011-2013","2010-2011"]
ROI = [15,120,400,3661]
Duration = [158,152,105,47]

x = np.arange(len(Cycle_Name))
width = 0.35  

#Formats the figure's graphs to be compared horrizontally 
fig, (ax,ax2) = plt.subplots(1,2)

#Generates the first graph, and the labels for each bar
ROI_bars = ax.barh(x-width/2,ROI, width, label='ROI Measured as a Multiple',color=(0.650, 0, 0.740),edgecolor="k")
Duration_bars = ax.barh(x + width/2, Duration, width, label='Duration in Weeks',color=(0,1,1),edgecolor="k")

ROI_labels = []
for i in ROI:
    ROI_labels.append((str(i)+" X"))
                       
Duration_labels = []
for i in Duration:
    Duration_labels.append((str(i)+" Weeks"))

ax.set_title('Bitcoin Bull Market Cycle ROI & Duration Comparison')
ax.legend()
ax.set_yticks([0,1,2,3])
ax.set_yticklabels(Cycle_Name)
ax.bar_label(ROI_bars,padding=3,labels=ROI_labels,label_type="edge")
ax.bar_label(Duration_bars, padding=3,labels=Duration_labels,label_type="edge")
ax.set_facecolor((0.87,0.87,0.87))
ax.set_xscale("log")#x axis set to a logarithmic scale to better visualize the comparison between the data
ax.set_xlim(0.1,15000)

fig.set_facecolor((0.87,0.87,0.87))
fig.tight_layout()

#Generates the second graph, and the labels for each bar
Cycle_Name = ["2015-2017","2011-2013","2010-2011"]
Drop = [84,86,93]
Duration2 = [52,59,23]

x = np.arange(len(Cycle_Name)) 
width = 0.35  

Drop_bars = ax2.barh(x - width/2, Drop, width, label='% Drop From Peak to Bottom',color=(0.650, 0, 0.740),edgecolor="k")
Duration2_bars = ax2.barh(x + width/2, Duration2, width, label='Duration in Weeks',color=(0,1,1),edgecolor="k")

Drop_labels = []
for i in Drop:
    Drop_labels.append((str(i)+" %"))
                       
Duration2_labels = []
for i in Duration2:
    Duration2_labels.append((str(i)+" Weeks"))


ax2.set_title('Bitcoin Bear Market Cycle Drop & Duration Comparison')
ax2.legend()
ax2.set_yticks([0,1,2])
ax2.set_yticklabels(Cycle_Name)
ax2.bar_label(Drop_bars,padding=3,labels=Drop_labels,label_type="center")
ax2.bar_label(Duration2_bars, padding=3,labels=Duration2_labels,label_type="center")
ax2.set_facecolor((0.87,0.87,0.87))

plt.subplots_adjust(left=0.088)#Formats the figure to better fit the two subplots
plt.show()
