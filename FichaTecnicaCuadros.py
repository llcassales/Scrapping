from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd

#s = Service('./chromedriver.exe')
#driver = webdriver.Chrome(service=s)
driver = webdriver.Chrome("C:/webdrivers/chromedriver.exe")

def books_info_data(ULR = 'https://www.museodelprado.es/coleccion/obra-de-arte/parte-superior-del-pantocrator-sostenido-por/a331fb54-a6d4-4732-8509-daf462aa92bb?searchid=05175cfe-058d-e702-0902-f3c703461140'):
    driver.get(URL)
    
    # Creamos una lista para cada característica del cuadro
    # imagenes = []       # Lista para almacenar las imágenes de los cuadros
    no_catalogos = []  # Lista para número del catálogo
    autores = []       # Autores de la obra
    titulos = []       # Título de la obra
    fechas = []        # Fecha de la obra
    tecnicas = []      # Técnica empleada para pintar el cuadro
    soportes = []      # Soporte utilizado para el cuadro
    dimensiones_alto = []    # Altura del cuadro (en cm)
    dimensiones_ancho = []   # Anchura del cuadro (en cm)
    series = []        # Serie a la cual pertenece la obra
    procedencias = []  # Origen del cuadro (lugar)
    
    # Leemos el contenido de la página
    content = driver.page_source
    soup = BeautifulSoup(content, features='lxml')
    
    for ficha_tecnica in soup.findAll('div', href=False, attrs={'class':'stick-container'}):
        # Esto es para capturar los dibujos; habrá que usar RegEx para sacar los enlaces de cada cuadro
        # dibujo = ficha_tecnica.find('img', attrs={'src', "https://content3.cdnprado.net/imagenes/Documentos/imgsem/a3/a331/a331fb54-a6d4-4732-8509-daf462aa92bb/dd5afc00-81d5-4e84-aca4-5377a4722391_832.jpg"})
        no_catalogo = ficha_tecnica.find('span', attrs={'property': 'cidoc:p102_has_title'})
        autor = ficha_tecnica.find('span', attrs={'property': 'ecidoc:p131_E82_p102_has_title'})
        titulo = ficha_tecnica.find('em')
        fecha = ficha_tecnica.find('dd', attrs={'property': 'date:textDate'})
        tecnica = ficha_tecnica.find('span', attrs={'rel': 'ecidoc:p108i_E12_p32_used_general_technique'})
        soporte = ficha_tecnica.find('span', attrs={'rel': 'ecidoc:p108i_E12_p126_employed_support'})
        dimension_alto = ficha_tecnica.find('span', attrs={'about': 'http://museodelprado.es/items/E54_Dimension_a331fb54-a6d4-4732-8509-daf462aa92bb_1ab6dc9e-3dde-478c-8553-0bcd7a5d47d5'})
        dimension_ancho = ficha_tecnica.find('span', attrs={'about': 'http://museodelprado.es/items/E54_Dimension_a331fb54-a6d4-4732-8509-daf462aa92bb_f674f619-fe5a-4284-9451-86255ff24af0'})
        serie = ficha_tecnica.find('dd', attrs={'property': 'ecidoc:p46i_E78_p102_forms_part_of'})
        procedencia = ficha_tecnica.find('dd', attrs={'property': 'cidoc:p27_moved_from'})
    
        # Ahora añadimos la información a las listas
        no_catalogos.append(no_catalogo.text)
        autores.append(autor.text)
        titulos.append(titulo.text)
        fechas.append(fecha.text)
        tecnicas.append(tecnica.text)
        soportes.append(soporte.text)
        dimensiones_alto.append(dimension_alto.text)
        dimensiones_ancho.append(dimension_ancho.text)
        series.append(serie.text)
        procedencias.append(procedencia.text)
    
    
    df = pd.DataFrame({'Número catálogo':no_catalogos, 'Autor': autores, 'Título de la obra': titulos,
                       'Fecha obra': fechas, 'Técnica empleada': tecnicas, 'Soporte de la obra': soportes,
                       'Altura obra (en cm)': dimensiones_alto, 'Anchura obra (en cm)': dimensiones_ancho,
                       'Serie de la cual forma parte la obra': series, 'Lugar de procedencia': procedencias})
    df.to_csv('Ficha Tecnica.csv', index=False, encoding='latin1')


