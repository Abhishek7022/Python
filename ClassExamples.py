# Examples for Class, Methods and Objects
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
