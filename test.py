import data_functions as df
import storing_password as sp
from flask import jsonify

# df.update_prebuiltDB("user","Naam= 'Robbert Groffi', Adres= 'Halingenstraat 32', IsAdmin=1","UserID=1")
# print(sp.get_userID('Robbert'))
# print(df.getDataFromTable('cpu'))
# table = 'kaka'
# print(f'''SELECT * FROM {table}''')
# print(df.getIdAndNamesFromTable('ram'))
# components = {
#     'cpu': df.getNamesFromTable('cpu'),
#     'gpu': [{'id': 1, 'name': 'GPU 1'}, {'id': 2, 'name': 'GPU 2'}],
#     'ram': df.getNamesFromTable('ram')
# }
# print(jsonify(components['ram']))
# df.inserDataIntoTable('cpu', 'Naam, Clock, Cores, Socket, Stock, Prijs, LeverancierID', '"i9-14900K", "6,0GHz", 24, "1700", 9, 639.00, 2')
# df.update_prebuiltDB('cpu','Naam = "i9-13900K"', 'CPUID = 1')
# print(df.get_foreign_key_name('type', 2))
ram = df.info_catcher_in_dictionary('ram')
ram_info = [{key: ram_dict[key] for key in ('id', 'naam')} for ram_dict in ram]

print(ram_info)

print(df.getIdAndNamesFromTable('ram'))