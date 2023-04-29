# função para média ponderada

import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot

dados = [8.0, 3.2, 4.5, 6.7]
pesos = [1.0, 2.0, 1.0, 3.0]

print(np.average(dados, weights=pesos))