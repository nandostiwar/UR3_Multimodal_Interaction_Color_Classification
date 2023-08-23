import csv
import os
import random

# Memoria 1: 1 azul 1 verde
ruta1 = str(os.path.dirname(os.path.abspath(__file__)))+'\memoria1.csv'
# Memoria 2: 1 azul 2 verdes
ruta2 = str(os.path.dirname(os.path.abspath(__file__)))+'\memoria2.csv'
# Memoria 3: 1 azul 3 verdes
ruta3 = str(os.path.dirname(os.path.abspath(__file__)))+'\memoria3.csv'
# Memoria 4: 2 azules 1 verde
ruta4 = str(os.path.dirname(os.path.abspath(__file__)))+'\memoria4.csv'
# Memoria 5: 2 azules 2 verdes
ruta5 = str(os.path.dirname(os.path.abspath(__file__)))+'\memoria5.csv'
# Memoria 6: 2 azules 3 verdes
ruta6 = str(os.path.dirname(os.path.abspath(__file__)))+'\memoria6.csv'
# Memoria 7: 3 azules 1 verde
ruta7 = str(os.path.dirname(os.path.abspath(__file__)))+'\memoria7.csv'
# Memoria 8: 3 azules 2 verdes
ruta8 = str(os.path.dirname(os.path.abspath(__file__)))+'\memoria8.csv'
# Memoria 9: 3 azules 3 verdes
ruta9 = str(os.path.dirname(os.path.abspath(__file__)))+'\memoria9.csv'

rutas = [ruta1, ruta2, ruta3, ruta4, ruta5, ruta6, ruta7, ruta8, ruta9]


''' ========================================================= '''
'''  Esta función se utiliza para traer un dato aleatorio de  '''
'''     la memoria correspondiente a la ruta especificada     '''
''' ========================================================= '''
def TraerDatosCSV(ruta):
    try:
        with open(ruta, 'r', newline='') as File:
            reader = csv.reader(File)
            datos = [list(map(int, i)) for i in reader]
            return datos
    except:
        with open(ruta, 'w', newline='') as File:
            writer = csv.writer(File)
            writer.writerow([0,0])
            writer.writerow([0,0])
        with open(ruta, 'r', newline='') as File:
            reader = csv.reader(File)
            datos = [list(map(int, i)) for i in reader]
            return datos
    # with open(ruta, newline='') as File:
    #     reader = csv.reader(File)
    #     data = [line for line in reader]
    # return data


''' ============================================================ '''
'''  Esta función se utiliza para reemplazar un dato especifico  '''
'''   en la ruta e indice especifico por el valor especificado   '''
''' ============================================================ '''
def ReemplazarEnCSV(ruta, indice, valor):
    with open(ruta, newline='') as File:
        reader = csv.reader(File)
        datos = [line for line in reader]
    datos[indice] = valor

    with open(ruta, 'w', newline='') as File:
        writer = csv.writer(File)
        writer.writerows(datos)


''' =========================================================== '''
'''   Esta función se utiliza para agregar dato especifico en   '''
'''   la ruta indicada, sin eliminar la informacion existente   '''
''' =========================================================== '''
def EscribirEnCSV(ruta, dato):
    try:
        with open(ruta, 'r', newline='') as File:
            reader = csv.reader(File)
            datos = [line for line in reader]
    except:
        datos = 0

    with open(ruta, 'w', newline='') as File:
        if datos != 0:
            writer = csv.writer(File)
            writer.writerows(datos)
            writer.writerow(dato)
        else:
            writer = csv.writer(File)
            writer.writerow(dato)
    
    # #Imprimir la memoria
    # with open(ruta, newline='') as File:
    #     reader = csv.reader(File)
    #     print("imprimiendo memoria")
    #     for row in reader:
    #         print(row)


