import time
import comunicacionUR3 as COM
import socket

def move(x,y,z):
  #print(receive())
  #time.sleep(1)
  punto= COM.receive()
  curve=['p','x','y','z','Rx','Ry','Rz', 3, 3]
  curve[1]=punto[0]+x*0.01       # BACK (-x) FRONT (+x)  convierte a milimetros
  curve[2]=punto[1]+y*0.01       # RIGHT (+y) LEFT (-y)
  curve[3]=punto[2]+z*0.01       # UP (+z) DOWN (-z)
  curve[4]=punto[3]       # 1° = 0.017444444
  curve[5]=punto[4]
  curve[6]=punto[5]
  
  if ( curve[1]<0.100 or curve[1]>0.999 or curve[2]<-0.292 or curve[2]>0.999 or curve[3]>0.999 ):
    print("El punto solicitado está por fuera del área de trabajo, por favor ingresar un movimiento dentro del área de trabajo")
  else:
    COM.transmis_move(curve.copy())
    time.sleep(2)
    curve = COM.receive()
    # if ( round(punto[0],3) == round(curve[0],3) and round(punto[1],3) == round(curve[1],3) and round(punto[2],3) == round(curve[2],3) ):
    #   print("Movimiento inválido, por favor ingresar un movimiento válido")
    

def open_Gripper():
  HOST = "192.168.0.112" # The UR IP address
  PORT = 30002 # UR secondary client
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT))

  f = open ("Gripper.open", "rb")   #Robotiq Gripper

  l = f.read(1024)
  while (l):
      s.send(l)
      l = f.read(1024)
  s.close()

def close_Gripper():
  HOST = "192.168.0.112" # The UR IP address
  PORT = 30002 # UR secondary client
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT))

  f = open ("Gripper.close", "rb")   #Robotiq Gripper

  l = f.read(1024)
  while (l):
      s.send(l)
      l = f.read(1024)
  s.close()

def half_Gripper():
  HOST = "192.168.0.112" # The UR IP address
  PORT = 30002 # UR secondary client
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT))

  f = open ("Gripper.half", "rb")   #Robotiq Gripper

  l = f.read(1024)
  while (l):
      s.send(l)
      l = f.read(1024)
  s.close()

def activate_Gripper():
  HOST = "192.168.0.112" # The UR IP address
  PORT = 30002 # UR secondary client
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT))

  f = open ("Gripper.activate", "rb")   #Robotiq Gripper

  l = f.read(1024)
  while (l):
      s.send(l)
      l = f.read(1024)
  s.close()

