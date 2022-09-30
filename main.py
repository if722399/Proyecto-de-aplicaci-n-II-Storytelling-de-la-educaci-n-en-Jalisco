# Librerías
import pandas as pd
import numpy as np
import functions as fn



# Cargar datos
D = pd.read_csv('final_data.csv', index_col=0)
df = D.copy()
df.head()


numeric_performers = df.select_dtypes(exclude=['object'])
categoric_performers = df.select_dtypes(include=['object'])


# Informacion de Jalisco que será utilizada posteriormente para graficar
data = df.copy()
file_name = 'limitemunicipal_mgj2012_modificadodecreto26837'
jalisco = fn.get_shp_files(basedir='.', object_type=file_name)
jalisco = jalisco[list(jalisco.keys())[0]]










