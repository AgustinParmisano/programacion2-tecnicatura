import datetime

class Persona:
    def __init__(self,nom,ape,dni,cta):
        self.nombre= nom
        self.apellido= ape
        self.dni= dni
        self.cuenta= cta
    
    def depositar(self,monto):
        total= self.cuenta.depositar(monto)
        print('La cuenta de dni: {0} tiene saldo: ${1}'.format(self.dni,total))

    def retirar(self,monto):
        total= self.cuenta.retirar(monto)
        if (total != False):
            print('La cuenta de dni: {0} tiene saldo: ${1}'.format(self.dni,total))

    
class Cuenta:
    def __init__(self,tipo,monto,iva):
        self.tipo= tipo
        self.monto= monto
        self.iva= iva
    
    def depositar(self,monto):
        self.monto+= monto
        return self.monto

    def retirar(self,monto):
        if (monto <= (self.monto - self.iva)):
            self.monto-= (monto + self.iva)
            return self.monto
        else:
            print('El monto que quiere retirar supera su saldo')
            return False

cta1= Cuenta('caja de ahorro',1000,10)
cta2= Cuenta('cuenta corriente',0,5)
cta3= Cuenta('cuenta corriente',300,5)
mauro = Persona('Mauro','Francois',28345623,cta1)
marcos = Persona('Marcos','Di Lauro',31135536,cta2)
fran = Persona('Francisco Javier','Landivar',30568522,cta3)

mauro.depositar(500)
marcos.depositar(2000)
fran.depositar(1500)
mauro.retirar(300)
marcos.retirar(2000)
fran.retirar(1000)
