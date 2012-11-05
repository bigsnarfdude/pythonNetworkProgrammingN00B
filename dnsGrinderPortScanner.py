#!/usr/bin/env python

'''
Program takes a file of dns names and grinds out the values and then connects up to the server via port 80,443, 8080 and validates TCP connectivity
'''

import socket
import string
import random

digits = string.lowercase + string.uppercase + string.digits
#gen_random_hosts_8_char_long = (''.join(random.sample(digits, 8)) for _ in range(1000000))

ip_list = []
ports_list = [ 80, 443, 8080 ]
host_dns_list = [ 'homer','www','www1','test','www2' ]
domain = 'example.com'
targets = [ host + '.' + domain for host in host_dns_list ]
#grinder_targets = [ host + '.' + domain for host in gen_random_hosts_8_char_long ]


def scan_host(address, port): 
    s = socket.socket() 
    print "Attempting to connect to %s on port %s." %(address, port) 
    try: 
        s.connect((address, port)) 
        print "Connected to server %s on port %s." %(address, port) 
        return True 
    except socket.error, msg: 
        print "Connecting to %s on port %s failed with the following error: %s" %(address, port, msg) 
        return False


for host in targets:
    try:                                      
        print host, socket.gethostbyname(host)
        ip_address = socket.gethostbyname(host)
        print ip_address
        ip_list.append(ip_address)
    except socket.error, msg:
        print '%s : %s' % (host, msg)

for scan in ip_list:
    for port in ports_list:
        try:
            print scan_host(scan, port)
        except:
            print "blah blah blah"

