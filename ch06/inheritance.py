class Person():
    pass

someone = Person()
print(type(someone))

class Person():
    def __init__(self):
        pass

someone = Person()
print(type(someone))

class Person():
    def __init__(self, name = "Anonymous"):
        self.name = name

John = Person("John Lee")
print(John.name)

class EmailPerson(Person):
    def __init__(self, name = "Anonymous", email = "Anonymous@aaa"):
        super().__init__(name)
        self.email = email

anony = EmailPerson()
print(anony.name)
print(anony.email)
bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name)
print(bob.email)

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
    def need_a_push(self):
        print("A little help here?")

car = Car()
print(car.exclaim())
# print(car.exclaim(car))  # TypeError: exclaim() takes 1 positional argument but 2 were given

