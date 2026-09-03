import pandas as pd
import matplotlib.pyplot as plt
måneder = ["januar", "februar", "mars", "april", "mai", "juni", "juli", "august", "september", "oktober", "november", "desember"]



fil = pd.read_csv("load/forbruk_2025.csv")
fil["Unnamed: 0"] = pd.to_datetime(fil["Unnamed: 0"],utc=True).dt.tz_convert('Europe/Oslo')

#print(fil.columns)
#print(fil.head()) 
#print(fil.dtypes)

fil = fil.set_index("Unnamed: 0")
load_monthly = fil["Actual Load"].resample("ME").mean()

resultat = pd.DataFrame(load_monthly)
resultat.index = måneder    # gir datoer måneds navn

#print(resultat)
#resultat.to_csv("results/manedlig_last_2025.csv",index=False)
plt.plot(resultat, marker="x")
plt.xlabel("måned")
plt.ylabel("gjennomsnittlig last(MW)")
plt.title("månedlig last i 2025")
plt.tight_layout()
plt.xticks(rotation=45)
plt.grid()
plt.savefig("results/manedlig_last_2025.png")
plt.show()


load_monthly_max = fil["Actual Load"].resample("ME").max()
#print("maksimal måntlig last: ", load_monthly_max)

load_monthly_min = fil["Actual Load"].resample("ME").min()
#print("Minimal måntlig last:", load_monthly_min)

load_monthly_std =fil["Actual Load"].resample("ME").std()
#print("std", load_monthly_std)

manedlig_last_statistikk = pd.concat([load_monthly_max, load_monthly_min, load_monthly_std], axis=1,  )
manedlig_last_statistikk.index = måneder
manedlig_last_statistikk.columns = ["Maksimal last", "Minimal last", "Standardavik"]
#print(manedlig_last_statistikk)

#manedlig_last_statistikk.to_csv("results/manedlig_last_statistikk_2025.csv",index=True)