import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud
import re as re 
from collections import Counter 

# Cargar tus DataFrames aquí
#data_ds=pd.read_csv('DataScientist.csv')
#data_da=pd.read_csv('DataAnalyst.csv')
#data_de=pd.read_csv('DataEngineer.csv')
#data_ba=pd.read_csv('BusinessAnalyst.csv')
df_ds=pd.read_csv('df_ds.csv')
df_da=pd.read_csv('df_da.csv')
df_de=pd.read_csv('df_de.csv')
df_ba=pd.read_csv('df_ba.csv')
#data_ds = data_ds.drop(['Unnamed: 0','index'],axis=1)
#data_da = data_da.drop(['Unnamed: 0'],axis=1)
#data_ba = data_ba.drop(['Unnamed: 0','index'],axis=1).head(3692)
#data = pd.concat([data_ds,data_da,data_de,data_ba]).reset_index(drop=True)
#data_to_csv = data.to_csv('data.csv')
#df = data.drop(['Rating', 'Company Name', 'Headquarters', 'Founded', 'Type of ownership', 'Competitors', 'Salary Estimate', 'Easy Apply', 'Industry', 'Revenue', 'Location', 'Size'], axis=1)
df=pd.read_csv('df.csv')
# Título de la aplicación
st.title('Análisis de Trabajos en el Ámbito de Datos')

# Gráfico 1
st.header('Distribución de tipos de trabajo')
trabajos_1 = ['Business Analyst', 'Data Analyst', 'Data Engineer', 'Data Scientist']
st.bar_chart(df[df['Job Title'].isin(trabajos_1)]['Job Title'].value_counts())

# Gráfico 2
st.header('Distribución de títulos de trabajo "Senior"')
trabajos_2 = ['Senior Data Engineer', 'Senior Data Analyst', 'Senior Business Analyst', 'Senior Data Scientist']
st.bar_chart(df[df['Job Title'].isin(trabajos_2)]['Job Title'].value_counts())

# Gráfico 3
st.header('Distribución de Sectores')
df_filtrado = df[df['Sector'] != '-1']
conteo_sectores = df_filtrado['Sector'].value_counts()
top_sectores = conteo_sectores[:5]
otros = conteo_sectores[5:].sum()
top_sectores['Otros'] = otros
colores = ['blue', 'yellow', 'green', 'orange', 'purple', 'red']
fig, ax = plt.subplots()
ax.pie(top_sectores, labels=top_sectores.index, autopct='%1.1f%%', startangle=140, colors=colores)
ax.set_title('Distribución de Sectores')
st.pyplot(fig)

# Gráficos 4, 5, 6 y 7 (Histogramas de Salarios)
# Definir límites de bins
#bin_edges = list(range(0, 201, 5))

# Gráficos 4, 5, 6 y 7 (Histogramas de Salarios)
#def mostrar_histograma(df, title):
 #   fig = px.histogram(df, x='Salary_average', title=title, nbins=len(bin_edges)-1, range_x=[0, 200], histnorm='percent', 
  #                     labels={'Salary_average': 'Salario Promedio'},
   #                    category_orders={'Salary_average': bin_edges})
def mostrar_histograma(df, title):
    fig = px.histogram(df, x='Salary_average', title=title,nbins=35)
    # Configurar ejes x e y
    fig.update_xaxes(range=[0, 200], dtick=20) 
    fig.update_yaxes(range=[0, 140])
    st.plotly_chart(fig)

st.header('Salarios Promedio por Posición')
mostrar_histograma(df_ds, 'Salario promedio Data Scientist')
mostrar_histograma(df_da, 'Salario promedio Data Analyst')
mostrar_histograma(df_de, 'Salario promedio Data Engineer')
mostrar_histograma(df_ba, 'Salario promedio Business Analyst')

# Palabras originales y de reemplazo
palabras_originales = ['COMPUTER SCIENCE', 'ENGINEERING DEGREE', ' MS ', 'BUSINESS ANALYTICS', 'SCRUM MASTER',
                       'MACHINE LEARNING', ' ML ', 'POWER BI', 'ARTIFICIAL INTELLIGENCE', ' AI ', 'ALGORITHMS',
                       'DEEP LEARNING', 'NEURAL NETWORK', 'NATURAL LANGUAGE PROCESSING', 'DECISION TREE', 'CLUSTERING', 'PL SQL']

palabras_reemplazo = ['COMPUTER_SCIENCE', 'ENGINEERING_DEGREE', ' MASTER ', 'BUSINESS_ANALYTICS', 'SCRUM_MASTER',
                      'MACHINE_LEARNING', ' MACHINE_LEARNING ', 'POWER_BI', 'ARTIFICIAL_INTELLIGENCE', ' ARTIFICIAL_INTELLIGENCE ',
                      'ALGORITHM', 'DEEP_LEARNING', 'NEURAL_NETWORK', 'NATURAL_LANGUAGE_PROCESSING', 'DECISION_TREE', 'CLUSTER', 'PLSQL']

# Aplicar reemplazo en el DataFrame
for original, reemplazo in zip(palabras_originales, palabras_reemplazo):
    df['Job Description'] = df['Job Description'].str.replace(original, reemplazo, regex=True)

# Definir palabras de interés
palabras_interes = ['COMPUTER_SCIENCE', 'MASTER', 'MBA', 'SQL', 'PYTHON', 'R', 'PHD', 'BUSINESS_ANALYTICS',
                    'SAS', 'PMP', 'SCRUM_MASTER', 'STATISTICS', 'MATHEMATICS', 'MACHINE_LEARNING', 'ARTIFICIAL_INTELLIGENCE',
                    'ECONOMICS', 'TABLEAU', 'AWS', 'AZURE', 'POWER_BI', 'ALGORITHM', 'DEEP_LEARNING', 'NEURAL_NETWORK',
                    'NATURAL_LANGUAGE_PROCESSING', 'DECISION_TREE', 'REGRESSION', 'CLUSTER', 'ORACLE', 'EXCEL', 'TENSORFLOW',
                    'HADOOP', 'SPARK', 'NOSQL', 'SAP', 'ETL', 'API', 'PLSQL', 'MONGODB', 'POSTGRESQL', 'ELASTICSEARCH', 'REDIS', 'MYSQL',
                    'FIREBASE', 'SQLITE', 'CASSANDRA', 'DYNAMODB', 'OLTP', 'OLAP', 'DEVOPS', 'NETWORK', 'APACHE', 'SECURITY', 'MARKDOWN']

# Función para crear WordCloud filtrado
def crear_wordcloud_filtrado(titulo, palabras_interes):
    text = ' '.join(df[df['Job Title'] == titulo]['Job Description'].astype(str))
    palabras_filtradas = re.findall(r'\b(?:' + '|'.join(palabras_interes) + r')\b', text, flags=re.IGNORECASE)

    # Contar la frecuencia de cada palabra
    frecuencias = Counter(palabras_filtradas)

    # Generar el WordCloud con las frecuencias
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(frecuencias)
    
    # Mostrar el WordCloud en Streamlit
    st.subheader(f"WordCloud Filtrado para {titulo}")
    st.image(wordcloud.to_array(), caption=f"WordCloud Filtrado para {titulo}", width=800)

# Aplicación Streamlit
st.title("WordCloud en Streamlit")

# Crear WordCloud para cada título
for titulo in ['Business Analyst', 'Data Analyst', 'Data Engineer', 'Data Scientist']:
    crear_wordcloud_filtrado(titulo, palabras_interes)
