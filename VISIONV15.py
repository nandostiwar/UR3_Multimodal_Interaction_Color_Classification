import cv2
import numpy as np
import time 
import mediapipe as mp



#############################################################
#             *!Definicion de variables                     #
#############################################################
coordenadasZona1 = [0]
coordenadasZona2 = [0]
coordenadasZona3 = [0]
coordenadasZona4 = [0]
coordenadasZona5 = [0]
coordenadasZona6 = [0]
coordenadasZona7 = [0]
coordenadasZona8 = [0]
coordenadasZona9 = [0]
coordenadasZona10 = [0]
coordenadasZona11 = [0]
coordenadasZona12 = [0]
coordenadas_gestos = [0,0]
cuboRetornadoGesto = [None]
cuboAzulEncontrado = False
CuboVerdeEncontrado = False
puntos = []
detector = False
señalControl  = [False]
señalCambio = [0]
coordenadasGraficas = [0,0]
colorCuboMemoria = 0
vectorMemori = [0]
coordenadasCentrosZonas = []
cubosAzules = [0,0,0,]
cubosAzulesBusy=[0,0,0]

#############################################################
#                     Amarillo                              # 
#############################################################
amarillobajo = np.array([15,100,20],np.uint8)
amarilloalto = np.array([45,255,255],np.uint8)
coordenadas_centroAmarillo = []
coordenadas_actualesAmarillo = []
objetos_amarillos = []
#############################################################
#                         Azul                              # 
#############################################################

# azulbajo = np.array([100,100,20],np.uint8)
azulbajo = np.array([100,150,20],np.uint8)
azulalto = np.array([107,255,255],np.uint8)
coordenadas_centroAzules = []
coordenadas_actualesAzules = []
objetos_azules = [0,0,0]
#! verificador azul
zonasActualesAzules = []
ZonasGuardadasAzules = [0,0,0]
ZonasAuxiliares = []
coordenadasObjetosAzules = [0,0,0]
#! verificador verde
zonasActualesVerdes = []
ZonasGuardadasVerdes = [0,0,0]
ZonasAuxiliares = []
coordenadasObjetosVerdes = [0,0,0]
#############################################################
#                        Verde                              # 
#############################################################
verdebajo = np.array([47,50,20],np.uint8)
verdealto = np.array([99,230,230],np.uint8)
coordenadas_centroVerdes = []
coordenadas_actualesVerdes = []
objetos_verdes = [0,0,0]
#############################################################
#                 Parametros de manos                       # 
#############################################################   
mp_drawing =  mp.solutions.drawing_utils #Sirve para dibujar los 21 puntos clave de las manos
mp_hands = mp.solutions.hands 
cx = 0
cy = 0
cxPrima = 75
CyPrima = 468
Mano = 0
distanciaManoCubosAzules = [None,None,None,None]
distanciaManoCubosVerdes = [None,None,None,None]
colorCuboMascaraAlto = np.array([264,69,50],np.uint8)
colorCuboMascaraBajo = np.array([260,69,50],np.uint8)
#############################################################
#          Parametros del espacio de trabajo                # 
#############################################################  
ROI_cm_X = 32.20
ROI_cm_Y = 22.25

ROI_mm_X = ROI_cm_X*10
ROI_mm_Y = ROI_cm_Y*10

imagen_resolucion_X = 640 
imagen_resolucion_Y =  480

#############################################################
#               *!Definicion de funciones                   #
#############################################################

def cambioPosicion(zonaCubos,zonasActuales,ZonasGuardadas):
    


    # global coordenadasAuxiliares
    global señalCambio

    contador = 0
    zonasActuales = zonaCubos
    # coordenadasAuxiliares = coordenadas_actualesAzules
    # print('coordenadas auxiliares ',coordenadasAuxiliares)
    # print('coordenadas guardadas', coordenadasObjetosAzules)
    ciclos = len(zonasActuales)
    if señalCambio[0] == 1:
        while contador != ciclos:
            if ZonasGuardadas[contador] == zonasActuales[contador]:
                contador = contador +1
            else:
                if zonasActuales[contador] in ZonasGuardadas:
                    # print('el elemento ya esta añadido')
                    contador = contador + 1
                else:
                    for zona in ZonasGuardadas:
                        if zona in zonasActuales:
                            print(f'la zona{zona}, esta en las zonas actuales')
                        else:
                            elemento = zona
                            # print(f'se va a eliminar{elemento}')
                            index = ZonasGuardadas.index(elemento)
                            ZonasGuardadas[index] = 0
                            # coordenadasObjetosAzules[index] = 0
                            index = ZonasGuardadas.index(0)
                            ZonasGuardadas[index] = zonasActuales[contador]
                            # coordenadasObjetosAzules[index] = coordenadasAuxiliares[contador]
                            contador = contador + 1
                            break
        # if contador == ciclos:
        #     señalCambio[0] = 0
        #     return ZonasGuardadas
        
        señalCambio[0] = 0
        return ZonasGuardadas

