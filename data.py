import pandas as pd 

hankedata = pd.read_csv("turku_hankkeet.csv")

hankedata = hankedata.drop(['StrateginenOhjelma','SidosryhmaRooli','Aihepiiri','ProjektiId','JulkaistavaProjektikuvaus','Kohderyhma'], axis=1)
hankedata["Hanke"].replace({"Tämä on hanke": None },inplace=True)
hankedata = hankedata.dropna(subset=['Hanke','AlkuPvm','MenotYhteensa'])

hankedata.to_csv("muokattu_turku_hankkeet.csv")