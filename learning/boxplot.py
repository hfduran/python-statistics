# Boxplot

import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# nesse set de dados, existem dois outliers: 85 e 86
# espera-se que o boxplot represente isso
dados = [20, 25, 25, 27, 28, 31, 33, 34, 36, 37, 44, 50, 59, 85, 86]

z = pd.Series(dados)
print(z.describe())

fig = plt.subplot()
fig.boxplot((dados), vert=False, showmeans=True, meanline=True,
           labels=('x'), patch_artist=True,
           medianprops={'linewidth': 2, 'color': 'purple'},
           meanprops={'linewidth': 2, 'color': 'red'})
plt.show()