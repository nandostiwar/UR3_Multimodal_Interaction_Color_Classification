    
import comunicacionUR3 as COM
import controlUR3 as UR3
import time

def movimientoInicial():
    posInicial = ['a', 0, -1.57, -1.57, -1.57, 1.57, 1.57*2, 1, 1] 
    COM.transmis_move(posInicial) 
    time.sleep(2)
    UR3.move(0,-4,0)
    time.sleep(2)
    UR3.move(0,0,-5)
    time.sleep(2)
    UR3.move(-3,0,0)
    time.sleep(2)
    UR3.activate_Gripper()
    UR3.close_Gripper()
    UR3.open_Gripper()

def desplazar(objetos,desplazamientoX,desplazamientoY):
    # Posicionamiento sobre el objeto
    UR3.move(objetos[1],objetos[0],0)
    # Baja y toma el objeto
    UR3.move(0,0,-11)
    UR3.close_Gripper()
    # Sube con el cubo tomado
    UR3.move(0,0,11)
    # Se desplaza el cubo lo indicado por el usuario
    UR3.move(desplazamientoX,desplazamientoY,0)
    # Baja y deja el cubo en la posicion indicada
    UR3.move(0,0,-11)
    UR3.open_Gripper()
    # Sube sin el cubo
    UR3.move(0,0,11)
    # vuelve al HOME
    xHome = objetos[1]+desplazamientoX
    yHome= objetos[0]+desplazamientoY
    UR3.move(-xHome,-yHome,0)




