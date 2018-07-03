class Perro:
	def __init__(self,n):
		self.nombre = n
	def nombre(self):
		a = str(self.nombre)
		print (a)
	def hacer(self,caca):
		print (caca * ("plouch"))
p1 = Perro("artemis")

a = p1.nombre

print (a)

p1.hacer(2)
