def save_delta(table):
    """
    Lê um arquivo JSON da camada raw, transforma e salva como tabela Delta na camada bronze.

    Args:
        table (str): Nome da tabela a ser processada.
    """
    df = spark.read.json(f'/Volumes/raw/pokemon/pokemon_raw/{table}')
    bronze_path = f'bronze.pokemon.{table}'
    
    (df.distinct()
       .coalesce(1)
       .write
       .format('delta')
       .mode('overwrite')
       .saveAsTable(bronze_path))