def correctorCoordenadas(coordenadas_actuales,coordenadasObjetos,ZonasGuardadas,objetos):

    for i in range(len(coordenadas_actuales)):
        zonaAuxiliar = conversorXY2ZN(coordenadas_actuales[i])
        indice = ZonasGuardadas.index(zonaAuxiliar)
        coordenadasObjetos[indice] = coordenadas_actuales[i]
        coordenadas = calibracion(coordenadas_actuales[i]) 
        objetos[indice] = coordenadas
    # print('las coordenadas corregidas son: ',coordenadasObjetos)
    # print('las coordenadas sin corregir son: ',coordenadas_actuales)

def distancia(x1,y1,x2,y2):
    p1 = np.array([x1, y1])
    p2 = np.array([x2,y2])

    return np.linalg.norm(p1 -p2)

def detector_espacioT(frame):
    
    global detector
    global maskroja5
    #Rojo
    rojolbajo1 = np.array([0,100,20],np.uint8)
    rojolalto1 = np.array([5,255,255],np.uint8)
    rojolbajo2 = np.array([175,100,20],np.uint8)
    rojolalto2 = np.array([179,255,255],np.uint8)

    imHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    maskroja3 = cv2.inRange(imHSV,rojolbajo1,rojolalto1)
    maskroja4 = cv2.inRange(imHSV,rojolbajo2,rojolalto2)
    maskroja5 = cv2.add(maskroja3,maskroja4)
    cv2.imwrite('maskroja.png',maskroja5)

    # cv2.imshow("maskroja5",maskroja5)
    
    contornos,_ =cv2.findContours(maskroja5,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contornos=sorted(contornos,key=cv2.contourArea,reverse=True)[:2]

    if len(contornos)>1:
        contornos.pop(0)
        for c in contornos :
            epsilon = 0.01*cv2.arcLength(c,True)
            approx = cv2.approxPolyDP(c,epsilon,True)
            if (len(approx)) == 4:
                puntos.append(approx[1][0])
                puntos.append(approx[0][0])
                puntos.append(approx[2][0])
                puntos.append(approx[3][0])
                detector = True
                return puntos
    else:
        print('No se encontro el espacio de trabajo')
        detector = False
        return detector

def calibracion(coordenadas):
    global imagen_resolucion_X
    global imagen_resolucion_Y
    global ROI_cm_X
    global ROI_cm_Y
    x = coordenadas[0]
    y = coordenadas[1]
    if (x*(ROI_cm_X/imagen_resolucion_X))>=16.1 and (y*(ROI_cm_Y/imagen_resolucion_Y)) >= 18.125:
        coorx = x*(ROI_cm_X/imagen_resolucion_X)-0.25
        coory = y*(ROI_cm_Y/imagen_resolucion_Y)+1
    elif (x*(ROI_cm_X/imagen_resolucion_X))>=16.1 and (y*(ROI_cm_Y/imagen_resolucion_Y)) <= 3:
        coorx = x*(ROI_cm_X/imagen_resolucion_X)-0.25
        coory = y*(ROI_cm_Y/imagen_resolucion_Y)+2
    elif (x*(ROI_cm_X/imagen_resolucion_X))<16.1 and (y*(ROI_cm_Y/imagen_resolucion_Y)) >= 18.125:
        coorx = x*(ROI_cm_X/imagen_resolucion_X)+1
        coory = y*(ROI_cm_Y/imagen_resolucion_Y)+1
    elif (x*(ROI_cm_X/imagen_resolucion_X))<16.1 and (y*(ROI_cm_Y/imagen_resolucion_Y)) <= 3:
        coorx = x*(ROI_cm_X/imagen_resolucion_X)+0.25
        coory = y*(ROI_cm_Y/imagen_resolucion_Y)+2
    else:
        coorx = x*(ROI_cm_X/imagen_resolucion_X)+0.5
        coory = y*(ROI_cm_Y/imagen_resolucion_Y)+1
    return[coorx,coory]

def conversorXY2ZN(coordenadas):

    coordenadax = coordenadas[0] 
    coordenaday = coordenadas[1]

    if coordenadax<160 and coordenaday<160:
        zona = 1
    elif coordenadax>160 and coordenadax<320 and coordenaday<160:
        zona = 2
    elif coordenadax>320 and coordenadax<480 and coordenaday<160:
        zona = 3
    elif coordenadax>480 and coordenadax<640 and coordenaday<160:
        zona = 4
    elif coordenadax<160 and coordenaday>160 and coordenaday<320 :
        zona = 5
    elif coordenadax>160 and coordenadax<320 and coordenaday>160 and coordenaday<320:
        zona = 6
    elif coordenadax>320 and coordenadax<480 and coordenaday>160 and coordenaday<320:
        zona = 7
    elif coordenadax>480 and coordenadax<640 and coordenaday>160 and coordenaday<320:
        zona = 8
    elif coordenadax<160 and coordenaday>320 and coordenaday<480 :
        zona = 9
    elif coordenadax>160 and coordenadax<320 and coordenaday>320 and coordenaday<480:
        zona = 10
    elif coordenadax>320 and coordenadax<480 and coordenaday>320 and coordenaday<480:
        zona = 11
    elif coordenadax>480 and coordenadax<640 and coordenaday>320 and coordenaday<480:
        zona = 12
    else:
        zona = 1
        # print(coordenadax,coordenaday)
    return(zona)

def procesamiento(frameHSV,dst):
    
    global azulbajo
    global azulalto
    global verdebajo
    global verdealto
    global cx
    global cy
    global colorCuboMascaraBajo
    global colorCuboMascaraAlto
    global cubosAzules
    global zonaCubosAzules
    global zonaCubosVerdes
    
    maskPunto = cv2.inRange(frameHSV,colorCuboMascaraBajo,colorCuboMascaraAlto)
    cv2.imshow('mascaraPunto',maskPunto)

    maskazul = cv2.inRange(frameHSV,azulbajo,azulalto)
    cv2.imshow("maskazul",maskazul)
    maskverde = cv2.inRange(frameHSV,verdebajo,verdealto)
    cv2.imshow("maskazul",maskazul)

    contorno2,_ = cv2.findContours(maskverde,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contorno1,_ = cv2.findContours(maskazul,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contorno1:    
        area = cv2.contourArea(c)
        if area > 2500:   
            M = cv2.moments(c)
            if (M['m00']) == 0:
                M['m00'] = 1
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])
            cv2.circle(dst,(x,y),7,(0,255,0),-1)
            font = cv2.FONT_ITALIC
            cv2.putText(dst,'{},{}'.format('%.2f'%(x*(ROI_cm_X/imagen_resolucion_X)),'%.2f'%(y*(ROI_cm_Y/imagen_resolucion_Y))),(x,y+50),font,0.5,(0,0,255),
                        2,cv2.LINE_AA)
            
            coordendas_cubo_azul = [x,y]
            coordenadas_actualesAzules.append(coordendas_cubo_azul)
            zonaAzul = conversorXY2ZN(coordendas_cubo_azul)
            zonaCubosAzules.append(zonaAzul)
            ID_Azul = len(coordenadas_actualesAzules)
            # if ID_Azul != 0:
            #     calibracion(x,y,imagen_resolucion_X,imagen_resolucion_Y,ROI_cm_X,ROI_cm_Y,'Azul',ID_Azul)

            for cubos in ZonasGuardadasAzules:
                index = ZonasGuardadasAzules.index(cubos)
                if cubos !=0:
                    coordenadax = coordenadasZonaTotal[cubos-1][0]
                    coordenaday = coordenadasZonaTotal[cubos-1][1]

                    cv2.putText(dst,f'Cubo Azul {index+1}',[coordenadax-30,coordenaday-50],cv2.FONT_ITALIC,0.5,(0,255,0),2,cv2.LINE_AA)
                     
    for c in contorno2:
        area = cv2.contourArea(c)
        if area > 1500:     
            M = cv2.moments(c)
            if (M['m00']) == 0:
                M['m00'] = 1
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])
            cv2.circle(dst,(x,y),7,(0,255,0),-1)
            font = cv2.FONT_ITALIC
            cv2.putText(dst,'{},{}'.format('%.2f'%(x*(ROI_cm_X/imagen_resolucion_X)),'%.2f'%(y*(ROI_cm_Y/imagen_resolucion_Y))),(x,y+50),font,0.5,(0,0,255),
                                        2,cv2.LINE_AA)
            coordendas_cubo_verde = [x,y]
            coordenadas_actualesVerdes.append(coordendas_cubo_verde)
            zonaVerde = conversorXY2ZN(coordendas_cubo_verde)
            zonaCubosVerdes.append(zonaVerde)
            ID_Verde = len(coordenadas_actualesVerdes)
            # if ID_Verde != 0:
            #     calibracion(x,y,imagen_resolucion_X,imagen_resolucion_Y,ROI_cm_X,ROI_cm_Y,'Verde',ID_Verde)

            for cubos in ZonasGuardadasVerdes:
                index = ZonasGuardadasVerdes.index(cubos)
                if cubos !=0:
                    coordenadax = coordenadasZonaTotal[cubos-1][0]
                    coordenaday = coordenadasZonaTotal[cubos-1][1]

                    cv2.putText(dst,f'Cubo verde {index+1}',[coordenadax-30,coordenaday-50],cv2.FONT_ITALIC,0.5,(0,255,0),2,cv2.LINE_AA)
                
