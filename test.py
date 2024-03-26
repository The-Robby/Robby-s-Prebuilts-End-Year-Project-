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

# ram = df.info_catcher_in_dictionary('ram')
# ram_info = [{key: ram_dict[key] for key in ('id', 'naam')} for ram_dict in ram]

# ram = df.info_catcher_in_dictionary('ram')
# ram2 = df.info_catcher_in_dictionary('ram', 1)
# ram_info = [{key: ram_dict[key] for key in ('id', 'naam', 'prijs')} for ram_dict in ram]
# print(ram)
# print(ram2)
# print(ram_info)
# print(df.getIdAndNamesFromTable('ram'))
# dict = {"kaka": "kaka", "pipi": 3, "zak": 500}
# list = [{"kaka": "kaka", "pipi": 3, "zak": 500}, {"kaka": "kaka", "pipi": 3, "zak": 500}]
# print(len(list))

# print(df.make_cart([{'naam': 'I9 13900K', 'clock': '5,2GHz', 'cores': 24, 'socket': '1700', 'stock': 5, 'prijs': 675.95, 'leverancier': 'Intel'}, {'naam': 'Nvidia GeForce RTX 4080', 'clock': '2535MHz', 'capaciteit': '16GB', 'gddr': '6X', 'stock': 1, 'prijs': 1479.0, 'leverancier': 'GIGABYTE'}, {'naam': 'RM1000e V2 PSU', 'watt': 1000, 'type': 'Modulair', 'stock': 4, 'prijs': 144.9, 'leverancier': 'Corsair'}, {'naam': 'Vengeance', 'clock': '6800MGh', 'capaciteit': '32GB', 'ddr': 5, 'stock': 7, 'prijs': 152.9, 'leverancier': 'Corsair'}, {'naam': 'ROG STRIX B760-F GAMING', 'socket': '1700', 'ddr': 5, 'gddr': '6X', 'stock': 8, 'prijs': 269.0, 'leverancier': 'ASUS'}, {'naam': 'Big Tower', 'aantalfans': 4, 'afmetingen': '100x100x40', 'stock': 2, 'prijs': 149.99, 'leverancier': 'Corsair'}, {'naam': '990 Pro', 'type': 'M.2', 'capaciteit': '2TB', 'stock': 4, 'prijs': 190.0, 'leverancier': 'SAMSUNG'}]))