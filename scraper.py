from selenium import webdriver
from selenium.webdriver.common.by import By

    
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path='chromedriver_linux64/chromedriver', options=options)

def abrirWebdriver(url):    
    driver.get(url) 
        
        
def click(xpath):
    boton = driver.find_element(By.XPATH,xpath)
    boton.click


def encotrarElemento(xpath):
    elemnto = driver.find_element(By.XPATH,xpath)

    return elemnto


def encotrarElementos(xpath):
    elemntos = driver.find_elements(By.XPATH,xpath)

    return elemntos
    