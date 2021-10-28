import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import urllib.request
import pandas_access as mdb
import zipfile
import re


url_1 = "https://www.miteco.gob.es/es/biodiversidad/servicios/banco-datos-naturaleza/informacion-disponible/ifn3_base_datos_1_25.aspx"
url_2 = "https://www.miteco.gob.es/es/biodiversidad/servicios/banco-datos-naturaleza/informacion-disponible/ifn3_base_datos_26_50.aspx"

downloads_dir = "ifn3"
c_dir = os.getcwd()

downloads_full_path = os.path.join(c_dir, downloads_dir) 

if not os.path.exists(downloads_full_path):
    os.makedirs(downloads_full_path)
                
def list_url(url, ext, contains):
    """Llista tots els fitxers amb format "ext" i que contenen "contains" de la direcció "url"
    """
    page = requests.get(url).text
    soup= BeautifulSoup(page, 'html.parser')
    return [node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext) and contains in node.get('href')]

list_zip_url_1 = list_url(url_1, "zip", "ifn3")
list_zip_url_2 = list_url(url_2, "zip", "ifn3")

list_total_zip = list_zip_url_1 + list_zip_url_2

# Baixa tots els zips de la llista
for zip_file in list_total_zip:  
    url_zip = "https://www.miteco.gob.es" + zip_file
    file_name = zip_file.split('/')[-1].split('_')[0]
    opener = urllib.request.build_opener()
    opener.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url_zip, downloads_full_path + "/" + file_name + '.zip')

# Extreu els fitxers mdb dels zips i eliminals
for file in os.listdir(downloads_full_path):
    with zipfile.ZipFile(os.path.join(downloads_full_path, file), 'r') as zip_ref:
        zip_ref.extractall(downloads_full_path)
    os.remove(os.path.join(downloads_full_path, file))
        
df_list = []
# Iterara tots els fitxers mdb, exportar la taula PCMatorral a dataframe i elimina'ls
for file in os.listdir(downloads_full_path):
    provincia = re.search('Ifn3p(.*).mdb', file).group(1)
    # importa la taula PCMatorral 
    df = pd.DataFrame(mdb.read_table(os.path.join(downloads_full_path, file), "PCMatorral"))
    df["Provincia"] = provincia
    df_list.append(df)
    os.remove(os.path.join(downloads_full_path, file))

df_total = pd.concat(df_list)

# Descarta les dades de Canàries
df_total = df_total[df_total["Provincia"] != '38']  
# Emplena amb 0's l'espècie per coincidir codia amb els de "codi_especies.csv"
df_total["Especie"] = df_total["Especie"].str.zfill(4)
# Importa els codis de les espècies en un diccionari
codi_especie = dict(pd.read_csv("codi_especies.csv", dtype=str).values)
# Escriu el corresponent nom de les espècies
df_total["Especie"] = df_total["Especie"].map(codi_especie) 
# Descarta els registres nuls d'espècie (són 53)
df_total = df_total[~df_total["Especie"].isna()]
# Exporta
df_total.to_csv("ifn3.csv", index=False)   
