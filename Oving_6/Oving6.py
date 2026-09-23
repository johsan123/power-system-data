import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

t = np.linspace(0,24,200)
A = 800
mu_1 = 13
sigma_1 = 2



G = A*np.exp(-((t-mu_1)**2/(2*sigma_1**2)))

plt.figure()
plt.plot(t, G, label = "Inntstråling")
plt.show()

#Del 2

df = pd.read_csv("pvgis_soldata.csv",skiprows=8,nrows=8760)
#print(df.head())
#print(df.columns)

df["time"] = pd.to_datetime(df["time"], format="%Y%m%d:%H%M").dt.round("h")
df = df.set_index("time")
#print(df.head())

daglig_sol = df["G(i)"].loc["2022-06-06"]

print(daglig_sol)


plt.figure(figsize=(7,4))
plt.plot(daglig_sol,label="inntråling")
plt.grid()
plt.tight_layout()
plt.xlabel("Tid")
plt.ylabel("Sol innstråling")
plt.legend()
plt.title("Global innstråling 2022-06-06")
plt.savefig("results/Global innstråling 2022-06-06.png")
plt.show()