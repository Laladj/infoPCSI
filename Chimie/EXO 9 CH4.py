from matplotlib import pyplot as plt
import numpy as np
t = [0, 5 ,10 , 20, 30, 40, 50, 60]
A = [1.5, 1.23, 1.01, 0.68, 0.46, 0.31, 0.21, 0.14]
plt.plot(t,A)
dA = np.gradient(A,t)
plt.plot(dA,t)