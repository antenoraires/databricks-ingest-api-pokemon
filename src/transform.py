import requests
import datetime
import json 
from multiprocessing import Pool
from load import save_delta

df = spark.table('bronze.pokemon.pokemon_list')
url_list = df.toPandas()["url"].tolist()

def get_pokemon_data(url):
    data = requests.get(url).json()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"/Volumes/raw/pokemon/pokemon_raw/pokemon_details/{data['id']}_{now}.json"
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

with Pool(10) as p:
    p.map(get_pokemon_data, url_list)
dbutils.fs.mkdirs('/Volumes/raw/pokemon/pokemon_raw/pokemon_detaisl')

# Exemplo de uso
table = dbutils.widget.get("table")
save_delta(table)