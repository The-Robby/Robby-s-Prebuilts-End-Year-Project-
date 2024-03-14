import data_functions as df
import storing_password as sp

# df.update_prebuiltDB("user","Naam= 'Robbert Groffi', Adres= 'Halingenstraat 32', IsAdmin=1","UserID=1")
df.update_prebuiltDB("user", "Uitgegeven = "+str(df.getTotalBuildPrice(1))+"", "UserID = 1")