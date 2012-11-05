#!/usr/bin/env python

'''
Program takes a file of dns names and grinds out the values
'''

import socket
import string
import random

digits = string.lowercase + string.uppercase + string.digits
gen_random_hosts_8_char_long = (''.join(random.sample(digits, 8)) for _ in range(1000000))

host_dns_list = ['homer','www','www1','test','www2']
domain = 'example.com'
targets = [ host + '.' + domain for host in host_dns_list ]
grinder_targets = [ host + '.' + domain for host in gen_random_hosts_8_char_long ]


for host in targets:
    try:                                      
        print host, socket.gethostbyname(host)
    except socket.error, msg:
        print '%s : %s' % (host, msg)
