def sliceloco(string,div):
	pos = ""

	for i in range(0,len(string),div):
		string2 = []
		sitrng2 = string2.insert(string[i:i+div])
		print (string2)

l = "re loco estoy aca en el instituto"

sliceloco(l,3)



