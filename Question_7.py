import json
import csv
import pandas as pd
from datetime import datetime, timedelta



def load_json_as_dict(file_name) -> dict:
    return json.loads(open(file_name, encoding="utf8").read())


data = pd.read_csv("./BTC-EUR.csv")


data = pd.DataFrame(data)

print(data)
print(data[['Date', 'Close']])

data_atual_menos_dez = (datetime.today() - timedelta(days=10)).strftime('%Y-%m-%d')
print(data_atual_menos_dez)

dados_dos_dez_dias = data[data.Date > data_atual_menos_dez]

print(dados_dos_dez_dias)

dados_dos_dez_dias_filtrados = dados_dos_dez_dias[['Date', 'Close']]

print(dados_dos_dez_dias_filtrados)


dados_dos_dez_dias_filtrados.to_csv("./eur_btc_rates.csv", index=None)
