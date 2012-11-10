#!/usr/bin/env python
# Copyright (c) 2003 CORE Security Technologies
# original author $Id: sniffer.py 17 2003-10-27 17:36:57Z jkohen $
# Simple packet sniffer.
# modified to work on my box with sudo ipython

from select import select
import socket
import sys

import impacket
from impacket import ImpactDecoder

DEFAULT_PROTOCOLS = ('icmp', 'tcp', 'udp')

toListen = DEFAULT_PROTOCOLS
sockets = []
for protocol in toListen:
	try:
		protocol_num = socket.getprotobyname(protocol)
	except socket.error:
		print "Ignoring unknown protocol:", protocol
		toListen.remove(protocol)
		continue
	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, protocol_num)
	s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
	sockets.append(s)

decoder = ImpactDecoder.IPDecoder()

while len(sockets) > 0:
	ready = select(sockets, [], [])[0]
	for s in ready:
		packet = s.recvfrom(4096)[0]
		if 0 == len(packet):
			sockets.remove(s)
			s.close()
		else:
			packet = decoder.decode(packet)
			print packet
