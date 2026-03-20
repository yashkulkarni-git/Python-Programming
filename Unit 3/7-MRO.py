# Use appropriate functions for each classWrite a program to display MRO using multiple inheritance. Multiple inheritance can be done as per your choice. 

class A:
    def showA(self):
        print("Class A Method")

class B:
    def showB(self):
        print("Class B Method")

class C(A, B):
    def showC(self):
        print("Class C Method")

obj = C()

obj.showA()
obj.showB()
obj.showC()

print("Method Resolution Order:")
print(C.__mro__)