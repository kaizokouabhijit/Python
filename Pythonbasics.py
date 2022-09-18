

class Test:
    x = 5
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def myfunc(self):
        return self.x + 5
        

p1 = Test("Abhijit", 26)

del p1.age

print(p1.name +" "+" "+  str(p1.x))
print(p1.myfunc())

# print(p1.age)



