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



property = ['AULAS_EXISTENTES','AULAS_USO','BENEFICIARIOS_ALIMENTOS_DIF_2014_digit','CONECTIVIDAD_mbs']
investment = []
performance = []
personal = []

total_variables = ['MATRICULA_TOTAL'] + property + investment + performance + personal 



