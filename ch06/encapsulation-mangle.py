class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

duck = Duck("Ugly")
ug_duck_name = duck.name
duck.name = "Goose"
# ug_duck_name = duck.__name     # AttributeError: 'Duck' object has no attribute '__name'
duck.__name = "Gooooose"         # A new attribute is created 
print(duck.name)
print(duck._Duck__name)         # "inside the getter" won't be printed
print(duck.__name)

