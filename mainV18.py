import sintetizador as stz
import VISIONV15 as V2
import reconocedor as rcd
import time 
import threading
import movimientos as mv
import ComandosMemEpis as cme

def zonasCoordenadas(zona,objetos):
    if zona == 1:
        desplazamientoX = V2.coordenadasZona1[0][0]
        desplazamientoY = V2.coordenadasZona1[0][1]
        desplazamientoX = desplazamientoX - objetos[0]
        desplazamientoY = desplazamientoY - objetos[1]
    elif zona == 2:
        desplazamientoX = V2.coordenadasZona2[0][0]
        desplazamientoY = V2.coordenadasZona2[0][1]
        desplazamientoX = desplazamientoX - objetos[0]
        desplazamientoY = desplazamientoY - objetos[1]
    elif zona == 3:
        desplazamientoX = V2.coordenadasZona3[0][0]
        desplazamientoY = V2.coordenadasZona3[0][1]
        desplazamientoX = desplazamientoX - objetos[0]
        desplazamientoY = desplazamientoY - objetos[1]
    elif zona == 4:
        desplazamientoX = V2.coordenadasZona4[0][0]
        desplazamientoY = V2.coordenadasZona4[0][1]
        desplazamientoX = desplazamientoX - objetos[0]
        desplazamientoY = desplazamientoY - objetos[1]
    elif zona == 5:
        desplazamientoX = V2.coordenadasZona5[0][0]
        desplazamientoY = V2.coordenadasZona5[0][1]
        desplazamientoX = desplazamientoX - objetos[0]
        desplazamientoY = desplazamientoY - objetos[1]
    elif zona == 6:
        desplazamientoX = V2.coordenadasZona6[0][0]
        desplazamientoY = V2.coordenadasZona6[0][1]
        desplazamientoX = desplazamientoX - objetos[0]
        desplazamientoY = desplazamientoY - objetos[1]
    elif zona == 7:
        desplazamientoX = V2.coordenadasZona7[0][0]
        desplazamientoY = V2.coordenadasZona7[0][1]
        desplazamientoX = desplazamientoX - objetos[0]
        desplazamientoY = desplazamientoY - objetos[1]
    elif zona == 8:
        desplazamientoX = V2.coordenadasZona8[0][0]
        desplazamientoY = V2.coordenadasZona8[0][1]
        desplazamientoX = desplazamientoX - objetos[0]
        desplazamientoY = desplazamientoY - objetos[1]
    elif zona == 9:
        desplazamientoX = V2.coordenadasZona9[0][0]
        desplazamientoY = V2.coordenadasZona9[0][1]
        desplazamientoX = desplazamientoX - objetos[0]
        desplazamientoY = desplazamientoY - objetos[1]
    elif zona == 10:
        desplazamientoX = V2.coordenadasZona10[0][0]
        desplazamientoY = V2.coordenadasZona10[0][1]
        desplazamientoX = desplazamientoX - objetos[0]
        desplazamientoY = desplazamientoY - objetos[1]
    elif zona == 11:
        desplazamientoX = V2.coordenadasZona11[0][0]
        desplazamientoY = V2.coordenadasZona11[0][1]
        desplazamientoX = desplazamientoX - objetos[0]
        desplazamientoY = desplazamientoY - objetos[1]
    elif zona == 12:
        desplazamientoX = V2.coordenadasZona12[0][0]
        desplazamientoY = V2.coordenadasZona12[0][1]
        desplazamientoX = desplazamientoX - objetos[0]
        desplazamientoY = desplazamientoY - objetos[1]
    
    mv.desplazar(objetos,desplazamientoY,desplazamientoX)
    V2.señalCambio[0]=1
    V2.ZonasGuardadasAzules = V2.cambioPosicion(V2.zonaCubosAzules,V2.zonasActualesAzules,V2.ZonasGuardadasAzules)
    V2.señalCambio[0]=1
    V2.ZonasGuardadasVerdes = V2.cambioPosicion(V2.zonaCubosVerdes,V2.zonasActualesVerdes,V2.ZonasGuardadasVerdes)
    V2.correctorCoordenadas(V2.coordenadas_actualesAzules,V2.coordenadasObjetosAzules,V2.ZonasGuardadasAzules,V2.objetos_azules)
    V2.correctorCoordenadas(V2.coordenadas_actualesVerdes,V2.coordenadasObjetosVerdes,V2.ZonasGuardadasVerdes,V2.objetos_verdes)



