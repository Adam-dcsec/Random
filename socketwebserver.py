#!/usr/bin/python3

import socket
import os
 

HOST = '' 
PORT = 8080 

#test = 'index.html'

#Function that dirwalks recursively and sends content based on if file was found not
def walkSend(fileToBeServed):
    found = False
    os.chdir("/var/www/html")
    for root, dirs, files in os.walk(".", topdown = False):
       for name in files:
          #print(name)
          if os.path.join(root, name) == '.' + fileToBeServed:
          #File has been found so serving it up
              #print('it works')
              found = True 
              fileserved = open('/var/www/html' + fileToBeServed, 'r')
              content = fileserved.read()
              conn.sendall(b'HTTP/1.1 200 OK\n')
              conn.sendall(b'Server: test\n')
              conn.sendall(b'Content-Type: text/html\n')
              conn.sendall(b'\n')
              conn.sendall(content.encode())   
          else:
              continue
    if not found:
    #Sending 404 Page because resource was not found
        conn.sendall(b'HTTP/1.1 404 OK\n')
        conn.sendall(b'Server: test\n')
        conn.sendall(b'Content-Type: text/html\n')
        conn.sendall(b'\n')
        conn.sendall(b'no dawg')
        #print("404")

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((HOST, PORT))
#except socket.error as msg:
    #print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    #sys.exit()
	
print('Socket bind complete')


#print('Connected with ' + addr[0] + ':' + str(addr[1]))

while True:
    #After every closed connection you need to relisten and reaccept any connection but you DONT NEED TO RELISTEN ON YOUR PORT OR YOU WILL GET ADDRESS IN USE ERRORS REEEEEEEE
    serversocket.listen(10)
    conn, addr = serversocket.accept()
      
    #Assigning data to the connection recieved
    s = conn.recv(1024)
    
    #Finding what is requested
    ss = s.split()[1]
    serveMe = ss.decode("utf-8")
    print(serveMe)
    
    #Running function to serve content
    walkSend(serveMe)
    
    #close connection
    conn.close()