''' ========================================================= '''
'''   Esta función se utiliza para crear las memorias si no   '''
'''   existen y poner la informacion de la memoria en caso    '''
'''                 de no estar configurada                   '''
''' ========================================================= '''
def InicializacionMemorias():
    global ruta1, ruta2, ruta3, ruta4, ruta5, ruta6, ruta7, ruta8, ruta9

    dato = TraerDatosCSV(ruta1)
    if dato[1] != [1,1]:
        ReemplazarEnCSV(ruta1, 0, [0,0])
        ReemplazarEnCSV(ruta1, 1, [1,1])
    
    dato = TraerDatosCSV(ruta2)
    if dato[1] != [1,2]:
        ReemplazarEnCSV(ruta2, 0, [0,0])
        ReemplazarEnCSV(ruta2, 1, [1,2])
    
    dato = TraerDatosCSV(ruta3)
    if dato[1] != [1,3]:
        ReemplazarEnCSV(ruta3, 0, [0,0])
        ReemplazarEnCSV(ruta3, 1, [1,3])
    
    dato = TraerDatosCSV(ruta4)
    if dato[1] != [2,1]:
        ReemplazarEnCSV(ruta4, 0, [0,0])
        ReemplazarEnCSV(ruta4, 1, [2,1])
    
    dato = TraerDatosCSV(ruta5)
    if dato[1] != [2,2]:
        ReemplazarEnCSV(ruta5, 0, [0,0])
        ReemplazarEnCSV(ruta5, 1, [2,2])
    
    dato = TraerDatosCSV(ruta6)
    if dato[1] != [2,3]:
        ReemplazarEnCSV(ruta6, 0, [0,0])
        ReemplazarEnCSV(ruta6, 1, [2,3])
    
    dato = TraerDatosCSV(ruta7)
    if dato[1] != [3,1]:
        ReemplazarEnCSV(ruta7, 0, [0,0])
        ReemplazarEnCSV(ruta7, 1, [3,1])
    
    dato = TraerDatosCSV(ruta8)
    if dato[1] != [3,2]:
        ReemplazarEnCSV(ruta8, 0, [0,0])
        ReemplazarEnCSV(ruta8, 1, [3,2])
    
    dato = TraerDatosCSV(ruta9)
    if dato[1] != [3,3]:
        ReemplazarEnCSV(ruta9, 0, [0,0])
        ReemplazarEnCSV(ruta9, 1, [3,3])


''' ========================================================= '''
'''   Esta función se utiliza para buscar aleatoriamente un   '''
'''                dato en la memoria indicada                '''
''' ========================================================= '''
# Usar en caso de no conocer la ruta
def BuscarEnMemoria(vectorAvV):
    # ejemplo:  vectorAvV = [1,1] 1 azul 1 verde
    global rutas
    for i in rutas:
        datos = TraerDatosCSV(i)
        if datos[1]==vectorAvV:
            try:
                indice = random.randint(2,(len(datos)-1))
                return datos[indice]
            except:
                print("no hay movimientos guardados")
                return(0)

''' ================================================= '''
'''   Esta función se utiliza para ingresar un dato   '''
'''         especifico en la memoria indicada         '''
''' ================================================= '''
# Usar en caso de no conocer la ruta
def EscribirEnMemoria(vectorAvV, dato):
    if vectorAvV == [1,1]:
        EscribirEnCSV(rutas[0], dato)
    elif vectorAvV == [1,2]:
        EscribirEnCSV(rutas[1], dato)
    elif vectorAvV == [1,3]:
        EscribirEnCSV(rutas[2], dato)
    elif vectorAvV == [2,1]:
        EscribirEnCSV(rutas[3], dato)
    elif vectorAvV == [2,2]:
        EscribirEnCSV(rutas[4], dato)
    elif vectorAvV == [2,3]:
        EscribirEnCSV(rutas[5], dato)
    elif vectorAvV == [3,1]:
        EscribirEnCSV(rutas[6], dato)
    elif vectorAvV == [3,2]:
        EscribirEnCSV(rutas[7], dato)
    elif vectorAvV == [3,3]:
        EscribirEnCSV(rutas[8], dato)


InicializacionMemorias()
EscribirEnMemoria([1,1],[1,1,1,0,0,0,0,0,0,2,1,12,0,0,0,0,0,0])
EscribirEnMemoria([1,2],[1,1,1,0,0,0,0,0,0,2,1,12,2,2,4,0,0,0])
EscribirEnMemoria([1,3],[1,1,1,0,0,0,0,0,0,2,1,12,2,2,4,2,3,9])
EscribirEnMemoria([2,1],[1,1,1,1,2,5,0,0,0,2,1,12,0,0,0,0,0,0])
EscribirEnMemoria([2,2],[1,1,1,1,2,5,0,0,0,2,1,12,2,2,4,0,0,0])
EscribirEnMemoria([2,3],[1,1,1,1,2,5,0,0,0,2,1,12,2,2,4,2,3,9])
EscribirEnMemoria([3,1],[1,1,1,1,2,5,1,3,6,2,1,12,0,0,0,0,0,0])
EscribirEnMemoria([3,2],[1,1,1,1,2,5,1,3,6,2,1,12,2,2,4,0,0,0])
EscribirEnMemoria([3,3],[1,1,1,1,2,5,1,3,6,2,1,12,2,2,4,2,3,9])