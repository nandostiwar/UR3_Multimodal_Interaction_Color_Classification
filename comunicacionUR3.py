import socket 
import struct
import codecs
import time
pose =[0]
def transmission_f(instruction):
      # -*- coding: utf-8 -*-
  # Echo client program
  #HOST = "192.168.0.100" # ip del robot
  HOST = "192.168.0.112" # ip del robot
  PORT = 30002 # puerto en el que el robot recibe
  PORT_30003 = 30003
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #crear un socket
  s.connect((HOST, PORT)) #iniciar la comunicacion

  co =  str.encode(instruction)+b"\n"
  s.send (co)
  data = s.recv(1024)
  s.close()

def transmission(instruction):
  transmission_f(instruction)
  #print(instruction)

def transmis_move(pos):

  """
  https://matthew-brett.github.io/teaching/string_formatting.html
  """
  if isinstance(pos,list):
    if (pos[0] != 'p'):
      string="movej([{},{},{},{},{},{}],a={},v={})".format(pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8])
    else:
      string="movej(p[{},{},{},{},{},{}],a={},v={})".format(pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8])
    transmission(string)
    pose[0]=string
  else: return pose
  


def receive_f():
  # -*- coding: utf-8 -*-
  # Echo client program
  HOST = "192.168.0.112" # ip del robot
  PORT = 30002 # puerto en el que el robot recibe
  PORT_30003 = 30003
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #crear un socket
  s.connect((HOST, PORT)) #iniciar la comunicacion
  count = 0
  home_status = 0
  program_run = 0
  while (count<1):
    if program_run == 0:
      try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        s.connect((HOST, PORT_30003))
        time.sleep(1.00)
        #print ""
        packet_1 = s.recv(4)
        packet_2 = s.recv(8)
        packet_3 = s.recv(48)
        packet_4 = s.recv(48)
        packet_5 = s.recv(48)
        packet_6 = s.recv(48)
        packet_7 = s.recv(48) 
        packet_8 = s.recv(48)
        packet_9 = s.recv(48)
        packet_10 = s.recv(48)
        packet_11 = s.recv(48)
        
        packet_12 = s.recv(8)
        x = struct.unpack('!d',packet_12)[0]
        #print ("X = ", x * 1000)
        
        packet_13 = s.recv(8)
        y = struct.unpack('!d', packet_13)[0]
        #print ("Y = ", y * 1000)
        
        packet_14 = s.recv(8)
        z = struct.unpack('!d', packet_14)[0]
        #print ("Z = ", z * 1000)
        
        packet_15 = s.recv(8)
        Rx = struct.unpack('!d', packet_15)[0]
        #print ("Rx = ", Rx)
        
        packet_16 = s.recv(8)
        Ry = struct.unpack('!d', packet_16)[0]
        #print ("Ry = ", Ry)
        
        packet_17 = s.recv(8)
        Rz = struct.unpack('!d', packet_17)[0]
        #print ("Rz = ", Rz)
        
        home_status = 1
        program_run = 0
        s.close()
      except socket.error as socketerror:
        print("Error: ", socketerror)
      #print ("received{count}: \t x={x},y={y},z={z},Rx={Rx},Ry={Ry},Rz={Rz}")
      count=count+1
  return [x,y,z,Rx,Ry,Rz]

def receive():
  return receive_f() #unquote for real receive
