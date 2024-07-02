from google.cloud import bigquery
import pandas as pd

credencial = "./desafio-civitas-ba2f48ceea15.json"

cliente = bigquery.Client.from_service_account_json(credencial)

# Calcula a média de tempo que uma foto leva para ser recebida após ser fotografada
query = """
SELECT
AVG(TIMESTAMP_DIFF(datahora_captura, datahora, SECOND))
FROM `rj-cetrio.desafio.readings_2024_06`;
"""

resultado = cliente.query(query)

for row in resultado:
    print(row)