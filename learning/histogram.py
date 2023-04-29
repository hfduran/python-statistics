# Histograma

import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt

x = [300,
     300,
     350,
     350,
     450,
     450,
     500,
     500,
     550,
     550,
     600,
     600,
     650,
     700,
     750,
     750,
     850,
     850,
     900,
     900,
     950,
     1000,
     1000,
     1000,
     1100,
     1200,
     1200,
     1250,
     1300,
     1400,
     1500,
     1500,
     1600,
     1650,
     1800,
     1900,
     2000,
     2000,
     2500,
     3000,
     ]

freq, bin_edges = np.histogram(x, bins=7)

fig, ax = plt.subplots()
ax.hist(x, bin_edges, cumulative=False)
ax.set_xlabel('x')
ax.set_ylabel('Frequency')
plt.show()

z = pd.Series(x)
print(z.describe())

fig = plt.subplot()
fig.boxplot((x), vert=False, showmeans=True, meanline=True,
           labels=('x'), patch_artist=True,
           medianprops={'linewidth': 2, 'color': 'purple'},
           meanprops={'linewidth': 2, 'color': 'red'})
plt.show()
