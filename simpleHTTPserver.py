#!/usr/bin/env python

import socket  
import signal 
import time  

class Server:

    def __init__(self, port=8888):
        self.host = ''  
        self.port = port
        self.www_directory = 'www' 

    def activate_server(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self._wait_for_connections()

    def shutdown(self):
        s.socket.shutdown(socket.SHUT_RDWR)

    def _generate_headers(self, code):
        h = ''
        if (code == 200):
            h = 'HTTP/1.1 200 OK\n'
        elif(code == 404):
            h = 'HTTP/1.1 404 Not Found\n'
        current_date = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        h += 'Date: ' + current_date +'\n'
        h += 'Server: Crap-Server\n'
        h += 'Connection: close\n\n'  
        return h

    def _wait_for_connections(self):
        while True:
            print "Awaiting Victims\n\n"
            self.socket.listen(1)

            conn, addr = self.socket.accept()
            print "Got connection from: ", addr
            print "*********************************************"
            data = conn.recv(1024)
            string = bytes.decode(data)

            request_method = string.split(' ')[0]
            print "Method: ", request_method
            print "Request body: ", string

            if (request_method == 'GET') | (request_method == 'HEAD'):
                file_requested = string.split(' ')
                file_requested = file_requested[1]

                file_requested = file_requested.split('?')[0]

                if (file_requested == '/'):
                    file_requested = '/index.html'

                file_requested = self.www_directory + file_requested
                print "Serving web page [",file_requested,"]"

                try:
                    file_handler = open(file_requested,'rb')
                    if (request_method == 'GET'):
                        response_content = file_handler.read()
                    file_handler.close()

                    response_headers = self._generate_headers( 200)

                except Exception as e: #in case file was not found, generate 404 page
                    print "Warning, file not found. Serving response code 404\n", e
                    response_headers = self._generate_headers( 404)

                    if (request_method == 'GET'):
                        response_content = b"<html><body><p>Error 404: File not found</p><p>Vincent's Crap HTTP server</p></body></html>"

                server_response =  response_headers.encode()
                if (request_method == 'GET'):
                    server_response +=  response_content

                conn.send(server_response)
                print "Closing connection with client"
                conn.close()

        else:
            print "Unknown HTTP request method:", request_method

def graceful_shutdown(sig, dummy):
    s.shutdown()
    import sys
    sys.exit(1)

signal.signal(signal.SIGINT, graceful_shutdown)
print "Starting web server\n\n"

s = Server(8888)
s.activate_server()
