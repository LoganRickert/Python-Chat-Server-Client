#!/usr/bin/env python 

# Python 2

""" 
A simple echo client 
""" 

import socket 

host = 'localhost' 
port = 8080 
size = 1024 

name = raw_input("What do you want your name to be? ")

while 1:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))
	message = name + ": " + raw_input("What would you like to send? ")
	s.send(message)
	data = s.recv(size)
	print(data)
	s.close()