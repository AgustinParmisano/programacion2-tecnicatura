class Node:
	def __init__(self,data,nxt):
		self.data=data
		self.nxt = nxt

	def last(self):
		act = self
		while act.nxt != None:
			act = act.nxt

		return act

	def first(self):
		return self

	def len(self):
		act = self
		res = 0
		while act.nxt:
			act = act.nxt
			res +=1
		return res
	def alldata(self):
		l = []
		act =self
		while act.nxt:
			l.append(act.data)
			act = act.nxt
		l.append(act.data)
		return (l)

	def __str__(self):
		return str((self.data))

n3 = Node(4,None)
n2 = Node(33,n3)
n1 = Node(25,n2)
n0 = Node(23,n1)

print (n0.last())
print (str(n0.alldata()))
