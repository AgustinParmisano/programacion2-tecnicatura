class Car:
	def __init__(self,gas):
		self.gas = gas
	def start(self):
		if self.gas >0:
			print ("Car Started")
			return True
		else:
			print("insufficient gas{}".format(self.gas))
			return False
	def drive(self):
		if self.gas > 0:
			print("driving")
			self.gas-=1
			return True
		else:
			print("no gas left")
			return False

a1 = Car(10)
if a1.start():
	while a1.drive():
		print(a1.gas)



