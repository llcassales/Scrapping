import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#s = Service('https://github.com/llcassales/Scrapping.git')
driver = webdriver.Chrome("C:/webdrivers/chromedriver.exe")

# Especificamos la web en la cual queremos hacer web scraping
driver.get('https://www.museodelprado.es/coleccion/obras-de-arte')

# Con la siguiente línea le decimos al código que haga "scroll" hasta el final de la página
# Es decir, cargará todos los cuadros que hay en la página
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
# # Todos los cuadros en una lista
# # Al usar el argumento find_elementS, en plural, nos originará una lista con todos los elementos
# # AVISO: el argumento .find_elements_by_xpath está obsoleto, usar en su lugar .find_elements()
# cuadros = driver.find_elements(by=By.XPATH, value="//figure") # Almacenará todos los elementos dentro de <figure>...</figure>
#
# for cuadro in cuadros:
#     # Buscamos dentro de la variable auxiliar "cuadro", que solo contiene los elementos que nos interesan
#     imagen = cuadro.find_element(by=By.XPATH, value=".//img[@src]") # Ponemos un punto delante para que busque dentro de //figure
#     print(imagen)
#
#     titulo = cuadro.find_element(by=By.XPATH, value=".//dt").text
#     print(titulo)
#
#     soporte = cuadro.find_element(by=By.XPATH, value='.//dd[@class="soporte"]').text
#     print(soporte)
#
#     autor = cuadro.find_element(by=By.XPATH, value=".//dd[@class='autor']").text
#     print(autor)
#
#     resumen = cuadro.find_element(by=By.XPATH, value='.//p').text
#     print(resumen)