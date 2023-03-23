import scraper
import manejoDato
from manejoDato import EliminarCaracter
import time
from selenium import webdriver
import pandas

#from selenium.webdriver.common.keys import Keys


url ='https://www.resultados-futbol.com/partido/Huddersfield-Town-Fc/Arsenal/2018'
characters = "%"
listDatos = {}


def datosPartido(url):    
    try:
        '''scraper.abrirWebdriver(url)

        xpath = '//button[@class=" css-kv701e"]/span'
        scraper.click(xpath)'''

        xpath = '//td[@class="equipo1"]/a/b'
        local = scraper.encotrarElemento(xpath).text    
    
        xpath = '//td[@class="equipo2"]/a/b'
        visitante = scraper.encotrarElemento(xpath).text    

        xpath = '//ul[@id="crumbs"]/li[2]/a'
        ligaTemporada =  scraper.encotrarElemento(xpath).text

        liga = ligaTemporada[0:len(ligaTemporada)-5]

        temporada = int(ligaTemporada[len(ligaTemporada)-4:len(ligaTemporada)])


        xpath = '//div[@id="marcador"]//a'
        jornada = scraper.encotrarElemento(xpath).text 
        caracter = " "
        modificar = EliminarCaracter(jornada,caracter)
        jornada=modificar.eliminarCara()

        xpath = '//div[@id="box-tabla"]//tr'
        estaPartido = scraper.encotrarElementos(xpath)

        #LOCAL

        xpath = '//div[@id="tab_match_teams"]//small[1]'
        aliniacionL = scraper.encotrarElemento(xpath).text 
        caracter = " "
        modificar = EliminarCaracter(aliniacionL,caracter)
        aliniacionL=modificar.eliminarCara()

        xpath = '//div[@class="header-team-1"]//div[@class="team-stats rank-pos"]'
        posicionL = scraper.encotrarElemento(xpath).text 
        caracter = " º"
        modificar = EliminarCaracter(posicionL,caracter)
        posicionL=int( modificar.eliminarCara())

        xpath = '//div[@id="marcador"]//div[@class="team-stats pts-elo"]'
        ptsEloL = scraper.encotrarElemento(xpath).text 
        caracter = " Pts. Elo"
        modificar = EliminarCaracter(ptsEloL,caracter)
        ptsEloL= int (modificar.eliminarCara())

        #VISITANTE
        
        xpath = '//div[@id="tab_match_teams"]/div[@class="team team2"]//small'
        aliniacionV = scraper.encotrarElemento(xpath).text 
        caracter = " "
        modificar = EliminarCaracter(aliniacionV,caracter)
        aliniacionV=modificar.eliminarCara()

        xpath = '//div[@class="header-team-2"]//div[@class="team-stats rank-pos"]'
        posicionV = scraper.encotrarElemento(xpath).text 
        caracter = " º"
        modificar = EliminarCaracter(posicionV,caracter)
        posicionV=modificar.eliminarCara()
        
        xpath = '//div[@class="header-team-2"]//div[1]'
        ptsEloV = scraper.encotrarElemento(xpath).text 
        caracter = " Pts. Elo"
        modificar = EliminarCaracter(ptsEloV,caracter)
        ptsEloV= int(modificar.eliminarCara())

        diccPagina = {
            'liga':liga,
            'temporada':temporada,
            'fecha':jornada,
            'local':local,
            'visitante':visitante,
            'L-aliniacion':aliniacionL,
            'L-posicion':posicionL,
            'L-pts-elo':ptsEloL, 
            'V-aliniacion':aliniacionV,
            'V-posicion':posicionV,
            'V-pts-elo':ptsEloV
        }
        
        
        for datoPartido in estaPartido:   

            text = datoPartido.text

            for x in range(len(characters)):
                text = text.replace(characters[x],"")
    
            tipoEstadistica = text[2:len(text)-2]
            tipoEstadistica = tipoEstadistica.strip()

            datoLocal = text[0:2]
            datoLocal =  datoLocal.strip()

            datoVisita = text[len(text)-2:len(text):]
            datoVisita = datoVisita.strip()

            diccPagina['L-'+str(tipoEstadistica)]= datoLocal
            diccPagina['V-'+str(tipoEstadistica)]=datoVisita

        listaDatos = manejoDato.compararDiccionarios(diccPagina)
        return manejoDato.nuevoRegistro(listaDatos)
    except:
        print('No hay datos estadisticos de partido')
    

    #print(listaDatos)


def partidos_x_jornada(url):
    # ----->
    #url = 'https://www.resultados-futbol.com/premier2021/grupo1/jornada7'
    #jornada= url[len(url)-8:len(url)]

    listUrlPartidos=[]
    
    try:
        scraper.abrirWebdriver(url)
        xpath = '//button[@class=" css-kv701e"]/span'
        scraper.click(xpath) 

        xpath='//table[@id="tabla1"]//td[@class="rstd"]/a'
        partidos=scraper.encotrarElementos(xpath)

    

        for i in partidos:
            url = i.get_attribute('href')
            listUrlPartidos.append(url)

        for url in listUrlPartidos:
            scraper.abrirWebdriver(url)

            '''xpath = '//ul[@id="crumbs"]/li[2]/a'
            ligaTemporada =  scraper.encotrarElemento(xpath).text'''



            xpath = '//button[@class=" css-kv701e"]/span'
            scraper.click(xpath)    
            #time.sleep(4)
            dato =datosPartido(url)

        #dato.to_csv('csv/'+ligaTemporada+' '+jornada+'.csv')

        return dato
    except:
        print('No abrio la pagina')

def jornadas_x_temporad():
    listaUrlJornadas = []
    scraper.abrirWebdriver("https://www.resultados-futbol.com/premier2022")
    xpath = '//button[@class=" css-kv701e"]/span'
    scraper.click(xpath) 

    #Click en selector de jornada
    xpath = '//div[@id="col-resultados"]//div[@class="right journey-simple"]/div[@class="j_cur"]/a'
    scraper.click(xpath)


    xpath='//div[@id="desplega_jornadas"]/ul/li/a'
    jornadas=scraper.encotrarElementos(xpath)
    cont = 0
    for i in jornadas:
        url = i.get_attribute('href')
        listaUrlJornadas.append(url)
        cont = cont + 1
        if cont == 42:
            print(cont)
            break
    
    for url in listaUrlJornadas:
        print (url)
        #time.sleep(4)
        dato=partidos_x_jornada(url)

    print(dato)
    dato.to_csv('csv/par3.csv')
