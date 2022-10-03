# Proyecto de aplicación II Storytelling de la educación en Jalisco
## Descripción
En este repositorio se encuentra el segundo proyecto de aplicación del laboratorio de procesamiento de datos  en donde a partir de la información proveniente de 4 datasets de la educación en Jalisco que tratan acerca de:
<br>
* Inmuebles
* Conectividad
* Performance
* Personal
<br>

se desarrolló un análisis con el cual se pudo describir de manera clara la situación en esos años de la educación en Jalisco, estos hallazgos se fueron registrando en el archivo **notebook.ipynb.**

<br><br>

## Desarrollo
Para el desarrollo de este análisis se desarrolló un app data que funciona de manera interactiva con la información de nuestro dataset final con el cual se pueden análizar diagramas de dispersión, plot lines de doble eje, el mapa del estado de jalisco con el promedio de la variable en cuestión por municipio y distintos dataframes con estadísticos descriptivos que nos ayudan a realizar análisis cruzados.

De esta manera el notebook queda libre de código y se utiliza principalmente para el registro de hallazgos asi como la presentación de los gráficos que resultaron ser más relevantes a lo largo de este proceso.
<br>
* **Aplicación:** Para poder correr la aplicación es necesario clonar este repositorio, instalar las dependencias que están en el archivo requirements.txt y correr el comando `streamlit run app.py`
<br><br>
## Funcionalidades
Dentro de la aplicación se pueden elegir distintas configuraciones para realizar el análisis, los pasos para realizar esta configuración son las siguientes:
* Elegir el dataset a analizar.
* Elegir la principal variable del análisis.
* Elegir si la segunda variable con la cual se va a contrastar y realizar el análisis cruzado será numérica o categórica.
* Elegir la segunda variable correpondiente al tipo que se eligió previamente.
* Observar métricas y visualizaciones para el registro de hallazgos.
### Ejemplo de análisis con variable secundaria numérica:
![image](https://user-images.githubusercontent.com/54387832/193589954-47651e53-96ed-47d5-87f9-68962bdb92c3.png)
![image](https://user-images.githubusercontent.com/54387832/193590088-66d00203-1426-46dd-be14-f5cdf43c8441.png)
![image](https://user-images.githubusercontent.com/54387832/193590327-be7ea75a-74c1-42d2-bc76-da4bf40b8272.png)
![image](https://user-images.githubusercontent.com/54387832/193590514-47cd611b-2e4d-4124-b92d-ebbf2a6c45f4.png)

<br><br>

### Ejemplo de análisis con variable secundaria categórica:
![image](https://user-images.githubusercontent.com/54387832/193591315-5cf934bd-ec78-427c-aba5-067ce20bf126.png)

