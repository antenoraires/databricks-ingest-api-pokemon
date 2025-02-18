import requests
import datetime
import json

url = 'https://pokeapi.co/api/v2/pokemon?limit=2000'

now= datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
path = f'/Volumes/raw/pokemon/pokemon_raw/pokemon_list/{now}.json'

response = requests.get(url)

data = response.json()
data_save = data['results']

with open(path, 'w') as f:
    json.dump(data_save, f)