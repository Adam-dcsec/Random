#!/usr/bin/python3
#InProgress

import socket
import sys
 
HOST = '' 
PORT = 8080 

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
    data = conn.recv(1024)
    #Sending back the data that was recieved
    conn.send(data)
    conn.close()
    #serversocket.close()
    #serversocket.listen(10)
    if not data:
        break
    conn.sendall(data)
    #serversocket.close()
