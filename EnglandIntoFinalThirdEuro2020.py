# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 11:02:57 2021

@author: deanp

Visualization of England's Deliveries and Solo Runs into the final third,
against each of its opponents on its road to Euro 2020 final.
"""

#%%
#Load libraries

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.font_manager
import matplotlib as mpl
import numpy as np
from highlight_text import htext
#%%
#Set up Data

labels = ['vs. CRO', 'vs. SCO', 'vs. CZE', 'vs. GER', 'vs. UKR', 'vs. DEN*', 'vs. ITA*']
england_deliveries = [26, 35, 29, 31, 51, 62, 37]
england_solo_runs = [-8, -20, -15, -8, -13, -20, -16]
opponent_deliveries = [35, 24, 22, 25, 35, 33, 67]
opponent_solo_runs = [-6, -14, -10, -9, -5, -3, -30]
width = 0.2 # width of bars
x = np.arange(7) # 7 games

#%%
#Set up figure
mpl.rcParams['font.family'] = "Arial"
text_color = 'white'

#%%
#Plot

fig, ax = plt.subplots(figsize=(9, 9))
ax.grid(lw="0.5", zorder=1)
plt.bar(x-0.1, england_deliveries, width, color='#89CFF0', zorder=2)
plt.bar(x-0.1, england_solo_runs, width, color='#FFC0CB',  zorder=2)
plt.bar(x+0.1, opponent_deliveries, width, color='#89CFF0', alpha=.2, zorder=2)
plt.bar(x+0.1, opponent_solo_runs, width, color='#FFC0CB', alpha=.2, zorder=2)
plt.xticks(x, labels)
fig.set_facecolor('#313332')
ax.patch.set_facecolor('#313332')
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_color(text_color)
ax.spines["left"].set_color(text_color)
ax.tick_params(axis="both", length=0)

htext.fig_text(
    x=.12, 
    y=1.03,             
    s="England's <deliveries> and <solo runs> \ninto the final third vs. opponents.",
    highlight_textprops=[{"color": '#89CFF0', "fontweight": "bold"},
                         {"color": '#FFC0CB', "fontweight": "bold"}],
    fontsize=20,
    color=text_color,
)
fig.text(
    x=.12,
    y=.91,
    s="Euro 2020",
    fontsize=16,
    fontstyle="italic",
    fontweight="regular",
    color=text_color,
    )

ax2 = fig.add_axes([.77, .92, .12, .12])
ax2.axis("off")
img = mpimg.imread('C:/Users/deanp/OneDrive/Desktop/Football Analytics/DP_Logo.png')
ax2.imshow(img)

fig.text(
    x=.1,
    y=.025,
    s="Created by Dean Patel. Data provided by UEFA.",
    fontsize=9,
    fontstyle="italic",
    color=text_color,
    )

ax.tick_params(axis='x', colors=text_color)

ax.tick_params(axis='y', colors=text_color)
#fig.savefig('C:/Users/deanp/OneDrive/Desktop/Football Analytics/Output/EnglandFinalThirdB.png', dpi=200, bbox_inches='tight') 

plt.show()