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



property = ['aulas_existentes','aulas_uso','beneficiarios_alimentos_dif_2014_digit','conectividad_mbs']
investment = ['inversion_aulas_interactivas_2015','inversion_aulas_interactivas_2014','inversion_aulas_interactivas_2013','inversion_aulas_provisionales_2013','inversion_aulas_provisionales_2014','inversion_aulas_provisionales_2015','inversion_infraestructura_educativa_estatal_2014_(recurso_2013)','inversion_infraestructura_educativa_estatal_2015_(recurso_2013)','observacion_mobiliario_piezas','observacion_mobiliario_alumnos','observacion_mobiliario_matricula']
performance = ['deserciin_intracurricular','reprobaciin','reprobaciin__con_regularizados','nivel_i_lenguaje_y_comunicacian_(%)','nivel_ii_lenguaje_y_comunicacian_(%)','nivel_iii_lenguaje_y_comunicacian_(%)','nivel_iv_lenguaje_y_comunicacian_(%)','nivel_i_matematicas_(%)','nivel_ii_matematicas_(%)','nivel_iii_matematicas_(%)','nivel_iv_matematicas_(%)','eficiencia_terminal']
personal = ['grupos','docenete_educacion_fisica','docente_actividades_artisticas','docente_actividades_tecnonologicas','docente_de_idiomas','personal_de_administrativo_y_servicios','director_con_grupo','director_sin_grupo','docentes']

total_variables = ['matricula_total'] + property + investment + performance + personal 



