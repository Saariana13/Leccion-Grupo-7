import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup


def cambiar_caracter(texto):
    return texto.replace('Ñ', 'N')


navegador = webdriver.Chrome()
navegador.get('https://datosmacro.expansion.com/pib/ecuador')


html_pagina = navegador.page_source
analizador = BeautifulSoup(html_pagina, 'html.parser')


tabla_datos = analizador.find('table')

lista_anios = []
lista_pib_dolares = []
lista_variacion = []


if tabla_datos:
    filas_tabla = tabla_datos.find_all('tr')
    for fila in filas_tabla[1:]:
        celdas = fila.find_all('td')
        lista_anios.append(cambiar_caracter(celdas[0].text.strip()))
        lista_pib_dolares.append(cambiar_caracter(celdas[2].text.strip()))
        lista_variacion.append(cambiar_caracter(celdas[3].text.strip()))


dataframe_pib = pd.DataFrame({
    'FECHA': lista_anios,
    'PIB ANUAL': lista_pib_dolares,
    'VAR_PIB': lista_variacion
})


dataframe_pib.to_csv('datos_pib_ecuador.csv', index=False, encoding='utf-8-sig')
navegador.quit()

print(dataframe_pib)

#Integrantes
#Fruto Borbor Melanie
#Pila Montero Génesis
#Ramírez Ancgundia Gabriela
#Sánchez Anzoátegui Ariana