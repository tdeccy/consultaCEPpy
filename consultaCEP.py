import requests
import json
import os

os.system('cls')
escUser = input('Infome o CEP: ')

url = f'https://viacep.com.br/ws/{escUser}/json/'
res = requests.get(url)

if 'Verifique a sua URL' in res.text:
    print('CEP invalido, informe um CEP correto!')
    exit()

cep = res.json()['cep']
logradouro = res.json()['logradouro']
bairro = res.json()['bairro']
localidade = res.json()['localidade']
uf = res.json()['uf']
ddd = res.json()['ddd']
complemento = res.json()['complemento']

print(f'\nCEP: {cep}\nEndereco: {logradouro}\nBairro: {bairro}\nCidade: {localidade}\nEstado: {uf}\nDDD: {ddd}\nComplemento: {complemento}')