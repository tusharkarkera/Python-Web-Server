from socket import *
import os
serverSocket = socket(AF_INET, SOCK_STREAM)     #create a socket

#Prepare server socket
serverPort = 7000
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
#full_path = os.path.realpath(__file__)         
#print(os.path.dirname(full_path))               

while True:
    print 'Ready to serve . . .'
    connectionSocket, addr = serverSocket.accept()  #create socket for client
    try:
        message =connectionSocket.recv(1024)   #receive message from client
        print message
        filename = message.split()[1]
        #print(filename)
        url = filename.split(".")

        if len(url) != 2:
            temUrl = filename.split("%20")      #handle folder name with a space
            finalUrl = ""
            for temStr in temUrl:
                #print temStr
                finalUrl = finalUrl+temStr+" "

            finalUrl = finalUrl[:-1]
            #print(finalUrl)
            resp = [
                '<html><body>',
                '<p> <h1>Directory listing </h1></p>',
                '<ul>',
            ]              
            for file in os.listdir('.'+finalUrl):
                resp.append('<li><a href="/'+file+'">' + file + '</a></li>')
            resp.append('</ul></body></html>')
            response_body = ''.join(resp)
            
            connectionSocket.send('\r\n')
            connectionSocket.send(response_body)
            connectionSocket.close()
        
        else:
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