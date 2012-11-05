#!/usr/bin/env python

"""
An echo server that uses select to handle multiple clients at a time.
Entering any line of input at the terminal will exit the server.
"""

import select
import socket
import sys
import time
import commands

host = '127.0.0.1'
port = 23454
backlog = 5
size = 1024
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)
input = [server,sys.stdin]
running = 1
while running:
# while answer != 'quit':

    inputready,outputready,exceptready = select.select(input,[],[])

    for s in inputready:

        if s == server:
            # handle the server socket
            client, address = server.accept()
            input.append(client)

        elif s == sys.stdin:
            # handle standard input
            junk = sys.stdin.readline()
            running = 0 

        else:
            # handle all other sockets
            data = s.recv(size)
            if data:
                s.send(data)
                commands.getstatusoutput('say -v Zarvox %s' % ''.join(data))
                time.sleep(0.5)
                print data
            else:
                s.close()
                input.remove(s)

server.close()
