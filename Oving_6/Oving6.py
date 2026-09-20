import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,24,200)
A = 800
mu_1 = 13
sigma_1 = 4



G = A*np.exp(-((t-mu_1)**2/(2*sigma_1**2)))

plt.figure()
plt.plot(t, G, label = "Inntstråling")
plt.show()