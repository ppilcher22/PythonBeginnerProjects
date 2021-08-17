class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Child(Person):
    def __init__(self, name, age, mother, father):
        super().__init__(name, age)
        self.mother = mother
        self.father = father


pers1 = Person('Homer', 33)
kid = Child('Charlie', 7, 'Mum', 'Papa')
print(pers1.name)

print(kid.father, kid.name)