#!/usr/bin/python3

from netaddr import *
import sys
import socket

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
            if ((tmp[2][0]) == arg):
              # resolves to single ip
              excludeips.append(arg)
            else:
              # dns name resolves to multiple ips
              excludeips = tmp[2]
        except:
            print >> sys.stderr, "Exception: %s" % str(e)
            sys.exit(1)


for line in read_stdin():
    line = line.split()
    found = 0
    for excludeip in excludeips:
        if (excludeip != '' and line[0] != ''):
            if IPAddress(excludeip) in IPNetwork(line[0]):
                found = 1
    if (found == 0):
        print(line[0])
