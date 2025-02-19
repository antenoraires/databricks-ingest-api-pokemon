df  = spark.read.json('/Volumes/raw/pokemon/pokemon_raw/pokemon_list')
bronze_path = 'bronze.pokemon.pokemon_list'
df.distinct()
    .coalesce(1)
    .write
    .format('delta')
    .mode('overwrite')
    .saveAsTable(bronze_path)