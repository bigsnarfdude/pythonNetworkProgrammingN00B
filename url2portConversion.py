'''
Program to parse URL's and obtain ports
'''

import socket
from urlparse import urlparse
from urlparse import urlunparse

url_list = [    'http://www.example.com',
                'https://www.example.com',
                'ftp://ftp.example.com',
                'gopher://gopher.example.com',
                'smtp://mail.example.com',
                'imap://mail.example.com',
                'imaps://mail.example.com',
                'pop3://pop.example.com',
                'pop3s://pop.example.com',]

ports_list = [ 80, 443, 21, 70, 25, 143, 993, 995 ]
domain = 'example.com'

def url_convert_port(host):
    parsed_url = urlparse(host)
    port = socket.getservbyname(parsed_url.scheme)
    print parsed_url, port
    return port

def port_convert_url(port, domain):
    return urlunparse((socket.getservbyport(port), domain,'/','','',''))

print [ url_convert_port(host) for host in url_list ]
print [ port_convert_url(port, domain) for port in ports_list ]





