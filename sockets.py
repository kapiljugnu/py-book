# using socket to read a file with http protocol

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()

mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1 :
        break
    print(data.decode())

mysock.close()


# Http request in python using urllib

from urllib import request, parse, error

fhand = request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
