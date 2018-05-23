empty = "192.168.0."
iplist = []

for i in range(1,255):

	iplist.append(empty+str(i))
	print(iplist)

servicios = {'ftp':21,'ssh':22,'smtp':25,'http':8080,'?':8100}

list_servicios = list(servicios.values())

print(list_servicios)
