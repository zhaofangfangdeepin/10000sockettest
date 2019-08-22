#!/usr/bin/env python
# -*- coding=utf-8 -*-

import socket
import threading

socket_list = []
ss = socket.socket()
ss.bind(('10.0.12.226', 30000))
ss.listen(10000)

def read_from_client(s):
    try:
        return s.recv(2048).decode('utf-8')
    except:
        socket_list.remove(s);

def server_target(s):
    try:    
        while True:
            content = read_from_client(s)
            print(content)
            if content is None:
                break
            for client_s in socket_list:
                client_s.send(content.encode('utf-8'))
    except e:
        print(e.strerror)

while True:
    s, addr = ss.accept()
    socket_list.append(s)
    threading.Thread(target=server_target, args=(s, )).start()
