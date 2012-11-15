import select
import socket
import sys

HOST = ''
PORT = 8888
backlog =5
size=1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind ((HOST, PORT))
server.listen(backlog)
input = [server, sys.stdin]
running = 1

while running:
    inputready, outputready, exceptready = select.select(input, [],[]) # select dumps in 3
    
    for s in inputready:

        if s == server:
            client, address = server.accept()
            input.append(client)

        elif s == sys.stdin:
            junk = sys.stdin.readline()
            running = 0

        else:
            data = s.recv(size)
            if data:
                print data
                s.send('server: ' + data)
            else:
                s.close()
                input.remove(s)

server.close()

