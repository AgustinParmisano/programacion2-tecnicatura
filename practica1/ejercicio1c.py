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

print(list.index(80))
list.remove(443)
print (list )
print(len(list))
list.insert(0,8100)
print(list)