def menProcedural(vectorRecuerdo,vectorZonaActualAzul,voctorZonaActualVerde):

    zonasTotales = [1,2,3,4,5,6,7,8,9,10,11,12]
    ZonasTotalesOcupadas =[vectorRecuerdo[2],vectorRecuerdo[5],vectorRecuerdo[8],vectorRecuerdo[11],vectorRecuerdo[14],vectorRecuerdo[17]]
    ZonasTotalesOcupadas = ZonasTotalesOcupadas + vectorZonaActualAzul + voctorZonaActualVerde
    print(ZonasTotalesOcupadas)
    zonasDisponiblesLista = []
    for zonasDisponibles in zonasTotales:
        if zonasDisponibles in  ZonasTotalesOcupadas:
            print('la zona esta ocupada')
        else:
            zonasDisponiblesLista.append(zonasDisponibles)
    print(f'Estas zonas estan libres {zonasDisponiblesLista}')

    vectorRecuerdoAzul = vectorRecuerdo[0:int(len(vectorRecuerdo)/2)]
    vectorRecuerdoVerde = vectorRecuerdo[int(len(vectorRecuerdo)/2):int(len(vectorRecuerdo))]
    print('vector de informacion azul',vectorRecuerdoAzul)
    print('vector de informacion verde',vectorRecuerdoVerde)
    print('')
    contador = 2
    #Para el color azul
    while vectorRecuerdoAzul[contador] != 0 and contador < 8:
        elemento = vectorRecuerdoAzul[contador]
        if elemento in vectorZonaActualAzul:
            indice = contador-3
            if indice == -1:
                indice = 1
            print(f'En mi memoria el cubo Azul {indice} ocupa la zona {elemento}\n')
            indiceDelCuboActual = vectorZonaActualAzul.index(elemento)+1
            if indiceDelCuboActual !=  indice:
                print('los indices de los cubos no coinciden\n')
                print(f'el cubo Azul {indiceDelCuboActual} esta ocupando la posicion del cubo Azul {indice}\n')
                objetos = V2.objetos_azules[indiceDelCuboActual-1]
                zonaDespejar = zonasDisponiblesLista.pop()

                if zonaDespejar != 0:
                    if zonaDespejar == 1:
                        desplazamientoX = V2.coordenadasZona1[0][0]
                        desplazamientoY = V2.coordenadasZona1[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 2:
                        desplazamientoX = V2.coordenadasZona2[0][0]
                        desplazamientoY = V2.coordenadasZona2[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 3:
                        desplazamientoX = V2.coordenadasZona3[0][0]
                        desplazamientoY = V2.coordenadasZona3[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 4:
                        desplazamientoX = V2.coordenadasZona4[0][0]
                        desplazamientoY = V2.coordenadasZona4[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 5:
                        desplazamientoX = V2.coordenadasZona5[0][0]
                        desplazamientoY = V2.coordenadasZona5[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 6:
                        desplazamientoX = V2.coordenadasZona6[0][0]
                        desplazamientoY = V2.coordenadasZona6[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 7:
                        desplazamientoX = V2.coordenadasZona7[0][0]
                        desplazamientoY = V2.coordenadasZona7[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 8:
                        desplazamientoX = V2.coordenadasZona8[0][0]
                        desplazamientoY = V2.coordenadasZona8[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 9:
                        desplazamientoX = V2.coordenadasZona9[0][0]
                        desplazamientoY = V2.coordenadasZona9[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 10:
                        desplazamientoX = V2.coordenadasZona10[0][0]
                        desplazamientoY = V2.coordenadasZona10[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 11:
                        desplazamientoX = V2.coordenadasZona11[0][0]
                        desplazamientoY = V2.coordenadasZona11[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 12:
                        desplazamientoX = V2.coordenadasZona12[0][0]
                        desplazamientoY = V2.coordenadasZona12[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                
                mv.desplazar(objetos,desplazamientoY,desplazamientoX)
                V2.señalCambio[0]=1
                V2.ZonasGuardadasAzules = V2.cambioPosicion(V2.zonaCubosAzules,V2.zonasActualesAzules,V2.ZonasGuardadasAzules)
                V2.señalCambio[0]=1
                V2.ZonasGuardadasVerdes = V2.cambioPosicion(V2.zonaCubosVerdes,V2.zonasActualesVerdes,V2.ZonasGuardadasVerdes)
                V2.correctorCoordenadas(V2.coordenadas_actualesAzules,V2.coordenadasObjetosAzules,V2.ZonasGuardadasAzules,V2.objetos_azules)
                V2.correctorCoordenadas(V2.coordenadas_actualesVerdes,V2.coordenadasObjetosVerdes,V2.ZonasGuardadasVerdes,V2.objetos_verdes)
                print('El cubo se cambio de posicion para evitar coliciones')
                contador = contador+3
            elif indiceDelCuboActual ==  indice:
                print(f'el cubo Azul {indiceDelCuboActual} esta bien colocado\n')
                contador = contador+3

        elif elemento in voctorZonaActualVerde:
            indice = contador-3
            indiceDelCuboActual = voctorZonaActualVerde.index(elemento)+1
            if indice == -1:
                indice = 1
            print('la zona verde guardada coincide con la zona en el vector AZUL en el indide ', indice)
            print('')
            objetos = V2.objetos_verdes[indiceDelCuboActual-1]
            zonaDespejar = zonasDisponiblesLista.pop()

            if zonaDespejar != 0:
                if zonaDespejar == 1:
                    desplazamientoX = V2.coordenadasZona1[0][0]
                    desplazamientoY = V2.coordenadasZona1[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 2:
                    desplazamientoX = V2.coordenadasZona2[0][0]
                    desplazamientoY = V2.coordenadasZona2[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 3:
                    desplazamientoX = V2.coordenadasZona3[0][0]
                    desplazamientoY = V2.coordenadasZona3[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 4:
                    desplazamientoX = V2.coordenadasZona4[0][0]
                    desplazamientoY = V2.coordenadasZona4[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 5:
                    desplazamientoX = V2.coordenadasZona5[0][0]
                    desplazamientoY = V2.coordenadasZona5[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 6:
                    desplazamientoX = V2.coordenadasZona6[0][0]
                    desplazamientoY = V2.coordenadasZona6[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 7:
                    desplazamientoX = V2.coordenadasZona7[0][0]
                    desplazamientoY = V2.coordenadasZona7[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 8:
                    desplazamientoX = V2.coordenadasZona8[0][0]
                    desplazamientoY = V2.coordenadasZona8[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 9:
                    desplazamientoX = V2.coordenadasZona9[0][0]
                    desplazamientoY = V2.coordenadasZona9[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 10:
                    desplazamientoX = V2.coordenadasZona10[0][0]
                    desplazamientoY = V2.coordenadasZona10[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 11:
                    desplazamientoX = V2.coordenadasZona11[0][0]
                    desplazamientoY = V2.coordenadasZona11[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 12:
                    desplazamientoX = V2.coordenadasZona12[0][0]
                    desplazamientoY = V2.coordenadasZona12[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
            
            mv.desplazar(objetos,desplazamientoY,desplazamientoX)
            V2.señalCambio[0]=1
            V2.ZonasGuardadasAzules = V2.cambioPosicion(V2.zonaCubosAzules,V2.zonasActualesAzules,V2.ZonasGuardadasAzules)
            V2.señalCambio[0]=1
            V2.ZonasGuardadasVerdes = V2.cambioPosicion(V2.zonaCubosVerdes,V2.zonasActualesVerdes,V2.ZonasGuardadasVerdes)
            V2.correctorCoordenadas(V2.coordenadas_actualesAzules,V2.coordenadasObjetosAzules,V2.ZonasGuardadasAzules,V2.objetos_azules)
            V2.correctorCoordenadas(V2.coordenadas_actualesVerdes,V2.coordenadasObjetosVerdes,V2.ZonasGuardadasVerdes,V2.objetos_verdes)
            print('El cubo Azul se cambio de posicion para evitar coliciones con el cubo Verde')
            contador = contador+3
        else:
            contador = contador+3

    #Para el color verde
    contador = 2
    while vectorRecuerdoVerde[contador] != 0 and contador < 8:
        elemento = vectorRecuerdoVerde[contador]
        if elemento in vectorZonaActualAzul:
            indice = contador-3
            if indice == -1:
                indice = 1
            print('la zona verde guardada coincide con la zona en el vector AZUL en el indide ', indice)
            print('')
            indiceDelCuboActual = vectorZonaActualAzul.index(elemento)+1
            objetos = V2.objetos_azules[indiceDelCuboActual-1]
            zonaDespejar = zonasDisponiblesLista.pop()

            if zonaDespejar != 0:
                if zonaDespejar == 1:
                    desplazamientoX = V2.coordenadasZona1[0][0]
                    desplazamientoY = V2.coordenadasZona1[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 2:
                    desplazamientoX = V2.coordenadasZona2[0][0]
                    desplazamientoY = V2.coordenadasZona2[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 3:
                    desplazamientoX = V2.coordenadasZona3[0][0]
                    desplazamientoY = V2.coordenadasZona3[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 4:
                    desplazamientoX = V2.coordenadasZona4[0][0]
                    desplazamientoY = V2.coordenadasZona4[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 5:
                    desplazamientoX = V2.coordenadasZona5[0][0]
                    desplazamientoY = V2.coordenadasZona5[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 6:
                    desplazamientoX = V2.coordenadasZona6[0][0]
                    desplazamientoY = V2.coordenadasZona6[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 7:
                    desplazamientoX = V2.coordenadasZona7[0][0]
                    desplazamientoY = V2.coordenadasZona7[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 8:
                    desplazamientoX = V2.coordenadasZona8[0][0]
                    desplazamientoY = V2.coordenadasZona8[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 9:
                    desplazamientoX = V2.coordenadasZona9[0][0]
                    desplazamientoY = V2.coordenadasZona9[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 10:
                    desplazamientoX = V2.coordenadasZona10[0][0]
                    desplazamientoY = V2.coordenadasZona10[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 11:
                    desplazamientoX = V2.coordenadasZona11[0][0]
                    desplazamientoY = V2.coordenadasZona11[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
                elif zonaDespejar == 12:
                    desplazamientoX = V2.coordenadasZona12[0][0]
                    desplazamientoY = V2.coordenadasZona12[0][1]
                    desplazamientoX = desplazamientoX - objetos[0]
                    desplazamientoY = desplazamientoY - objetos[1]
            
            mv.desplazar(objetos,desplazamientoY,desplazamientoX)
            V2.señalCambio[0]=1
            V2.ZonasGuardadasAzules = V2.cambioPosicion(V2.zonaCubosAzules,V2.zonasActualesAzules,V2.ZonasGuardadasAzules)
            V2.señalCambio[0]=1
            V2.ZonasGuardadasVerdes = V2.cambioPosicion(V2.zonaCubosVerdes,V2.zonasActualesVerdes,V2.ZonasGuardadasVerdes)
            V2.correctorCoordenadas(V2.coordenadas_actualesAzules,V2.coordenadasObjetosAzules,V2.ZonasGuardadasAzules,V2.objetos_azules)
            V2.correctorCoordenadas(V2.coordenadas_actualesVerdes,V2.coordenadasObjetosVerdes,V2.ZonasGuardadasVerdes,V2.objetos_verdes)
            print('El cubo Azul se cambio de posicion para evitar coliciones con el cubo Verde')
            contador = contador+3
        elif elemento in voctorZonaActualVerde:
            indice = contador-3
            if indice == -1:
                indice = 1
            print(f'En mi memoria el cubo verde {indice} ocupa la zona {elemento}\n')
            indiceDelCuboActual = voctorZonaActualVerde.index(elemento)+1
            if indiceDelCuboActual !=  indice:
                print('los indices de los cubos no coinciden\n')
                print(f'el cubo verde {indiceDelCuboActual} esta ocupando la posicion del cubo Azul {indice}\n')
                objetos = V2.objetos_verdes[indiceDelCuboActual-1]
                zonaDespejar = zonasDisponiblesLista.pop()

                if zonaDespejar != 0:
                    if zonaDespejar == 1:
                        desplazamientoX = V2.coordenadasZona1[0][0]
                        desplazamientoY = V2.coordenadasZona1[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 2:
                        desplazamientoX = V2.coordenadasZona2[0][0]
                        desplazamientoY = V2.coordenadasZona2[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 3:
                        desplazamientoX = V2.coordenadasZona3[0][0]
                        desplazamientoY = V2.coordenadasZona3[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 4:
                        desplazamientoX = V2.coordenadasZona4[0][0]
                        desplazamientoY = V2.coordenadasZona4[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 5:
                        desplazamientoX = V2.coordenadasZona5[0][0]
                        desplazamientoY = V2.coordenadasZona5[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 6:
                        desplazamientoX = V2.coordenadasZona6[0][0]
                        desplazamientoY = V2.coordenadasZona6[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 7:
                        desplazamientoX = V2.coordenadasZona7[0][0]
                        desplazamientoY = V2.coordenadasZona7[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 8:
                        desplazamientoX = V2.coordenadasZona8[0][0]
                        desplazamientoY = V2.coordenadasZona8[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 9:
                        desplazamientoX = V2.coordenadasZona9[0][0]
                        desplazamientoY = V2.coordenadasZona9[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 10:
                        desplazamientoX = V2.coordenadasZona10[0][0]
                        desplazamientoY = V2.coordenadasZona10[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 11:
                        desplazamientoX = V2.coordenadasZona11[0][0]
                        desplazamientoY = V2.coordenadasZona11[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                    elif zonaDespejar == 12:
                        desplazamientoX = V2.coordenadasZona12[0][0]
                        desplazamientoY = V2.coordenadasZona12[0][1]
                        desplazamientoX = desplazamientoX - objetos[0]
                        desplazamientoY = desplazamientoY - objetos[1]
                
                mv.desplazar(objetos,desplazamientoY,desplazamientoX)
                V2.señalCambio[0]=1
                V2.ZonasGuardadasAzules = V2.cambioPosicion(V2.zonaCubosAzules,V2.zonasActualesAzules,V2.ZonasGuardadasAzules)
                V2.señalCambio[0]=1
                V2.ZonasGuardadasVerdes = V2.cambioPosicion(V2.zonaCubosVerdes,V2.zonasActualesVerdes,V2.ZonasGuardadasVerdes)
                V2.correctorCoordenadas(V2.coordenadas_actualesAzules,V2.coordenadasObjetosAzules,V2.ZonasGuardadasAzules,V2.objetos_azules)
                V2.correctorCoordenadas(V2.coordenadas_actualesVerdes,V2.coordenadasObjetosVerdes,V2.ZonasGuardadasVerdes,V2.objetos_verdes)
                print('El cubo se cambio de posicion para evitar coliciones')
                contador = contador+3
            elif indiceDelCuboActual ==  indice:
                print(f'el cubo verde {indiceDelCuboActual} esta bien colocado\n')
                contador = contador+3
        else: 
            contador = contador+3
    tareaAzul1 = vectorRecuerdoAzul[0:3]
    tareaAzul2 = vectorRecuerdoAzul[3:6]
    tareaAzul3 = vectorRecuerdoAzul[6:9]

    tareaVerde1 = vectorRecuerdoVerde[0:3]
    tareaVerde2 = vectorRecuerdoVerde[3:6]
    tareaVerde3 = vectorRecuerdoVerde[6:9]

    print('tareaAzul1',tareaAzul1)
    print('tareaAzul2',tareaAzul2)
    print('tareaAzul3',tareaAzul3)
    
    print('tareaVerde1',tareaVerde1)
    print('tareaVerde2',tareaVerde2)
    print('tareaVerde3',tareaVerde3)

    if tareaAzul1[0] != 0:
        print(f'el cubo azul indice {tareaAzul1[1]} ira en la zona {tareaAzul1[2]}')
        objetos = V2.objetos_azules[tareaAzul1[1]-1]
        zona = tareaAzul1[2]
        zonasCoordenadas(zona,objetos)
    if tareaAzul2[0] != 0:
        print(f'el cubo azul indice {tareaAzul2[1]} ira en la zona {tareaAzul2[2]}')
        objetos = V2.objetos_azules[tareaAzul2[1]-1]
        zona = tareaAzul2[2]
        zonasCoordenadas(zona,objetos)
    if tareaAzul3[0] != 0:
        print(f'el cubo azul indice {tareaAzul3[1]} ira en la zona {tareaAzul3[2]}')
        objetos = V2.objetos_azules[tareaAzul3[1]-1]
        zona = tareaAzul3[2]
        zonasCoordenadas(zona,objetos)
    if tareaVerde1[0] != 0:
        print(f'el cubo verde indice {tareaVerde1[1]} ira en la zona {tareaVerde1[2]}')
        objetos = V2.objetos_verdes[tareaVerde1[1]-1]
        zona = tareaVerde1[2]
        zonasCoordenadas(zona,objetos)
    if tareaVerde2[0] != 0:
        print(f'el cubo verde indice {tareaVerde2[1]} ira en la zona {tareaVerde2[2]}')
        objetos = V2.objetos_verdes[tareaVerde2[1]-1]
        zona = tareaVerde2[2]
        zonasCoordenadas(zona,objetos)
    if tareaVerde3[0] != 0:
        print(f'el cubo verde indice {tareaVerde3[1]} ira en la zona {tareaVerde3[2]}')
        objetos = V2.objetos_verdes[tareaVerde3[1]-1]
        zona = tareaVerde3[2]
        zonasCoordenadas(zona,objetos)



if __name__ == '__main__':
    
    # mv.movimientoInicial()
    objetos = []
    estadoAprendizaje = 0
    estadoReposo = 1
    estadoEjecucion = 0
    saludoOK = 0
    numero_cubos = 0
    tomarInstrucciones = 0
    memoriaEpisodica = [0,0]
    hilo_A = threading.Thread(target= V2.visualizador,)     
    hilo_A.start()
    Encender_Microfono = True
    contador = 0
    contadorInstrucciones = 0
    tareaAprendida = 0
    VectorMemoria = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    global banderaAudio
    
    banderaAudio = 0
    

    def audioVerificador(a):
        global banderaAudio
        if banderaAudio == 0:
            listaMovimiento = rcd.IdentificarMovimiento(a)
            banderaAudio = 1
            return listaMovimiento

        else:
            print('no se ejecuto la tarea')
            numero_cubos = numero_cubos + 1
            stz.respuestas(6)

    while True:
        #*!posible while
        if Encender_Microfono:
            a =  rcd.EntenderAlUsuario()
            if a != 0:
                Encender_Microfono = False
            else:
                Encender_Microfono = True
                # break 
        if estadoReposo == 1 and saludoOK == 0 :
            print('entramos al if del resposo')
            V2.señalCambio[0]=1
            V2.ZonasGuardadasAzules = V2.cambioPosicion(V2.zonaCubosAzules,V2.zonasActualesAzules,V2.ZonasGuardadasAzules)
            V2.señalCambio[0]=1
            V2.ZonasGuardadasVerdes = V2.cambioPosicion(V2.zonaCubosVerdes,V2.zonasActualesVerdes,V2.ZonasGuardadasVerdes)
            V2.correctorCoordenadas(V2.coordenadas_actualesAzules,V2.coordenadasObjetosAzules,V2.ZonasGuardadasAzules,V2.objetos_azules)
            V2.correctorCoordenadas(V2.coordenadas_actualesVerdes,V2.coordenadasObjetosVerdes,V2.ZonasGuardadasVerdes,V2.objetos_verdes)

        if a == 'hola' and estadoReposo == 1:
            stz.respuestas(1)
            stz.solicitudes(1)
            saludoOK = 1
            Encender_Microfono = True
            banderaIniCubos = 1
            print('UR3 recibio el saludo')

        elif a == 'Aprender tarea' and saludoOK == 1:
            print('UR3 esta dispuesto a aprender una tarea')
            #quiero que aprendas una tarea
            #!ejecutar una sola vez 
            V2.señalCambio[0]=1
            V2.ZonasGuardadasAzules = V2.cambioPosicion(V2.zonaCubosAzules,V2.zonasActualesAzules,V2.ZonasGuardadasAzules)
            V2.señalCambio[0]=1
            V2.ZonasGuardadasVerdes = V2.cambioPosicion(V2.zonaCubosVerdes,V2.zonasActualesVerdes,V2.ZonasGuardadasVerdes)
            V2.correctorCoordenadas(V2.coordenadas_actualesAzules,V2.coordenadasObjetosAzules,V2.ZonasGuardadasAzules,V2.objetos_azules)
            V2.correctorCoordenadas(V2.coordenadas_actualesVerdes,V2.coordenadasObjetosVerdes,V2.ZonasGuardadasVerdes,V2.objetos_verdes)
            numero_cubos = len(V2.coordenadas_actualesAzules) + len( V2.coordenadas_actualesVerdes)
            VectAvV = [len(V2.coordenadas_actualesAzules), len( V2.coordenadas_actualesVerdes)]
            print('el nuemro de cubos en el estado de transicion es',numero_cubos)
            if numero_cubos>0:
                estadoAprendizaje = 1
                estadoReposo = 0 
                estadoEjecucion = 0
                stz.respuestas(4)
                tomarInstrucciones = 1
                V2.señalControl[0] = True
                Encender_Microfono = True
                saludoOK = 0

            else:
                print('no se han encontrado cubos por favor espere')
                stz.respuestas(7)
                saludoOK == 0
                numero_cubos = len(V2.coordenadas_actualesAzules) + len( V2.coordenadas_actualesVerdes)
                VectAvV = [len(V2.coordenadas_actualesAzules), len( V2.coordenadas_actualesVerdes)]
                Encender_Microfono = True

        elif estadoAprendizaje == 1  and saludoOK == 0 and tomarInstrucciones == 1:
            print('UR3 esta a la espera de instreucciones')


            V2.señalControl[0] = True

            if numero_cubos>0:
                print('numero de cubos antes de restar ', numero_cubos)
                print('siguiente cubo')
                print('Este es el mensaje que retorna EntenderUsuario:', a)
                if a == 'este':
                    print("algoritmo de la mano")
                    coordenadasGestos = V2.coordenadas_gestos
                    print('ESTAS SON LAS COORDENADAS GUARDADAS',coordenadasGestos)
                    if len(coordenadasGestos) == 2 and coordenadasGestos[0] != 0 :
                        objetos = [coordenadasGestos[0][0],coordenadasGestos[0][1]]
                        objetosEnPixeles = [V2.coordenadasGraficas[0][0],V2.coordenadasGraficas[0][1]]
                        desplazamientoX = round(coordenadasGestos[1][0],2)
                        desplazamientoY = round(coordenadasGestos[1][1],2)

                        # !nueva implementacion:

                        objetoszona = V2.conversorXY2ZN(objetosEnPixeles)
                        zonaFinal = V2.conversorXY2ZN(V2.coordenadasGraficas[1])

                        print('la conversion de las coordenadas del objeto a zonas es: ', objetoszona)
                        print('las zonas azules guardadas son: ', V2.ZonasGuardadasAzules)


                        if objetoszona in V2.ZonasGuardadasAzules:
                            print('el cubo es azul')
                            print(V2.ZonasGuardadasAzules)
                            cuboId = V2.ZonasGuardadasAzules.index(objetoszona)+1
                            print('el indice del elemento  :',objetoszona,'es',cuboId)
                            VectorMemoria[(cuboId-1)*3] = 1
                            VectorMemoria[((cuboId-1)*3)+1] = cuboId
                            VectorMemoria[((cuboId-1)*3)+2] = zonaFinal
                        else:
                            print('el cubo es verde')
                            print(V2.ZonasGuardadasVerdes)
                            cuboId = V2.ZonasGuardadasVerdes.index(objetoszona)+1
                            VectorMemoria[(cuboId-1)*3+9] = 2
                            VectorMemoria[((cuboId-1)*3)+10] = cuboId
                            VectorMemoria[((cuboId-1)*3)+11] = zonaFinal


                        #! final de la nueva implementacion 
                             
                        # desplazamientoX = desplazamientoX - coordenadasGestos[0][0]
                        # desplazamientoY = desplazamientoY - coordenadasGestos[0][1]
                        PosicionFinalx = (desplazamientoX-objetos[0])
                        PosicionFinaly = (desplazamientoY-objetos[1])
                        PosicionFinalx = round(PosicionFinalx,2)
                        PosicionFinaly = round(PosicionFinaly,2)
                        print(objetos)
                        print(PosicionFinalx)
                        print(PosicionFinaly)
                        mv.desplazar(objetos,PosicionFinaly,PosicionFinalx)
                        V2.coordenadas_gestos[0] = 0
                        coordenadasGestos[0] = 0
                        V2.cuboRetornadoGesto[0] = None
                        numero_cubos = numero_cubos - 1
                        
                        V2.señalCambio[0]=1
                        V2.ZonasGuardadasAzules = V2.cambioPosicion(V2.zonaCubosAzules,V2.zonasActualesAzules,V2.ZonasGuardadasAzules)
                        V2.señalCambio[0]=1
                        V2.ZonasGuardadasVerdes = V2.cambioPosicion(V2.zonaCubosVerdes,V2.zonasActualesVerdes,V2.ZonasGuardadasVerdes)
                        V2.correctorCoordenadas(V2.coordenadas_actualesAzules,V2.coordenadasObjetosAzules,V2.ZonasGuardadasAzules,V2.objetos_azules)
                        V2.correctorCoordenadas(V2.coordenadas_actualesVerdes,V2.coordenadasObjetosVerdes,V2.ZonasGuardadasVerdes,V2.objetos_verdes)
                        stz.respuestas(8)
                        Encender_Microfono = True
                    


                else:
                    listaMovimiento = rcd.IdentificarMovimiento(a)
                    if listaMovimiento[2] != 0:
                        print(listaMovimiento)
                        color = listaMovimiento[1]
                        cuboId = listaMovimiento[2]
                        zonaId = listaMovimiento[5]
                        if color == 1:
                            VectorMemoria[(cuboId-1)*3] = 1
                            VectorMemoria[((cuboId-1)*3)+1] = cuboId
                            VectorMemoria[((cuboId-1)*3)+2] = zonaId
                            objetos = V2.objetos_azules[cuboId-1]
                        
                        elif color == 2:
                            VectorMemoria[(cuboId-1)*3+9] = 2
                            VectorMemoria[((cuboId-1)*3)+10] = cuboId
                            VectorMemoria[((cuboId-1)*3)+11] = zonaId
                            objetos = V2.objetos_verdes[cuboId-1]
                            
                        if zonaId != 0:
                            if zonaId == 1:
                                desplazamientoX = V2.coordenadasZona1[0][0]
                                desplazamientoY = V2.coordenadasZona1[0][1]
                                desplazamientoX = desplazamientoX - objetos[0]
                                desplazamientoY = desplazamientoY - objetos[1]
                            elif zonaId == 2:
                                desplazamientoX = V2.coordenadasZona2[0][0]
                                desplazamientoY = V2.coordenadasZona2[0][1]
                                desplazamientoX = desplazamientoX - objetos[0]
                                desplazamientoY = desplazamientoY - objetos[1]
                            elif zonaId == 3:
                                desplazamientoX = V2.coordenadasZona3[0][0]
                                desplazamientoY = V2.coordenadasZona3[0][1]
                                desplazamientoX = desplazamientoX - objetos[0]
                                desplazamientoY = desplazamientoY - objetos[1]
                            elif zonaId == 4:
                                desplazamientoX = V2.coordenadasZona4[0][0]
                                desplazamientoY = V2.coordenadasZona4[0][1]
                                desplazamientoX = desplazamientoX - objetos[0]
                                desplazamientoY = desplazamientoY - objetos[1]
                            elif zonaId == 5:
                                desplazamientoX = V2.coordenadasZona5[0][0]
                                desplazamientoY = V2.coordenadasZona5[0][1]
                                desplazamientoX = desplazamientoX - objetos[0]
                                desplazamientoY = desplazamientoY - objetos[1]
                            elif zonaId == 6:
                                desplazamientoX = V2.coordenadasZona6[0][0]
                                desplazamientoY = V2.coordenadasZona6[0][1]
                                desplazamientoX = desplazamientoX - objetos[0]
                                desplazamientoY = desplazamientoY - objetos[1]
                            elif zonaId == 7:
                                desplazamientoX = V2.coordenadasZona7[0][0]
                                desplazamientoY = V2.coordenadasZona7[0][1]
                                desplazamientoX = desplazamientoX - objetos[0]
                                desplazamientoY = desplazamientoY - objetos[1]
                            elif zonaId == 8:
                                desplazamientoX = V2.coordenadasZona8[0][0]
                                desplazamientoY = V2.coordenadasZona8[0][1]
                                desplazamientoX = desplazamientoX - objetos[0]
                                desplazamientoY = desplazamientoY - objetos[1]
                            elif zonaId == 9:
                                desplazamientoX = V2.coordenadasZona9[0][0]
                                desplazamientoY = V2.coordenadasZona9[0][1]
                                desplazamientoX = desplazamientoX - objetos[0]
                                desplazamientoY = desplazamientoY - objetos[1]
                            elif zonaId == 10:
                                desplazamientoX = V2.coordenadasZona10[0][0]
                                desplazamientoY = V2.coordenadasZona10[0][1]
                                desplazamientoX = desplazamientoX - objetos[0]
                                desplazamientoY = desplazamientoY - objetos[1]
                            elif zonaId == 11:
                                desplazamientoX = V2.coordenadasZona11[0][0]
                                desplazamientoY = V2.coordenadasZona11[0][1]
                                desplazamientoX = desplazamientoX - objetos[0]
                                desplazamientoY = desplazamientoY - objetos[1]
                            elif zonaId == 12:
                                desplazamientoX = V2.coordenadasZona12[0][0]
                                desplazamientoY = V2.coordenadasZona12[0][1]
                                desplazamientoX = desplazamientoX - objetos[0]
                                desplazamientoY = desplazamientoY - objetos[1]
                        else:
                            desplazamientoX = listaMovimiento[4][0]
                            desplazamientoY = listaMovimiento[4][1]
                        print(desplazamientoX,desplazamientoY)
                        # print(objetos)
                        # memoriaEpisodica[contador] = [color,zonaId]
                        # print(memoriaEpisodica)
                        mv.desplazar(objetos,desplazamientoY,desplazamientoX)
                        V2.señalCambio[0]=1
                        V2.ZonasGuardadasAzules = V2.cambioPosicion(V2.zonaCubosAzules,V2.zonasActualesAzules,V2.ZonasGuardadasAzules)
                        V2.señalCambio[0]=1
                        V2.ZonasGuardadasVerdes = V2.cambioPosicion(V2.zonaCubosVerdes,V2.zonasActualesVerdes,V2.ZonasGuardadasVerdes)
                        V2.correctorCoordenadas(V2.coordenadas_actualesAzules,V2.coordenadasObjetosAzules,V2.ZonasGuardadasAzules,V2.objetos_azules)
                        V2.correctorCoordenadas(V2.coordenadas_actualesVerdes,V2.coordenadasObjetosVerdes,V2.ZonasGuardadasVerdes,V2.objetos_verdes)
                        print('el vector de memoria ',VectorMemoria)
                        stz.respuestas(8)
                        numero_cubos = numero_cubos - 1
                        print('numero de cubos restado es igual a: ',numero_cubos)
                        Encender_Microfono = True
                    else:
                        print('no se ejecuto la tarea')
                        stz.respuestas(6)
                        Encender_Microfono = True
                    
                    
                    V2.señalCambio[0]=1
                    V2.ZonasGuardadasAzules = V2.cambioPosicion(V2.zonaCubosAzules,V2.zonasActualesAzules,V2.ZonasGuardadasAzules)
                    V2.señalCambio[0]=1
                    V2.ZonasGuardadasVerdes = V2.cambioPosicion(V2.zonaCubosVerdes,V2.zonasActualesVerdes,V2.ZonasGuardadasVerdes)
                    V2.correctorCoordenadas(V2.coordenadas_actualesAzules,V2.coordenadasObjetosAzules,V2.ZonasGuardadasAzules,V2.objetos_azules)
                    V2.correctorCoordenadas(V2.coordenadas_actualesVerdes,V2.coordenadasObjetosVerdes,V2.ZonasGuardadasVerdes,V2.objetos_verdes)
                        
            if numero_cubos == 0:
                stz.respuestas(5)
                tareaAprendida = 1
                print('Instrucciones finalizadas')
                print('el vector de cantidad de cubos es: ',VectAvV)
                cme.EscribirEnMemoria(VectAvV, VectorMemoria)
                VectorMemoria = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                estadoAprendizaje = 0
                estadoReposo = 1
                saludoOK = 0
                tomarInstrucciones = 0
                V2.señalControl[0] = False

        
        elif a == 'Ejecutar tarea' and saludoOK == 1 and estadoAprendizaje == 0:    
            print('UR3 esta preparado para ejecutar una tarea')
            V2.señalCambio[0]=1
            V2.ZonasGuardadasAzules = V2.cambioPosicion(V2.zonaCubosAzules,V2.zonasActualesAzules,V2.ZonasGuardadasAzules)
            V2.señalCambio[0]=1
            V2.ZonasGuardadasVerdes = V2.cambioPosicion(V2.zonaCubosVerdes,V2.zonasActualesVerdes,V2.ZonasGuardadasVerdes)
            V2.correctorCoordenadas(V2.coordenadas_actualesAzules,V2.coordenadasObjetosAzules,V2.ZonasGuardadasAzules,V2.objetos_azules)
            V2.correctorCoordenadas(V2.coordenadas_actualesVerdes,V2.coordenadasObjetosVerdes,V2.ZonasGuardadasVerdes,V2.objetos_verdes)
            cubos = [len(V2.coordenadas_actualesAzules),len(V2.coordenadas_actualesVerdes)] 
            if cubos[0]>0:
                print('Esta es la cantidad de cubos que ve UR3 ',cubos)
                tarea = cme.BuscarEnMemoria(cubos)
                # tarea = [1,1,8,1,2,12,0,0,0,2,1,7,0,0,0,0,0,0]
                print('esta es la tarea que va a ejecutar UR3',tarea)
                if tarea != None:
                    banderaDeTarea = 1
                    if banderaDeTarea == 1:
                        vectorZonaActualAzul = V2.ZonasGuardadasAzules
                        voctorZonaActualVerde = V2.ZonasGuardadasVerdes
                        banderaDeTarea = 0
                    menProcedural(tarea,vectorZonaActualAzul,voctorZonaActualVerde)
                    print('Se termino la funcion desde el estado ejecucion ')
                    stz.respuestas(2)
                    estadoReposo = 1
                    estadoEjecucion = 0
                    saludoOK = 0
                    Encender_Microfono = True
                else:
                    stz.respuestas(7)
                    cubos = [len(V2.coordenadas_actualesAzules),len(V2.coordenadas_actualesVerdes)] 
                    print('Esta es la cantidad de cubos que veo ahora ', cubos)
                    estadoReposo = 1
                    estadoEjecucion = 0
                    saludoOK = 0
                    Encender_Microfono = True
            else:
                stz.respuestas(9)
                cubos = [len(V2.coordenadas_actualesAzules),len(V2.coordenadas_actualesVerdes)] 
                print('Esta es la cantidad de cubos que veo ahora ', cubos)
                estadoReposo = 1
                estadoEjecucion = 0
                saludoOK = 1
                Encender_Microfono = True
                



          
            # print('el contador de instrucciones es: ', contadorInstrucciones)
            # if contadorInstrucciones == 1:
            #     print('Entro al if con un valor de: ', contadorInstrucciones)
            #     # saludoOK = 0
            #     estadoReposo = 1
            #     estadoEjecucion = 0
            
        else:
            Encender_Microfono = True


        




       



# https://www.digitalocean.com/community/tutorials/python-multiprocessing-example
# https://www.tutorialspoint.com/python/python_multithreading.htm
# https://superfastpython.com/multiprocessing-queue-in-python/
# https://www.digitalocean.com/community/tutorials/python-multiprocessing-example