def gestos(frame,hands,dst):

    global imagen_resolucion_X
    global imagen_resolucion_Y
    global coordenadas_gestos
    global cx
    global cy
    global cxPrima
    global CyPrima
    global Mano
    global cuboRetornadoGesto
    global cuboAzulEncontrado 
    global CuboVerdeEncontrado 
    color_punto = (255,255,0)

    frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)      
    # frame_RGB = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)      
    results = hands.process(frame_RGB)

    Abierto = 0
    bandera_axu = 1

    # coordenadas_gestos = [0,0]
    if results.multi_hand_landmarks is not None and señalControl[0] == True:
        Mano = 1
        
        for hand_landmarks in results.multi_hand_landmarks:
            
            x1 = int(hand_landmarks.landmark[4].x*imagen_resolucion_X) 
            y1 = int(hand_landmarks.landmark[4].y*imagen_resolucion_Y)
            #Indice
            x2 = int(hand_landmarks.landmark[8].x*imagen_resolucion_X) 
            y2 = int(hand_landmarks.landmark[8].y*imagen_resolucion_Y)
            cx,cy = (x1 + x2) // 2,(y1 + y2)//2

            cv2.circle(frame,(x1,y1),5,color_punto, -1)
            cv2.circle(frame,(x2,y2),5,color_punto, -1)    
            cv2.line(frame,(x1,y1),(x2,y2),(255,0,255),2) 
            cv2.circle(frame,(cx,cy),8,(130,40,76), -1)
        
        distance = distancia(x1,y1,x2,y2)
        if distance<30 and señalControl[0]==True:
            cv2.circle(frame,(cx,cy),8,(0,0,255), -1)
            cv2.putText(frame,"Cerrado",(0,470),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),3)
            cv2.putText(dst,"Cerrado",(0,470),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),3)
            if coordenadas_gestos[0] == 0 and cuboRetornadoGesto[0] != None:
                coordenadas_gestos[0] = cuboRetornadoGesto[0]
            else:
                coordenadas_gestos[1] = [cxPrima*(ROI_cm_X/imagen_resolucion_X),CyPrima*(ROI_cm_Y/imagen_resolucion_Y)]
                coordenadasGraficas[1] = [cxPrima,CyPrima]
                # cv2.line(dst,(cxPrima,CyPrima),(coordenadas_gestos[0][0],coordenadas_gestos[0][1]),(0,0,180),2)
            

                if cxPrima<160 and CyPrima<160:
                    zona = 1
                    vectorMemori[0] = [colorCuboMemoria,zona]
                    print('la coordenada mano quedo en la zona 1')
                elif cxPrima>160 and cxPrima<320 and CyPrima<160:
                    zona = 2
                    vectorMemori[0] = [colorCuboMemoria,zona]
                    print('la coordenada mano quedo en la zona 2')
                
                elif cxPrima>320 and cxPrima<480 and CyPrima<160:
                    zona = 3
                    vectorMemori[0] = [colorCuboMemoria,zona]
                    print('la coordenada mano quedo en la zona 3')
                    
                elif cxPrima>480 and cxPrima<640 and CyPrima<160:
                    zona = 4
                    vectorMemori[0] = [colorCuboMemoria,zona]
                    print('la coordenada mano quedo en la zona 4')
               
                elif cxPrima<160 and CyPrima>160 and CyPrima<320 :
                    zona = 5
                    vectorMemori[0] = [colorCuboMemoria,zona]
                    print('la coordenada mano quedo en la zona 5')

                elif cxPrima>160 and cxPrima<320 and CyPrima>160 and CyPrima<320:
                    zona = 6
                    vectorMemori[0] = [colorCuboMemoria,zona]
                    print('la coordenada mano quedo en la zona 6')
                
                elif cxPrima>320 and cxPrima<480 and CyPrima>160 and CyPrima<320:
                    zona = 7
                    vectorMemori[0] = [colorCuboMemoria,zona]
                    print('la coordenada mano quedo en la zona 7')
                    
                elif cxPrima>480 and cxPrima<640 and CyPrima>160 and CyPrima<320:
                    zona = 8
                    vectorMemori[0] = [colorCuboMemoria,zona]
                    print('la coordenada mano quedo en la zona 8')

                elif cxPrima<160 and CyPrima>320 and CyPrima<480 :
                    zona = 9
                    vectorMemori[0] = [colorCuboMemoria,zona]
                    print('la coordenada mano quedo en la zona 9')

                elif cxPrima>160 and cxPrima<320 and CyPrima>320 and CyPrima<480:
                    zona = 10
                    vectorMemori[0] = [colorCuboMemoria,zona]
                    print('la coordenada mano quedo en la zona 10')
                
                elif cxPrima>320 and cxPrima<480 and CyPrima>320 and CyPrima<480:
                    zona = 11
                    vectorMemori[0] = [colorCuboMemoria,zona]
                    print('la coordenada mano quedo en la zona 11')
                    
                elif cxPrima>480 and cxPrima<640 and CyPrima>320 and CyPrima<480:
                    zona = 12
                    vectorMemori[0] = [colorCuboMemoria,zona]
                    print('la coordenada mano quedo en la zona 12')


                
            print('coordenadas cerrado ', coordenadas_gestos)

        elif distance>30:
            cv2.putText(frame,"Abierto",(0,470),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
            cv2.putText(dst,"Abierto",(0,470),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
            Abierto = 1
        cuboGesto(dst)
        
    cantidadCubos = len(objetos_azules) + len(objetos_verdes) 

    # if len(coordenadas_gestos) == 2 and coordenadasGraficas[1] != 0 and bandera_axu == 1  and cantidadCubos != 0:

    #     # cv2.line(dst,(coordenadasGraficas[0][0],coordenadasGraficas[0][1]),(coordenadasGraficas[1][0],coordenadasGraficas[1][1]),(180,0,180),11)
    #     bandera_axu = 0

def cuboGesto(dst):
    global Mano
    global cx
    global cy
    global coordenadas_actualesAzules
    global coordenadas_actualesVerdes
    global distanciaManoCubosAzules
    global distanciaCubosVerdes
    global cuboRetornadoGesto
    global cuboAzulEncontrado 
    global CuboVerdeEncontrado 
    global cxPrima
    global CyPrima
    global señalControl
    global coordenadasGraficas
    global colorCuboMemoria


    if Mano == 1 and señalControl[0] ==True:
        cuboAzulEncontrado = False
        CuboVerdeEncontrado = False

        distanciaManoCubosAzules=[10000,10000,10000,10000]
        distanciaManoCubosVerdes=[10000,10000,10000,10000]

        indexAzul = 0 
        for coordenadas in coordenadas_actualesAzules:
            cv2.line(dst,(cxPrima,CyPrima),(coordenadas_actualesAzules[indexAzul]),(180,0,0),2)
            distanciaCubosAzules = distancia(coordenadas[0],coordenadas[1],cxPrima,CyPrima)
            distanciaManoCubosAzules[indexAzul] = (distanciaCubosAzules)
            indexAzul = indexAzul+1
        distanciaMinimaAzul = min(distanciaManoCubosAzules)
        # print('La distancia minima de las azules es: ',distanciaMinimaAzul)
        # print('la distancia es al cubo azul es:',distanciaManoCubosAzules)
 
        indexVerde = 0
        for coordenadas in coordenadas_actualesVerdes:
            cv2.line(dst,(cxPrima,CyPrima),(coordenadas_actualesVerdes[indexVerde]),(0,180,0),2)
            # print('coordenadas verdes ', coordenadas)
            distanciaCubosVerdes = distancia(coordenadas[0],coordenadas[1],cxPrima,CyPrima)
            distanciaManoCubosVerdes[indexVerde] = (distanciaCubosVerdes)
            indexVerde = indexVerde + 1
        distanciaMinimaVerde = min(distanciaManoCubosVerdes)
        # print('La distancia minima de las Verdes es: ',distanciaMinimaVerde)
        # print('la distancia es al cubo Verde es:',distanciaManoCubosVerdes)

        if distanciaMinimaAzul<distanciaMinimaVerde:
            cuboAzulEncontrado = True
            colorCuboMemoria = 1
            # print('Azul es minimo')
            indice = distanciaManoCubosAzules.index(distanciaMinimaAzul)
            if distanciaMinimaAzul<150:
                cv2.line(dst,(cxPrima,CyPrima),(coordenadas_actualesAzules[indice]),(0,0,180),2)
                cuboRetornadoGesto[0] = [objetos_azules[indice][0],objetos_azules[indice][1]] 
                coordenadasGraficas[0] = [coordenadas_actualesAzules[indice][0],coordenadas_actualesAzules[indice][1]] 
            # cv2.line(dst,(cx,cy),(coordenadas_actualesAzules[indice]),(0,0,180),2)

        else:
            colorCuboMemoria = 2
            CuboVerdeEncontrado = True
            # print('Verde es minimo')
            indice = distanciaManoCubosVerdes.index(distanciaMinimaVerde)
            if distanciaMinimaVerde<150: 
                cv2.line(dst,(cxPrima,CyPrima),(coordenadas_actualesVerdes[indice]),(0,0,180),2)
                cuboRetornadoGesto[0] = [objetos_verdes[indice][0],objetos_verdes[indice][1]]
                coordenadasGraficas[0] = [coordenadas_actualesVerdes[indice][0],coordenadas_actualesVerdes[indice][1]] 
            # cv2.line(dst,(cx,cy),(coordenadas_actualesAzules[indice]),(0,0,180),2)

def visualizador():
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture('PRUEBAVIDEO8.mp4')
    # cap = cv2.VideoCapture('PRUEBAVIDEO9.mp4')
    # cap = cv2.VideoCapture('PRUEBAVIDEO10.mp4')
    # cap = cv2.VideoCapture('PRUEBAVIDEO11.mp4')
    # cap = cv2.VideoCapture('PRUEBAVIDEO13.mp4')
    # cap = cv2.VideoCapture('PRUEBAVIDEO14.mp4')
    # cap = cv2.VideoCapture('PRUEBAVIDEO15.mp4')
    # cap = cv2.VideoCapture('PRUEBAVIDEO16.mp4')
    # cap = cv2.VideoCapture('PRUEBAVIDEO8.mp4')
    global imagen_resolucion_X
    global imagen_resolucion_Y
    global detector
    global coordenadasZona1
    global coordenadasZona2 
    global coordenadasZona3 
    global coordenadasZona4 
    global coordenadasZona5 
    global coordenadasZona6 
    global coordenadasZona7 
    global coordenadasZona8 
    global coordenadasZona9 
    global coordenadasZona10 
    global coordenadasZona11 
    global coordenadasZona12 
    global coordenadasZonaTotal
    global ZonasGuardadasAzules
    global ZonasGuardadasVerdes
    global zonasActualesAzules

    global coordenadas_centroAmarillo
    global coordenadas_actualesAmarillo
    global objetos_amarillos
    global coordenadas_centroAzules 
    global coordenadas_actualesAzules 
    global objetos_azules 
    global coordenadas_centroVerdes
    global coordenadas_actualesVerdes
    global objetos_verdes
    global cxPrima
    global CyPrima
    global VcubosAC
    global zonaCubosAzules
    global zonaCubosVerdes
    pTime = 0
    Z1centroX = int((imagen_resolucion_X/4)/2)
    Z1centroY = int((imagen_resolucion_Y/3)/2)

    coordenadasZona1[0] =[Z1centroX*(ROI_cm_X/imagen_resolucion_X),Z1centroY*(ROI_cm_Y/imagen_resolucion_Y)] 

    Z2centroX = int(3*Z1centroX)
    Z2centroY = int(Z1centroY)

    coordenadasZona2[0] =[Z2centroX*(ROI_cm_X/imagen_resolucion_X),Z2centroY*(ROI_cm_Y/imagen_resolucion_Y)] 
    
    Z3centroX = int(5*Z1centroX)
    Z3centroY = int(Z1centroY)
    
    coordenadasZona3[0] =[Z3centroX*(ROI_cm_X/imagen_resolucion_X),Z3centroY*(ROI_cm_Y/imagen_resolucion_Y)] 

    Z4centroX = int(7*Z1centroX)
    Z4centroY = int(Z1centroY)
    
    coordenadasZona4[0] =[Z4centroX*(ROI_cm_X/imagen_resolucion_X),Z4centroY*(ROI_cm_Y/imagen_resolucion_Y)] 

    Z5centroX = int(Z1centroX)
    Z5centroY = int(3*Z1centroY)
    coordenadasZona5[0] =[Z5centroX*(ROI_cm_X/imagen_resolucion_X),Z5centroY*(ROI_cm_Y/imagen_resolucion_Y)] 
    
    Z6centroX = int(3*Z1centroX)
    Z6centroY = int(3*Z1centroY)
    coordenadasZona6[0] =[Z6centroX*(ROI_cm_X/imagen_resolucion_X),Z6centroY*(ROI_cm_Y/imagen_resolucion_Y)] 

    Z7centroX = int(5*Z1centroX)
    Z7centroY = int(3*Z1centroY)
    coordenadasZona7[0] =[Z7centroX*(ROI_cm_X/imagen_resolucion_X),Z7centroY*(ROI_cm_Y/imagen_resolucion_Y)] 

    Z8centroX = int(7*Z1centroX)
    Z8centroY = int(3*Z1centroY)
    coordenadasZona8[0] =[Z8centroX*(ROI_cm_X/imagen_resolucion_X),Z8centroY*(ROI_cm_Y/imagen_resolucion_Y)] 

    Z9centroX = int(Z1centroX)
    Z9centroY = int(5*Z1centroY)
    coordenadasZona9[0] =[Z9centroX*(ROI_cm_X/imagen_resolucion_X),Z9centroY*(ROI_cm_Y/imagen_resolucion_Y)] 

    Z10centroX = int(3*Z1centroX)
    Z10centroY = int(5*Z1centroY)
    coordenadasZona10[0] =[Z10centroX*(ROI_cm_X/imagen_resolucion_X),Z10centroY*(ROI_cm_Y/imagen_resolucion_Y)] 

    Z11centroX = int(5*Z1centroX)
    Z11centroY = int(5*Z1centroY)
    coordenadasZona11[0] =[Z11centroX*(ROI_cm_X/imagen_resolucion_X),Z11centroY*(ROI_cm_Y/imagen_resolucion_Y)] 

    Z12centroX = int(7*Z1centroX)
    Z12centroY = int(5*Z1centroY)
    coordenadasZona12[0] =[Z12centroX*(ROI_cm_X/imagen_resolucion_X),Z12centroY*(ROI_cm_Y/imagen_resolucion_Y)] 


    coordenadasZonaTotal = [[Z1centroX,Z1centroY],[Z2centroX,Z2centroY],[Z3centroX,Z3centroY],[Z4centroX,Z4centroY],
    [Z5centroX,Z5centroY],[Z6centroX,Z6centroY],[Z7centroX,Z7centroY],[Z8centroX,Z8centroY],[Z9centroX,Z9centroY],
    [Z10centroX,Z10centroY],[Z11centroX,Z11centroY],[Z12centroX,Z12centroY],]

    with mp_hands.Hands(
        static_image_mode = False,
        max_num_hands     = 1) as hands:
        while True:
            ret,frame = cap.read()
            frame = cv2.resize(frame,(imagen_resolucion_X, imagen_resolucion_Y))
            # frame = cv2.flip(frame,1)
            cTime =  time.time()
            fps = 1/(cTime-pTime)
            pTime = cTime
            if ret == False:break
            height, width, _ =  frame.shape
            if detector == False:
                puntos = detector_espacioT(frame)
            if detector == True :





                coordenadas_centroAmarillo = []
                coordenadas_actualesAmarillo = []
                objetos_amarillos = []
                coordenadas_centroAzules = []
                coordenadas_actualesAzules = []
                # objetos_azules = []
                coordenadas_centroVerdes = []
                coordenadas_actualesVerdes = []
                # objetos_verdes = []
                VcubosAC = []
                zonaCubosAzules = []
                zonaCubosVerdes = []

                pts1 = np.float32([puntos[0],puntos[1],puntos[2],puntos[3]])
                pts2 = np.float32([[0,0],[640,0],[0,480],[640,480]])
                M = cv2.getPerspectiveTransform(pts1,pts2)
                dst = cv2.warpPerspective(frame,M,(640,480))
                dst = cv2.flip(dst,1)
                frameHSV = cv2.cvtColor(dst,cv2.COLOR_BGR2HSV)
                mascaraRoja = cv2.imread('maskroja.png')
                cv2.circle(mascaraRoja,(cx,cy),24,(255,255,255), -1)
                cv2.imshow('maskroja',mascaraRoja)
                pts1Primo = np.float32([puntos[0],puntos[1],puntos[2],puntos[3]])
                pts2Primo = np.float32([[0,0],[640,0],[0,480],[640,480]])
                MPrimo = cv2.getPerspectiveTransform(pts1Primo,pts2Primo)
                dst2 = cv2.warpPerspective(mascaraRoja,MPrimo,(640,480))
                dst2 = cv2.flip(dst2,1)
                gray = cv2.cvtColor(dst2,cv2.COLOR_BGR2GRAY)
                _,th = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
                contorno3,hierarchy1 = cv2.findContours(th, cv2.RETR_EXTERNAL,
                          cv2.CHAIN_APPROX_NONE)
                cv2.drawContours(dst, contorno3, -1, (0,255,0), 3)

                for c in contorno3:    
                    area = cv2.contourArea(c)
                    if area > 1000:   
                        M = cv2.moments(c)
                        if (M['m00']) == 0:
                            M['m00'] = 1
                        cxPrima = int(M['m10']/M['m00'])
                        CyPrima = int(M['m01']/M['m00'])
                        cv2.circle(dst,(cxPrima,CyPrima),7,(0,255,0),-1)
                        font = cv2.FONT_ITALIC
                        cv2.putText(dst,'{},{}'.format('%.2f'%(cxPrima*(ROI_cm_X/imagen_resolucion_X)),'%.2f'%(CyPrima*(ROI_cm_Y/imagen_resolucion_Y))),(cxPrima,CyPrima+50),font,0.5,(0,0,255),
                                    2,cv2.LINE_AA)
                        # coordenadas_actualesAzules.append([x,y])
                        # ID_Azul = len(coordenadas_actualesAzules)
                
                cv2.imshow("dst2",dst2)
                mascaraRoja = cv2.imread('maskroja.png')
                procesamiento(frameHSV,dst)
                gestos(frame,hands,dst)
            

                cv2.line(dst,(int(imagen_resolucion_X/4),0),(int(imagen_resolucion_X/4),imagen_resolucion_Y),(0,0,255),2)
                cv2.line(dst,(int(2*(imagen_resolucion_X/4)),0),(int(2*(imagen_resolucion_X/4)),imagen_resolucion_Y),(0,0,255),2)
                cv2.line(dst,(int(3*(imagen_resolucion_X/4)),0),(int(3*(imagen_resolucion_X/4)),imagen_resolucion_Y),(0,0,255),2)
                
                
                cv2.line(dst,(0,int(imagen_resolucion_Y/3)),(imagen_resolucion_X,int(imagen_resolucion_Y/3)),(0,0,255),2)
                cv2.line(dst,(0,int(2*(imagen_resolucion_Y/3))),(imagen_resolucion_X,int(2*(imagen_resolucion_Y/3))),(0,0,255),2)
                cv2.line(dst,(0,int(3*(imagen_resolucion_Y/3))),(imagen_resolucion_X,int(3*(imagen_resolucion_Y/3))),(0,0,255),2)

                
                # cv2.circle(dst,(Z1centroX,Z1centroY),7,(255,255,0),-1)
                cv2.putText(dst,'Z1',(Z1centroX-75,Z1centroY-50),cv2.FONT_ITALIC,0.8,(0,0,0),2,cv2.LINE_AA)

                # cv2.circle(dst,(Z2centroX,Z2centroY),7,(255,255,0),-1)
                cv2.putText(dst,'Z2',(Z2centroX-75,Z2centroY-50),cv2.FONT_ITALIC,0.8,(0,0,0),2,cv2.LINE_AA)

                # cv2.circle(dst,(Z3centroX,Z3centroY),7,(255,255,0),-1)
                cv2.putText(dst,'Z3',(Z3centroX-75,Z3centroY-50),cv2.FONT_ITALIC,0.8,(0,0,0),2,cv2.LINE_AA)
                
                # cv2.circle(dst,(Z4centroX,Z4centroY),7,(255,255,0),-1)
                cv2.putText(dst,'Z4',(Z4centroX-75,Z4centroY-50),cv2.FONT_ITALIC,0.8,(0,0,0),2,cv2.LINE_AA)
                
                # cv2.circle(dst,(Z5centroX,Z5centroY),7,(255,255,0),-1)
                cv2.putText(dst,'Z5',(Z5centroX-75,Z5centroY-50),cv2.FONT_ITALIC,0.8,(0,0,0),2,cv2.LINE_AA)
                
                # cv2.circle(dst,(Z6centroX,Z6centroY),7,(255,255,0),-1)
                cv2.putText(dst,'Z6',(Z6centroX-75,Z6centroY-50),cv2.FONT_ITALIC,0.8,(0,0,0),2,cv2.LINE_AA)

                # cv2.circle(dst,(Z7centroX,Z7centroY),7,(255,255,0),-1)
                cv2.putText(dst,'Z7',(Z7centroX-75,Z7centroY-50),cv2.FONT_ITALIC,0.8,(0,0,0),2,cv2.LINE_AA)
                
                # cv2.circle(dst,(Z8centroX,Z8centroY),7,(255,255,0),-1)
                cv2.putText(dst,'Z8',(Z8centroX-75,Z8centroY-50),cv2.FONT_ITALIC,0.8,(0,0,0),2,cv2.LINE_AA)
               
                # cv2.circle(dst,(Z9centroX,Z9centroY),7,(255,255,0),-1)
                cv2.putText(dst,'Z9',(Z9centroX-75,Z9centroY-50),cv2.FONT_ITALIC,0.8,(0,0,0),2,cv2.LINE_AA)
               
                # cv2.circle(dst,(Z10centroX,Z10centroY),7,(255,255,0),-1)
                cv2.putText(dst,'Z10',(Z10centroX-75,Z10centroY-50),cv2.FONT_ITALIC,0.8,(0,0,0),2,cv2.LINE_AA)
               
                # cv2.circle(dst,(Z11centroX,Z11centroY),7,(255,255,0),-1)
                cv2.putText(dst,'Z11',(Z11centroX-75,Z11centroY-50),cv2.FONT_ITALIC,0.8,(0,0,0),2,cv2.LINE_AA)

                # cv2.circle(dst,(Z12centroX,Z12centroY),7,(255,255,0),-1)
                cv2.putText(dst,'Z12',(Z12centroX-75,Z12centroY-50),cv2.FONT_ITALIC,0.8,(0,0,0),2,cv2.LINE_AA)
                # !AQUI SE CAMBIARION COSAS

                # señalCambio[0]=1
                # ZonasGuardadasAzules = cambioPosicion(zonaCubosAzules,zonasActualesAzules,ZonasGuardadasAzules)
                # señalCambio[0]=1
                # ZonasGuardadasVerdes = cambioPosicion(zonaCubosVerdes,zonasActualesVerdes,ZonasGuardadasVerdes)
                # correctorCoordenadas()
                # correctorCoordenadas(coordenadas_actualesAzules,coordenadasObjetosAzules,ZonasGuardadasAzules,objetos_azules)
                # correctorCoordenadas(coordenadas_actualesVerdes,coordenadasObjetosVerdes,ZonasGuardadasVerdes,objetos_verdes)
                # print('las coordenadas en cm azules son ',objetos_azules)
                # print('las coordenadas en cm verdes son ',objetos_verdes)
                # print('Estas son las zonas Actuales',zonasActuales)
                # print('Estas son las zonas guardadas',ZonasGuardadas)
                # Cubo 0
                # cv2.putText(dst,'.',(161,368),cv2.FONT_HERSHEY_PLAIN,2,(0,255,255),3)
                # cv2.putText(dst,'*',(220, 368),cv2.FONT_HERSHEY_PLAIN,2,(0,255,255),3)
                # # Cubo1
                # cv2.putText(dst,'.',(218, 314),cv2.FONT_HERSHEY_PLAIN,2,(0,255,255),3)
                # cv2.putText(dst,'*',(227, 209),cv2.FONT_HERSHEY_PLAIN,2,(0,255,255),3)
                # # Cubo2
                # cv2.putText(dst,'.',(411, 237),cv2.FONT_HERSHEY_PLAIN,2,(0,255,255),3)
                # cv2.putText(dst,'*',(426, 242),cv2.FONT_HERSHEY_PLAIN,2,(0,255,255),3)

                #!AQUI SE ACABARON LAS COSAS NUEVAS

                cv2.imshow("dst",dst)
        

            cv2.putText(frame,f'Azul: {len(coordenadas_actualesAzules)}',(0,50),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),3)
            cv2.putText(frame,f'Verde: {len(coordenadas_actualesVerdes)}',(0,80),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),3)
            cv2.putText(frame,f'Objetos: {len(coordenadas_actualesAzules)+len(coordenadas_actualesVerdes)}',(0,110),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),3)
            cv2.putText(frame,f'FPS: {int(fps)}',(400,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)
            cv2.imshow("Frame",frame)


            k = cv2.waitKey(1) & 0xFF
            if k == ord('n'):
                cv2.destroyWindow('dst')
                break

        cap.release()
        cv2.destroyAllWindows()

# visualizador(cap,imagen_resolucion_X,imagen_resolucion_Y)
# visualizador()