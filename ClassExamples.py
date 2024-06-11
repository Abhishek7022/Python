# Examples for Class, Methods and Objects

# Write a class method having details of a person:
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        print(f'Greetings {self.name}!')
        print(f'Your age is {self.age}')

    def get_gender(self):
        print(f'Your gender is {self.gender}')

p1 = Person('Jamvant', 25, 'Male')
p1.get_details()
p1.get_gender()


# Write a class method to print distance and slope of a given line:
class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2-y1)/(x2-x1)

li = Line((3,2), (8,10))
print(li.slope())
print(li.distance())


# Write a class method to print the volume and surface area of a cylinder:
class Cylinder:

    pi = 3.14

    def __init__(self, radius, height):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi*(self.radius**2)*self.height

    def surface_area(self):
        return 2*Cylinder.pi*self.radius*self.height + 2*Cylinder.pi*(self.radius**2)

c = Cylinder(3, 2)
print(c.volume())
print(c.surface_area())


# Write a class method to print class attributes and bank deposit and withdrawal:
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, damount):
        self.balance = self.balance + damount
        print(f'Amount deposited: ${damount} accepted!')

    def withdraw(self, wamount):
        if self.balance < wamount:
            print('Insufficient funds! Transaction denied!')
        else:
            self.balance = self.balance - wamount
            print(f'Amount withdrawn: ${wamount} accepted!')

    def __str__(self):
        return f"Owner is: {self.owner}\nBalance is: {self.balance}"

a = Account('Sugreev', 500)
str(a.owner)
a.deposit(400)
a.withdraw(800)
a.withdraw(500)
print(a)