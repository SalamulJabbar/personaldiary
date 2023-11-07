import requests

api_key = '1d8527e3-01f0-4037-9f49-ae1bfc9a47e9'
word='papzola'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definitions)