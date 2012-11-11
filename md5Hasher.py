'''
file hasher for md5 of all file

The Malware Hash Registry (MHR) project is a look-up service similar to the Team Cymru IP address to ASN mapping project. This project differs however, in that you can query our service for a computed MD5 or SHA-1 hash of a file and, if it is malware and we know about it, we return the last time we've seen it along with an approximate anti-virus detection percentage
'''

import os
import hashlib
import sys
import socket
import string


for root, dir, files in os.walk(str(sys.argv[1])):
    for fp in files:
        try:
            fn = root+fp
            infile = open(fn, "rb")
            content = infile.read()
            infile.close()
            m = hashlib.md5()
            m.update(content)
            hash = m.hexdigest()
            mhr = socket.socket(socket.AF_INET,\    
                                            socket.SOCK_STREAM)
            mhr.connect(("server", 43))
            mhr.send(str(hash + "\r\n"))
            response = ''
            while True:
                d = mhr.recv(4096)
                response += d
                if d == '':
                    break
                if "NO_DATA" not in response:
                    print "<INFECTED>:"+str(fn)
        except:
            pass
