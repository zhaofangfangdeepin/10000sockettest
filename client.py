#!/usr/bin/env python
# -*- coding=utf-8 -*- 
import socket
import threading
client_list = []
for i in range(1,10000):
    s = socket.socket()
    s.connect(('10.0.12.226', 30000))
    client_list.append(s)
    msg='client %s create success !'%i
    s.send(msg.encode('utf-8'))

def read_from_server(s):
    while True:
        print(s.recv(2048).decode('utf-8'))
        threading.Thread(target=read_from_server, args=(s, )).start()

while True:
    line = input('')
    if line is None or line == 'exit':
        break
    s.send(line.encode('utf-8'))
