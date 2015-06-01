from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)     #create a socket

#Prepare server socket
serverPort = 7000
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:
        print buf
        break