
#!/bin/usr/python

class Pila:
	def __init__(self):
		self.data=[]

	def is_Empty (self):
		return (len(self.data) <1)

	def pop(self):
		if not self.is_Empty():
			lost = len(self.data)-1
			res = self.data[-1] 
			del self.data[-1]
			return res
		else:
			return self.data

	def push(self, elem):
		self.data.append(elem)
		return len(self.data)



p1=Pila()
p2=Pila()
p1.push(2)
p1.push(33)
p2.push(2)
print (p1.pop()/p2.pop())
