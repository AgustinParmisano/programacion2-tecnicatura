#!/usr/bin/python

class Node:

	def __init__(self,data,nxt):
		self.data=data
		self.nxt=nxt

	def last(self):
		act=self
		while act.nxt !=None:
			act=act.nxt
		return act

	def first(self):

             return self

        def len(self):
		act=self
        	res=0
		while act.nxt:
                 	act=act.nxt 
		return res

	def alldata(self):
		li=[]
		act=self
		while act.nxt:
			li.append(act.data)
			act=act.nxt
		li.append(act.data)
		return (li) 











n3 = Node(4,None)
n2 = Node(33,n3)
n1 = Node(25,n2)
n0 = Node(23,n1)
print (n0.last().data)
print (str(n0.alldata()))

	
