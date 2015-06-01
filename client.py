from socket import *

clientsocket = socket(AF_INET, SOCK_STREAM)     #create a socket
clientsocket.connect(('', 7000))
clientsocket.send('hello, this is a test string')