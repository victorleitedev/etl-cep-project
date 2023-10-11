# viacep.com.br/ws/01001000/json/
import pandas as pd
import requests

# CONSUME CEP API
def getCEP(cep):
    print(f"https://viacep.com.br/ws/{cep}/json/")
    result = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    return result.json() if result.status_code == 200 else None

# GET DATA FROM THE CSV FILE
df = pd.read_csv("cep-db-origin.csv")
# List all the ceps stored in the CSV file
adressCEPs = df["cep"].tolist()

print(adressCEPs)
