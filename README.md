# cidr_exclude
Exclude an IP address or DNS name from a stdin CIDR list, e.g. as extra whitelisting for ipset-blacklist

Doesn't accept a CIDR as argument, yet - just use the network address instead

Syntax: accepts multiple arguments, dns name or ip address

Example:
* cat /tmp/tmp.Nm40laAgjP | ./cidr_exclude.py 23.22.181.230 52.1.126.80
* cat /tmp/tmp.Nm40laAgjP | ./cidr_exclude.py www.telenet.be
