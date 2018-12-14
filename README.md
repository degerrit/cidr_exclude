# cidr_exclude
exclude an IP address or dns name from a stdin CIDR list, e.g. as extra whitelisting for ipset-blacklist

Syntax: accepts multiple arguments, dns name or ip address

Example:
* cat /tmp/tmp.Nm40laAgjP | ./cidr_exclude.py 23.22.181.230 52.1.126.80
* cat /tmp/tmp.Nm40laAgjP | ./cidr_exclude.py www.telenet.be
