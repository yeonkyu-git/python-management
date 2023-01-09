#!/bin/env python
import socket

def CheckSocket(ip,port):
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_result = tcp_sock.connect_ex((ip,port))

    if tcp_result == 0:
      print("Source IP = ", ip, "Port = ", port, "port is open")
    else:
      print("Source IP = ", ip, "Port = ", port, "port is not open")
    tcp_sock.close()


def readIPAndPortFile():
  f = open("ipandport.txt", 'r')
  while True:
    line = f.readline()
    if not line:
      break
    ip, port = line.split(" ")
    CheckSocket(ip, int(port))
  f.close()


if __name__ == '__main__':
    readIPAndPortFile()