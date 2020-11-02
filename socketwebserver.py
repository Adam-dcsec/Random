#!/usr/bin/python3

import socket
import sys
import os
import glob
import re
 

HOST = '' 
PORT = 8080 
#path = '/root/Desktop/Scripts/testpad'

test = 'index.html'

def walk(fileToBeServed):
#def walk():
    os.chdir("/var/www/html")
    for root, dirs, files in os.walk(".", topdown = False):
       for name in files:
          files = os.path.join(root, name)
          matchedFile = re.findall(r"./" + fileToBeServed, files, flags=re.IGNORECASE)
          if matchedFile:
               for i in matchedFile:
                    print(i)
          #print(files)
   #for name in dirs:
      #print(os.path.join(root, name))
      
walk(test)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((HOST, PORT))
#except socket.error as msg:
    #print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    #sys.exit()
	
print('Socket bind complete')


#print('Connected with ' + addr[0] + ':' + str(addr[1]))

#directory = os.listdir()
#print(directory)

#fileserved = open(path, 'r')
#content = fileserved.read()
#print(content.split()[1])




while True:
    #After every closed connection you need to relisten and reaccept any connection but you DONT NEED TO RELISTEN ON YOUR PORT OR YOU WILL GET ADDRESS IN USE ERRORS REEEEEEEE
    serversocket.listen(10)
    conn, addr = serversocket.accept()
      
    #Assigning data to the connection recieved
    #data = conn.recv(1024)
    #data
    #conn.recv(1024)
    s = conn.recv(1024)
    ss = s.split()[1]
    serveMe = '.' + ss.decode("utf-8")
    print(serveMe)
    
    conn.sendall(b'HTTP/1.1 200 OK\n')
    conn.sendall(b'Server: test\n')
    conn.sendall(b'Content-Type: text/html\n')
    conn.sendall(b'\n')
    #conn.sendall(ss.encode())
    #conn.sendall(b'HTTP/1.1 200 OK\n')
    #conn.sendall(b'Server: test\n')
    #conn.sendall(b'Content-Type: text/html\n')
    #conn.sendall(b'\n')
    #Sending back the data that was recieved
    #conn.sendall(content.encode())
    conn.close()
