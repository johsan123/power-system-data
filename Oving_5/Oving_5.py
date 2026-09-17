#Oppgave 1 
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt



#L_0 = 20
#t = np.linspace(0, 23, 200)
#u_1 = 20
#sigma_1 = 6
#A_1= 50

#L = L_0 + A_1*np.exp(-((t-u_1)**2)/(2*sigma_1**2))
#plt.figure()
#plt.plot(t, L, label=f"bredde på topp:{sigma_1},\n tidspunkt for topp:{u_1},\n Amplitude: {A_1}")
#plt.grid()
#plt.legend()
#plt.title("Eksperimentring med parameterverdier")
#plt.savefig("Eksperiment_3")
#plt.show()

#Oppgave 3

df = pd.read_csv("ProductionConsumption-2023.csv")
df["Time(Local)"] = pd.to_datetime(df["Time(Local)"], format="%d.%m.%Y %H:%M:%S %z",utc=True)
df["Time(Local)"] = df["Time(Local)"].dt.tz_convert("Europe/Oslo")

df = df.set_index("Time(Local)")
#print(df.describe())

#print(df.head())
#print(df.dtypes)
t = np.linspace(0,23,24)


dag = df.loc["2023-03-2"]


#Døgnprofil
plt.figure()
plt.plot(t, dag["Consumption"], label="Observerte data")
plt.title("Døgnprofil")
plt.xlabel("Tid")
plt.ylabel("Effekt")
plt.grid()
plt.legend()
plt.savefig("Dognprofil 2023-03-2")
plt.show()

#Parameter verdier
L_0 = 15750
A_1 = 3106
mu_1 = 8
sigma_1 = 2.5
A_2 = 1800
mu_2 = 19
sigma_2 = 4 
A_0 = -280
mu_0 = 3 
sigma_0 = 1.5



morning_peak =  A_1*np.exp(-((t-mu_1)**2/(2*sigma_1**2)))
evening_peak =  A_2*np.exp(-((t-mu_2)**2/(2*sigma_2**2)))
night_peak =  A_0*np.exp(-((t-mu_0)**2/(2*sigma_0**2)))
L = L_0 + night_peak +morning_peak + evening_peak


plt.figure()
plt.title("Modellert kurve")
plt.plot(t,L,label="Modellert kurve")
plt.xlabel("Tid")
plt.ylabel("Effekt")
plt.grid()
plt.legend()
#plt.savefig("Modellert kurve")
plt.show()


plt.figure()
plt.title("Observert data og modelert kurve")
plt.plot(t,dag["Consumption"], label="Observerte data")
plt.plot(t,L, label="Modellert kurve")
plt.xlabel("Tid")
plt.ylabel("Effekt")
plt.grid()
plt.legend()
plt.savefig("Modellert kurve over observert data")
plt.show()
