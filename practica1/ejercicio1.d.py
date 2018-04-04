#!/usr/bin/python3

servicios = {'ssh':22, 'ftp': 21, 'http': 80, 'smtp': 25, 'https': 443, 'apache':8080}

print (sorted(servicios.keys())) 

print ("")

for k, v in servicios.items():
	print(k,":", v)

print ("")


if 'ftp' in servicios:
	print (servicios['ftp']) 

print ("")



for k, v in servicios.items():
	print (("[+] Found vulnerabilities with ​ %s ​ on port %s") % (k, v))
