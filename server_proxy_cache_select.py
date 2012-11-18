import select
import socket
import sys
import urllib2

HOST = ''
PORT = 8888
BACKLOG = 5
SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(BACKLOG)
input = [server, sys.stdin]
running = True

cache = {}


def get_webpage(url):
    result = urllib2.urlopen(url).read()
    cache[url] = result

    return result

while running: # simple select reactor
    inputready, outputready, exceptready = select.select(input, [], [])

    for s in inputready:

        if s == server:
            client, address = server.accept()
            input.append(client)

        elif s == sys.stdin:
            junk = sys.stdin.readline()
            running = False

        else:
            data = s.recv(SIZE)
            if data and data.startswith("http://"):
                url = data.strip()
                if url in cache:
                    print "fetched from cache"
                    data_to_client = cache[url]
                else:
                    print "going to the interweb"
                    data_to_client = get_webpage(url)
                    s.send(data_to_client)
            else:
                s.close()
                input.remove(s)

server.close()
