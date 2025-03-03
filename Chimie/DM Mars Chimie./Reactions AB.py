# -*- coding: utf-8 -*-
"""

@author: antoinelaldjee-deroubaix HX1

DM De Chimie
"""

import numpy as np
import matplotlib.pyplot as plt

pK_A = 4.8
K_A = 10**(-4.8)

pH = np.linspace(0, 14, 100)
acide = 1/(1 + K_A*(10**pH))
base = K_A*(10**pH)/(1+K_A*(10**pH))

plt.plot(pH, acide, 'r',label = '% de AH')
plt.plot(pH, base, 'b', label = '% de a$^-$')
plt.xlabel('pH')
plt.ylabel('proportion')
plt.legend()
plt.title('Diagramme de distribution de l\'acide éthanoique')
plt.grid()
plt.show()
