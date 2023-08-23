import Diccionario as Dcc
import random
import pyttsx3
tts = pyttsx3.init()

tts.setProperty('rate',160)
voices = tts.getProperty('voices')
tts.setProperty('voice',voices[2].id)

def HablarAlUsuario(texto):
    tts.say(texto)
    tts.runAndWait()

def solicitudes(opcion):
    if opcion == 1:
        i = random.randint(0,len(Dcc.PreguntasTareas)-1)
        HablarAlUsuario(Dcc.PreguntasTareas[i])
    elif opcion == 2:
        HablarAlUsuario('¿Qué cubos desea clasificar?')
    else:
        HablarAlUsuario('Error, comando de síntesis de voz no identificado')

def respuestas(opcion):
    if opcion == 1:
        i = random.randint(0,len(Dcc.ListaDeSaludos)-1)
        HablarAlUsuario(Dcc.ListaDeSaludos[i])

    elif opcion == 2:
        HablarAlUsuario('la tarea se ejecutó con éxito')

    elif opcion == 3:
        HablarAlUsuario('Este módulo aún no está disponible')

    elif opcion == 4:
        HablarAlUsuario('Enseñame')
        
    elif opcion == 5:
        HablarAlUsuario('Tarea aprendida')
    elif opcion == 6:
        HablarAlUsuario('La tarea no fue reconocida, por favor repita nuevamente')
    elif opcion == 7:
        HablarAlUsuario('No se han encontrado los cubos, ¿quieres que aprenda una tarea o que la ejecute?') 
    elif opcion == 8:
        HablarAlUsuario('siguiente instrucción ')
    elif opcion == 9:
        HablarAlUsuario('No se ha encontrado una tarea para ejecutar, por favor revise que la cantidad de cubos sea correcta, ¿quieres que aprenda una tarea o que la ejecute?')

    else:
        HablarAlUsuario('Error, comando de síntesis de voz no identificado')



# respuestas(9)
