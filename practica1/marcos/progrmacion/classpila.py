class Pila:
	def __init__(self):
		self.data=[]

	def is_empty(self):
		return (len(self.data)<1)

	def pop(self):
		if not self.is_empty():
			return (self.data.pop())
		return False

	def push(self,elem):
		self.data.append(elem)
		return len(self.data)

	def top(self):
		if not self.is_empty():
			return self.data[-1]
		return False

	def __str__(self):
		return self.data

pila1 = Pila()
pila2 = Pila()
pila1.push(8)
pila1.push(10)
pila2.push(2)
print (pila1.top()/pila2.top())


