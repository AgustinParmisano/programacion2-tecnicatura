class Cola:
        def __init__(self):
                self.data=[]

        def is_empty(self):
                return (len(self.data)<1)

        def pop(self):
                if not self.is_empty():
                        return (self.data.pop())
                return False

        def push(self,elem):
                self.data.insert(0,elem)
                return len(self.data)

        def top(self):
                if not self.is_empty():
                        return self.data[-1]
                return False

        def __str__(self):
                return self.data

cola1 = Cola()
cola2 = Cola()
cola1.push(8)
cola1.push(10)
cola2.push(2)
print (cola1.top()/cola2.top())

