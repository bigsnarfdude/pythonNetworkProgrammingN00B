'''
Basic python web page getter using sockets
'''


import sys
import socket 
from urlparse import urlparse
from urlparse import urlunparse

url = 'http://www.rfc-editor.org/rfc-index.html'
port = url_convert_port(url)
host = url_convert_host(url)
filename = url_convert_filename(url)

def url_convert_port(host):
    parsed_url = urlparse(host)
    port = socket.getservbyname(parsed_url.scheme)
    return port

def url_convert_host(host):
    parsed_url = urlparse(host)
    host = parsed_url.netloc
    return host

def url_convert_filename(host):
    parsed_url = urlparse(host)
    filename = parsed_url.path
    return filename

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
c.connect((host, port)) 
file_object = c.makefile('r', 0)
file_object.write("GET "+filename+" HTTP/1.0\n\n") 

buffer = file_object.readlines() 
for line in buffer: 
    print line
