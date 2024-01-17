# VD_proyecto

En el presente documento detallamos las necesidades principales para ejecutar nuestro streamlit y cómo interactuar con él. Archivos necesarios para tener en carpeta local o repositorio de Github:
(COPIAR ARCHIVOS QUE ESTÁN EN EL REPOSITORIO DE GITHUB ÁLVARO)
 
•	St.py: hoja de Python donde se generan gráficas y todo lo relacionado con streamlit para visualización y worldcloud para poder representar las palabras más importantes de cada trabajo
•	Vd-definitivo: tratamiento de datos y gráficas


En primer lugar, para desarrollar todo el trabajo que hemos realizado en streamlit, decidimos crear un entorno virtual, cuyas características y paquetes esenciales se recogen en el archivo requirements.txt. 
Si desea correr el archivo en local, recomendamos seguir los siguientes pasos:
1.	Dentro de la carpeta que desee trabajar abra una terminal de Windows PowerShell.
2.	Para crear el entorno virtual introduzca el siguiente comando: python -m venv venv. El primer venv lo crea, el segundo es el nombre de la carpeta creada.
3.	Para activar el entorno virtual introduzca el siguiente comando: \venv\Scripts\activate.
4.	Para instalar los requerimientos introduzca el siguiente comando: pip install -r .\requirements.txt
5.	Una vez que se han completado estos pasos, en la misma terminal de Windows Powershell y fijándonos que seguimos trabajando en el entorno virtual (venv), introduzca el siguiente comando: streamlit run nombrearchivo.py 
Así conseguirá abrir el archivo en local, en una pestaña del navegador que esté usando en su equipo.
Si desea correr el archivo en web a través de Github, le recomendamos seguir los siguientes pasos:
1.	Crear un repositorio en Github.
2.	Subir todos los archivos necesarios especificados al principio de este documento a su repositorio.
3.	Una vez creado y comiteado el repositorio, subirlo a streamlit a través del siguiente enlace: https://share.streamlit.io/deploy. 
 Así conseguirá abrir el archivo en público, en una pestaña del navegador que esté usando en su equipo.
Ejecución de código del archivo:
En primer lugar, el archivo realiza una importación de las librerías o módulos y las clases extraídas de estas, necesarias para ejecutar el código. 
Librerías o módulos: streamlit (para la creación de la web), pandas (para manipular y analizar los datos), matplotlib.pyplot y plotly.express (ambas para la construcción de gráficas) y re (librería de expresiones regulares de Python).
Clases: wordcloud (para construir los wordclouds) y counter (para contabilizar la frecuencia de los elementos de lista).
Luego realizamos la carga del dataframe, hemos dejado comentadas varías líneas de cargas de dataframes que hemos utilizado para la construcción del dataframe final, porque consideramos que pueden ser útiles si quieren hacer otros estudios de estos datos y recurrir a las fuentes iniciales, ya que para hacer posible la subida del código a una web usando streamlit, hemos necesitado eliminar todas las variables que no han sido evaluadas en nuestro análisis y crear un  nuevo dataframe llamado df (que es el utilizado para la representación). 
El siguiente paso en el código es la creación de gráficos. 
-	Gráficas interactivas: 
Gráfico de barras interactivo: con los cuatro títulos de trabajo más relevantes que aparecen en nuestra BBDD. 
Permite si situamos el ratón sobre él:
1.	Aumentar o disminuir los índices de sus ejes.
2.	Conocer los valores exactos de cada columna si posamos el ratón sobre ella. 
Histogramas interactivos: cuatro histogramas sobre la distribución de salarios medios según el título del puesto de trabajo.
Permiten si situamos el ratón sobre ellos:
1.	Conocer los valores exactos de cada columna si posamos el ratón sobre ella. 
2.	Hacer zoom sobre determinadas partes del gráfico. 

-	Gráficas fijadas: 
Gráfico de tarta sobre los cinco principales sectores de todos en los que se reparten las ofertas de trabajo estudiadas.
Gráfico de wordcloud:  representación de los términos más repetidos, dentro de una serie de términos que hemos identificado como importantes en el sector de análisis datos, en las descripciones de las ofertas de trabajo según el tipo de título de trabajo.
