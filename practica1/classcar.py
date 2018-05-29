#!/usr/bin/python3
import time

class Car:
    def __init__(self,gas):
        self.gas=gas


    def start (self):
        if self.gas>0:
            print ("car started")
            return True
        else:
            print ("no gas, cammpt start the car")
            return False

    def drive(self):
        if self.gas>0:
            self.gas-=1
            return True
        else:
            print("no gas left")
            return False
a1=Car(11)
if a1.start():
    while a1.drive():
        print(a1.gas)
        time.sleep(1)
a2=Car(0)
if a2.start():
    while a2.drive():
        print(a2.gas)
        time.sleep(1)

