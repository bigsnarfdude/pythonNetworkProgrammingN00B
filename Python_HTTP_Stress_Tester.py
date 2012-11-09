#!/usr/bin/env python
# -*- coding: utf-8 -*-

# I am not responsible for what you do with this application
# Yo no soy responsable de lo que haces con esta aplicación
# je ne suis pas responsable de ce que vous faites avec cette application.
# USE ON YOUR OWN RISK.
# WITH NO ANY EXPRESS OR IMPLIED WARRANTIES
# EMPLOI SUR VOS PROPRES RISQUES.
# SANS AUCUNE GARANTIE EXPLICITE OU IMPLICITE

# This is a simple http flooder to test YOUR server with multiples requests

#  Copyright 2012 Arnaud Alies <mouu@hush.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

from threading import Thread
from urllib import urlopen
from atexit import register
from os import _exit
from sys import stdout, argv

def auto_send_request(server, number_of_requests=10):
	for z in range(number_of_requests):
		try:
			urlopen(server)
			stdout.write(".")
		except IOError:
			stdout.write("E")

def flood(url, number_of_requests = 1000, number_of_threads = 50):
	number_of_requests_per_thread = int(number_of_requests/number_of_threads)
	try:
		for x in range(number_of_threads):
			Thread(target=auto_send_request, args=(url, number_of_requests_per_thread)).start()
	except:
		stdout.write("\n[E]\n")
		clean_exit()
	print("\nDone %i requests on %s" % (number_of_requests, url))

def clean_exit():
	print("\nQuitting...")
	_exit(0)

def main():
	register(clean_exit)
	try:
		server = str(argv[1])
		requests = int(argv[2])
	except IndexError:
		print("You can launch your script using: \npython filename.py http://server/ requests\nexample: python http://localhost/ 10000")
		server = raw_input("Server: ")
		requests = input("N° requests: ")
	flood(server, requests)

if __name__ == '__main__':
	main()
