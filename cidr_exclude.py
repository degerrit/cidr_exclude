#!/usr/bin/python3

from netaddr import *
import pprint
import fileinput, sys
import socket, struct

def read_stdin():
    readline = sys.stdin.readline()
    while readline:
        yield readline
        readline = sys.stdin.readline()

# replace any dns names with ip addresses
excludeips = []
for arg in sys.argv:
    if (sys.argv[0] != arg):
        try:
            tmp=socket.gethostbyname_ex(arg)
            # print (tmp)
            excludeips = tmp[2]
        except:
            excludeips.append(arg)

for line in read_stdin():
    line = line.split()
    for excludeip in excludeips:
        if (excludeip != '' and line[0] != ''):
            if IPAddress(excludeip) in IPNetwork(line[0]):
                found = 1
                break
            else:
                found = 0

    if (found == 0):
        print(line[0])
