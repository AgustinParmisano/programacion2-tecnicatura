def connect(**kwargs):
	if "ip" and "port" in kwargs:
		print("Trying to connect to {} for port {}".format(kwargs["ip"],kwargs["port"]))

connect(ip="192.168.1.1",port=8000)		
