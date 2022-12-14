import numpy as np
import pandas as pd
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

financial = [5.5, 7.1, 6.9, 5.1, 4.6, 5.3, 5.9, 5.6, 5.5, 7.1, 6.9, 5.1, 4.6, 5.3, 5.9, 5.6, 4.7, 6.4, 6.7, 4.3, 4.1,
             5.1, 5.7, 4.7, 5.3, 6.4, 5.8, 4.9, 4.1, 4.8]
energy = [5.2, 7.4, 6.6, 5.7, 5.6, 5.5, 6.4, 6.1, 5.2, 7.4, 6.6, 5.7, 5.6, 5.5, 6.4, 6.1, 4.4, 6.6, 6.4, 4.8, 5.0, 5.3,
          6.2, 5.2, 5.0, 6.6, 5.6, 5.5, 5.0, 4.9]
technology = [7.3, 8.2, 7.1, 7.6, 8.2, 11.5, 9.2, 9.5, 7.3, 8.2, 7.1, 7.6, 8.2, 11.5, 9.2, 9.5, 6.2, 7.4, 6.9, 6.4, 7.4,
              11.1, 8.9, 8.1, 7.1, 7.4, 6.0, 7.0, 7.0, 10.3]

test_statistic, p_value = f_oneway(financial, energy, technology)
print("Test Statistic =", round(test_statistic, 2))
print("P-value =", round(p_value, 4))

df = pd.DataFrame({'scores': [5.5, 7.1, 6.9, 5.1, 4.6, 5.3, 5.9, 5.6, 5.5, 7.1, 6.9, 5.1, 4.6, 5.3, 5.9, 5.6, 4.7, 6.4,
                              6.7, 4.3, 4.1, 5.1, 5.7, 4.7, 5.3, 6.4, 5.8, 4.9, 4.1, 4.8, 5.2, 7.4, 6.6, 5.7, 5.6, 5.5,
                              6.4, 6.1, 5.2, 7.4, 6.6, 5.7, 5.6, 5.5, 6.4, 6.1, 4.4, 6.6, 6.4, 4.8, 5.0, 5.3, 6.2, 5.2,
                              5.0, 6.6, 5.6, 5.5, 5.0, 4.9, 7.3, 8.2, 7.1, 7.6, 8.2, 11.5, 9.2, 9.5, 7.3, 8.2, 7.1, 7.6,
                              8.2, 11.5, 9.2, 9.5, 6.2, 7.4, 6.9, 6.4, 7.4, 11.1, 8.9, 8.1, 7.1, 7.4, 6.0, 7.0, 7.0,
                              10.3],
                   'group': np.repeat(['financial', 'energy', 'technology'], repeats=30)})
tukey = pairwise_tukeyhsd(endog=df['scores'],
                          groups=df['group'],
                          alpha=0.05)
print(tukey)
