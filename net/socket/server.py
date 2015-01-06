#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

host = ""
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) // 创建一个TCP连接
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  // 把socket设置成可复用的
s.bind((host, port)) // 绑定IP和端口
s.listen(1)  // 开始监听

print "Server is running on port %d; press Ctrl-C to terminate." % port

while 1:
    clientsock, clientaddr =  s.accept()  // 连接到一个客户端后，程序会停止， 返回两个信息
    clientfile = clientsock.makefile('rw', 0)
    clientfile.write("Welcome, " + str(clientaddr) + "\n")
    clientfile.write("Please enter a string: ")
    line = clientfile.readline().strip()
    clientfile.write("You entered %d characters.\n" % len(line))
    clientfile.close()
    clientsock.close()

