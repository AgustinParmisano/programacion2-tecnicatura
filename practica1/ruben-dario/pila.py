class Pila:
	def __init__(self):
		self.elementos=[]

	def push (self, elemento):
		self.elementos.append(elemento)

	def isEmpty (self):
		return (self.elementos == [])

	def pop(self):
		if not self.isEmpty():
			return self.elementos.pop()

p1=Pila()
p2=Pila()
p1.push(2)
p1.push(33)
print (p1.pop())
