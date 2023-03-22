import pandas as pd
import store

diccBase ={
        'liga':[],
        'temporada':[],
        'fecha':[],
        'local':[],  
        'visitante':[], 
        'L-aliniacion':[],
        'L-posicion':[],
        'L-pts-elo':[], 
        'V-aliniacion':[],
        'V-posicion':[],
        'V-pts-elo':[],            
        'L-Posesión del balón':[],
        'L-Goles':[],
        'L-Tiros a puerta':[],
        'L-Tiros fuera':[],
        'L-Total tiros':[],
        'L-Paradas del portero':[],
        'L-Saques de esquina':[],
        'L-Fueras de juego':[],
        'L-Tarjetas Rojas':[],
        'L-Asistencias':[],
        'L-Sustituciones':[],
        'L-Faltas':[],
        'L-Tarjetas Amarillas':[],
        'L-Lesiones':[],
        'L-Tiros al palo':[],
        'L-Penalti cometido':[],
        'V-Posesión del balón':[],
        'V-Goles':[],
        'V-Tiros a puerta':[],
        'V-Tiros fuera':[],
        'V-Total tiros':[],
        'V-Paradas del portero':[],
        'V-Saques de esquina':[],
        'V-Fueras de juego':[],
        'V-Tarjetas Rojas':[],
        'V-Asistencias':[],
        'V-Sustituciones':[],
        'V-Faltas':[],
        'V-Tarjetas Amarillas':[],
        'V-Lesiones':[],
        'V-Tiros al palo':[],
        'V-Penalti cometido':[]
}

listaIndex = [
        'liga',
        'temporada',
        'fecha',
        'local',  
        'visitante', 
        'L-aliniacion',
        'L-posicion',
        'L-pts-elo', 
        'V-aliniacion',
        'V-posicion',
        'V-pts-elo',            
        'L-Posesión del balón',
        'L-Goles',
        'L-Tiros a puerta',
        'L-Tiros fuera',
        'L-Total tiros',
        'L-Paradas del portero',
        'L-Saques de esquina',
        'L-Fueras de juego',
        'L-Tarjetas Rojas',
        'L-Asistencias',
        'L-Sustituciones',
        'L-Faltas',
        'L-Tarjetas Amarillas',
        'L-Lesiones',
        'L-Tiros al palo',
        'L-Penalti cometido',
        'V-Posesión del balón',
        'V-Goles',
        'V-Tiros a puerta',
        'V-Tiros fuera',
        'V-Total tiros',
        'V-Paradas del portero',
        'V-Saques de esquina',
        'V-Fueras de juego',
        'V-Tarjetas Rojas',
        'V-Asistencias',
        'V-Sustituciones',
        'V-Faltas',
        'V-Tarjetas Amarillas',
        'V-Lesiones',
        'V-Tiros al palo',
        'V-Penalti cometido'
        ]
pd_datoEstadisticos = pd.DataFrame(data=diccBase) 

def nuevoRegistro(listaDatosEsta):
    global pd_datoEstadisticos
    s = pd.Series(listaDatosEsta,index=listaIndex)
   
    pd_datoEstadisticos = pd_datoEstadisticos.append(s,ignore_index=True)
    
    return pd_datoEstadisticos

def eliminarPorciento(text):
    characters = "%"
    for x in range(len(characters)):
        text = text.replace(characters[x],"")


def compararDiccionarios(diccPagina):
    listaRegistro = []

    for d1 in diccBase.keys():
        encontro = False
        for d2 in diccPagina.keys():
            if d1==d2:
                listaRegistro.append(diccPagina[str(d2)])
                encontro = True
                break
        if encontro == False:    
            listaRegistro.append(0)
    
    return listaRegistro


class EliminarCaracter:
    def __init__(self,texto,caracter):
        self.texto = texto
        self.caracter = caracter


    def eliminarCara(self):
        
        for x in range(len(self.caracter)):
            self.texto = str(self.texto).replace(self.caracter[x],"")
        
        return self.texto

