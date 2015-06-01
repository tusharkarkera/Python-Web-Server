from socket import *
import os
serverSocket = socket(AF_INET, SOCK_STREAM)     #create a socket

#Prepare server socket
serverPort = 7000
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

while True:
    print 'Ready to serve . . .'
    connectionSocket, addr = serverSocket.accept()  #create socket for client
    try:
        message =connectionSocket.recv(1024)   #receive message from client
        print message
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata =f.read()
        #Send contents of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
        print 'File Received'
    except IOError:
        connectionSocket.send('\n404 File Not Found\n')
        connectionSocket.close()
serverSocket.close()