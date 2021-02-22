class Animal:
        def Info(self):
            print("This is animal class")
        def Move(self,m):
            pass 

class Dog(Animal):
    def Move(self,m):
          print("I have",m,"legs.I can run")

class Crow(Animal):
    def Move(self,m):
          print("I have",m,"legs.I can fly")

obj1=Dog()
obj1.Move(4)
obj2=Crow()
obj2.Move(2)

        