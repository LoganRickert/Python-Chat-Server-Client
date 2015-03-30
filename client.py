#!/usr/bin/env python 

# Python 2

""" 
A simple echo client 
""" 

import socket 

host = 'localhost' 
port = 8080 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = raw_input("What do you want your name to be? ")
s.connect((host,port))
s.send(name + ": " + raw_input("What would you like to send? "))
data = s.recv(size) 
s.close() 
print(data)