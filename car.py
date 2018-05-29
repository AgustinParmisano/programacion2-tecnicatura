#!/usr/bin/python
import time

class Car:

	def __init__(self,gas):
		self.gas = gas
	def start(self):
		if self.gas > 0:
			print ("car started")
			return True
		else:
			print ("insuficien gas {}".format(self.gas))
			return False
	def drive(self):
		if self.gas > 0:
			print ("driving")
	   		self.gas -=1
	   		return True
		else:
			print ("no gas sert")
			return False

a1 = Car(5)
if a1.start():
	while a1.drive():
		print (a1.gas)
		time.sleep(1)

