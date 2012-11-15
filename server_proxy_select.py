import select
import socket
import sys
import urllib2

HOST = ''
PORT = 8888
backlog = 5
size = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind ((HOST, PORT))
server.listen(backlog)
input = [server, sys.stdin]
running = 1


def get_webpage(url):
    result = urllib2.urlopen(url).read()
    return result

while running:
    inputready, outputready, exceptready = select.select(input, [],[]) 
    
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
                if "http://" in data:
                    url = data.strip()
                    data_to_client = get_webpage(url)
                    s.send(data_to_client)
            else:
                s.close()
                input.remove(s)

server.close()
