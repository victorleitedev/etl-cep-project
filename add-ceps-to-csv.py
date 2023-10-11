import pandas as pd
import requests
import csv

# CONSUME CEP API
def getCEP(cep):
    print(f"https://viacep.com.br/ws/{cep}/json/")
    result = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    return result.json() if result.status_code == 200 else None

# Ask if you want to search for another CEP details
qtddCEPs = input('Quantos CEPs deseja pesquisar?')
cepsReg = 0

for i in range(int(qtddCEPs)):
    cepValue = str(input(f"Digite o CEP[{i}]: "))
    response = getCEP(cepValue)
    
    if 'erro' in response.keys():
        print("CEP inválido")
    else:
        with open('cep-db-detailed.csv','a',newline='') as f:
            # Create a Dictonary writer with the API returned keys
            print(response.keys())
            newReg = csv.DictWriter(f, fieldnames= response.keys())
            # Add the header in the first row if there's no CEPs registered
            if cepsReg == 0: newReg.writeheader()
            # Append the data in a new row in the CSV file
            newReg.writerow(response)
            cepsReg += 1
            print(cepsReg)
            print(f"Novo CEP adicionado: {response['cep']}")

# GET DATA FROM THE CSV FILE
result = pd.read_csv('cep-db-detailed.csv', encoding='unicode_escape')
print("REGISTROS:\n",result)