class Nodo:
    
    def __init__(self, dato, nxt):
        self.dato=dato
        self.nxt=nxt

    def buscarmax(self):
        act=self
        mayor=-9999

        while act.nxt != None:
            if act.dato > mayor:
                mayor=act.dato
            act=act.nxt

        if act.dato>mayor:
            mayor=act.dato

        return mayor

    def buscarmin(self):
        act=self
        menor=9999

        while act.nxt != None:
            if act.dato<menor:
                menor=act.dato
            act=act.nxt

        if act.dato<menor:
            menor=act.dato

        return menor


nodo1=Nodo(50,None)
nodo2=Nodo(3,nodo1)
nodo3=Nodo(10,nodo2)
nodo4=Nodo(1,nodo3)

print(nodo4.buscarmax())

print(nodo4.buscarmin())
