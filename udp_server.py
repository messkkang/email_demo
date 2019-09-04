#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket

# 创建套接字对象 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(("0.0.0.0", 9999))  # 绑定地址，即确定自己的通信地址

# 0.0.0.0 表示本机任意IP
# 127.x.x.x 表示本机IP，只能用于本机上的不同进程间通信

while True:
    # msg = sock.recv(1024)  # 接收一条消息
    msg, addr = sock.recvfrom(1024)
    print(addr, msg.decode())
    sock.sendto("你是傻子！".encode(), addr)  # 发送消息

# sock.sendto("邓君", ("192.168.8.111", 9999))  # 发送消息