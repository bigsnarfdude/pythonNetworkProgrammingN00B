'''
Program to parse URL's and obtain ports
'''

import socket
from urlparse import urlparse

url_list = [    'http://www.example.com',
                'https://www.example.com',
                'ftp://ftp.example.com',
                'gopher://gopher.example.com',
                'smtp://mail.example.com',
                'imap://mail.example.com',
                'imaps://mail.example.com',
                'pop3://pop.example.com',
                'pop3s://pop.example.com',]

def url_convert_port(host):
    parsed_url = urlparse(host)
    port = socket.getservbyname(parsed_url.scheme)
    print parsed_url, port
    return port

print [ url_convert_port(host) for host in url_list ]


