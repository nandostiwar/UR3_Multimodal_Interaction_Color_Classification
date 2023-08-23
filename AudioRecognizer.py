from ast import Return
from asyncio.windows_events import NULL
from cgitb import text
import speech_recognition as sr     #librería de reconocimiento de voz
import WordsDictionary as wd
from os import path
import pyttsx3                      #librería de habla
import random
tts = pyttsx3.init()

from text_to_num import alpha2digit #librería para convertir número textual en un número
import re

###################################################################################################
########################################  TEXT TO SPEECH  #########################################
###################################################################################################

def Understand2User():
    Output = [0,0,0,0,0,0,0]
    #Posición 5:  Hola
    #Posición 6: Cubo a clasificar --> 0=Nada 1=Azul 2=Verde 3=Amarillo
    #texto = Text2Number("toma el cubo azul uno y ponlo un centímetro hacia arriba")
    #UserResponse = texto
    #print(texto)
    UserResponse = Text2Number(Listen2User())
    for j in range(len(UserResponse)):
        Word = UserResponse[j]
        for i in range(len(wd.MovementList)):  # tipo de movimiento
            if Word in wd.MovementList[i]:
                if i == 0:
                    Output[0] = 1
                elif i == 1:
                    Output[3] = 1
        
        for i in range(len(wd.ObjectColor)):  # color del objeto
            if Word in wd.ObjectColor[i]:
                if i == 0:
                    Output[1] = 1
                elif i == 1:
                    Output[1] = 2
                elif i == 2:
                    Output[1] = 3
                if (j+1) < len(UserResponse):
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
        
        #Detecta si hay un saludo
        if Word in wd.GreetingsList:
            Output[5] = 1

        #detecta si hay una labor de clasificación
        if Word=='clasifique' or Word=='clasificar' or Word=='clasifica':
            for k in range(j, len(UserResponse)):
                Word2 = UserResponse[k]   #esta variable guarda progresivamente las palabras despues de que detecta la palabra "clasifique"
                for i in range(len(wd.ObjectColor)):  # en este punto compara las palabras siguientes a "clasifique" con el diccionario
                    if Word2 in wd.ObjectColor[i]:    # para encontrar qué color se desea clasificar
                        if i == 0:
                            Output[6] = 1
                            Output[0] = Output[1] = Output[2] = Output[3] = Output[4] = 0
                        elif i == 1:
                            Output[6] = 2
                            Output[0] = Output[1] = Output[2] = Output[3] = Output[4] = 0
                        elif i == 2:
                            Output[6] = 3
                            Output[0] = Output[1] = Output[2] = Output[3] = Output[4] = 0

    return Output


def Listen2User():
    r = sr.Recognizer()
    r.dynamic_energy_threshold = True
    r.pause_threshold = 0.8
    print("Espera un momento..." + '\n')
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source=source, duration = 1)
        Speak2User('Hola, en que te puedo ayudar?')
        audio = r.listen(source)
    
    try:
        understand = r.recognize_google(audio, language='es-COL')    #reconoce el audio, lo convierte en texto y lo almacena en understand
        Audioresponse = "entendí " + understand
        print(Audioresponse + '\n')
        return(understand)
        
    except sr.UnknownValueError:
        print("No entendi" + '\n')
        return(0)

    except sr.RequestError as e:
        print("Google Speech Recognition error" + '\n')
        return(0)

def Text2Number(sentence):
    text_convert= alpha2digit(sentence,'es')
    n = [str(n) for n in re.findall(r'-?\d+\.?\d*', text_convert)]
    text_array = text_convert.split()
    for i in range(len(n)):
        nstring = n[i]
        nindex = text_array.index(nstring)
        text_array[nindex] = float(n[i])
    return text_array

###################################################################################################
########################################  SINTESIS DE VOZ  ########################################
###################################################################################################

def Speak2User(texto):
    tts.say(texto)
    tts.runAndWait()

def Greeting2User(señal):   # para ejecutar el saludo se llama esta función, 
    if señal == 1:          # pero es necesario poner ya sea un 1 o se puede poner directamente Output[5] en la entrada
        i = random.randint(0,13)
        Speak2User(wd.GreetingsList[i])
