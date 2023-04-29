# Média simples

import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot

dados = [8.0, 3.2, 4.5, 6.7]
dados_nan = [8.0, 3.2, np.nan, 4.5, 6.7]

# cria-se um array np para os dados
dados_np = np.array(dados)
dados_nan_np = np.array(dados_nan)
dados_nan_pd = pd.Series(dados_nan)

# a funcao np.mean também é um metodo do array np
print(np.mean(dados_np))
print(dados_np.mean())

# para fazer media com nan:
print(np.nanmean(dados_nan))
print(dados_nan_pd.mean())
