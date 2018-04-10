#!/usr/bin/python3

list = []

camp=input("ingrese puerto: ")
while camp!=0000:
	if camp!=0000:
		list.append(camp)
	camp=input("ingrese puerto: ")

print(list)
list.sort()
print(list)

<<<<<<< HEAD
if 80 in list:
	print(list.index(80))
=======
print(list.index(80))
list.remove(443)
print (list )
print(len(list))
list.insert(0,8100)
print(list)


>>>>>>> d43e9190d31fae7db49b1b1c8f62dc13c9cb5412
