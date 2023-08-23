import speech_recognition as sr     #librería de reconocimiento de voz
import Diccionario as Dcc
import sintetizador as stz
import queue

from text_to_num import alpha2digit #librería para convertir número textual en un número
import re
import time 

def EscucharUsuario():
    r = sr.Recognizer()
    r.dynamic_energy_threshold = True
    r.pause_threshold = 0.8
    time.sleep(0.1)
    print("Te estoy escuchando....." + '\n')
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source=source, duration = 1)
        audio = r.listen(source)
    
    try:
        understand = r.recognize_google(audio, language='es-COL')    #reconoce el audio, lo convierte en texto y lo almacena en understand
        Audioresponse = "entendí " + understand
        print(Audioresponse + '\n')
        return(understand)
        
    except sr.UnknownValueError:
        stz.HablarAlUsuario('No te entendí')
        print("No entendi" + '\n')
        return(EntenderAlUsuario())

    except sr.RequestError as e:
        print("Google Speech Recognition error" + '\n')
        return(0)

def TextoANumero(oracion):
    texto_convertido= alpha2digit(oracion,'es')
    n = [str(n) for n in re.findall(r'-?\d+\.?\d*', texto_convertido)]
    ListaTexto = texto_convertido.split()
    for i in range(len(n)): 
        nstring = n[i]
        nindex = ListaTexto.index(nstring)
        ListaTexto[nindex] = float(n[i])
    return ListaTexto

def EntenderAlUsuario():
    RespuestaUsuario = EscucharUsuario()
    # RespuestaUsuario =  'toma el cubo azul uno y ponlo cinco centímetros a la derecha'
    if RespuestaUsuario != 0:
        RespuestaUsuario = TextoANumero(RespuestaUsuario)
    if comparador(RespuestaUsuario, Dcc.ListaDeSaludos)==True:
        print('Voz tomo el turno')
        return 'hola'
    elif comparador(RespuestaUsuario, Dcc.AprenderTarea)==True:
        return 'Aprender tarea'
    elif comparador(RespuestaUsuario, Dcc.EjecutarTarea)==True:
        return 'Ejecutar tarea'
    elif comparador(RespuestaUsuario, Dcc.ClasificaCubosAzules)==True:
        return 'clasifica cubos azules'
    elif comparador(RespuestaUsuario, Dcc.ClasificaCubosVerdes)==True:
        return 'clasifica cubos verdes'
    elif comparador(RespuestaUsuario,['este cubo'])==True or comparador(RespuestaUsuario,['este culo'])==True or comparador(RespuestaUsuario,['este quo'])==True  :
        return 'este'

    
    else:
        return RespuestaUsuario




def comparador(Frase, diccionario):
    if type(Frase) != int:
        for i in range(len(diccionario)):
            FraseDiccionario = diccionario[i].split()
            if len(list(set(FraseDiccionario) & set(Frase))) == len(FraseDiccionario):
                return True



def IdentificarMovimiento(UserResponse):
    print(UserResponse)
    Output = [0,0,0,0,0,0]
    # UserResponse = TextoANumero(EscucharUsuario())
    for j in range(len(UserResponse)):
        Word = UserResponse[j]
        for i in range(len(Dcc.ListaMovimientos)):  # tipo de movimiento
            if Word in Dcc.ListaMovimientos[i]:
                if i == 0:
                    Output[0] = 1
                elif i == 1:
                    Output[3] = 1
        
        for i in range(len(Dcc.ColorDeObjetos)):  # color del objeto
            if Word in Dcc.ColorDeObjetos[i]:
                if i == 0:
                    Output[1] = 1
                elif i == 1:
                    Output[1] = 2
                elif i == 2:
                    Output[1] = 3
                if UserResponse[(j+1)] == 'uno':
                    Output[2] = 1
                else:
                    Output[2] = int(UserResponse[(j+1)]) # número del cubo
        
        # distancia a nueva posicion
        if Word == 'centímetros' or Word == 'milímetros' or Word == 'centímetro' or Word == 'milímetro' or Word == 'cm' or Word == 'mm': 
            if 'derecha' in UserResponse:
                x = 0
                if UserResponse[(j-1)] == 'un':
                    y = 1
                else:
                    y = UserResponse[(j-1)]
                Coordinates = [x,y]
                Output[4] = Coordinates
            elif 'izquierda' in UserResponse:
                x = 0
                if UserResponse[(j-1)] == 'un':
                    y = -1
                else:
                    y = UserResponse[(j-1)]*(-1)
                Coordinates = [x,y]
                Output[4] = Coordinates
            elif 'abajo' in UserResponse:
                if UserResponse[(j-1)] == 'un':
                    x = 1
                else:
                    x = UserResponse[(j-1)]
                y = 0
                Coordinates = [x,y]
                Output[4] = Coordinates
            elif 'arriba' in UserResponse:
                if UserResponse[(j-1)] == 'un':
                    x = -1
                else:
                    x = UserResponse[(j-1)]*(-1)
                y = 0
                Coordinates = [x,y]
                Output[4] = Coordinates
            # print(Output)

        if Word == 'zona':
            
            Output[5] = int(UserResponse[j+1])
    
    
    print(Output)


    return Output