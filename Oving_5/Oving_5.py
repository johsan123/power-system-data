#Oppgave 1 
import math
import numpy as np
import matplotlib.pyplot as plt
L_0 = 20
t = np.linspace(0, 23, 200)
u_1 = 20
sigma_1 = 6
A_1= 50

L = L_0 + A_1*np.exp(-((t-u_1)**2)/(2*sigma_1**2))
plt.figure()
plt.plot(t, L, label=f"bredde på topp:{sigma_1},\n tidspunkt for topp:{u_1},\n Amplitude: {A_1}")
plt.grid()
plt.legend()
plt.title("Eksperimentring med parameterverdier")
plt.savefig("Eksperiment_3")
plt.show()



