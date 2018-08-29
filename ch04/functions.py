def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

# Positional Arguments
menu1 = menu('chardonnay', 'chicken', 'cake')
print(menu1)


# Keyword Arguments
menu2 = menu(entree='beef', dessert='bagel', wine='bordeaux')
print(menu2)

# mix positional and keyword arguments
# If you call a function with both positional and keyword arguments, the positional arguments need to come first.
menu3 = menu('frontenac', dessert='flan', entree='fish')
print(menu3)

# Specify Default Parameter Values
# Default argument values are calculated when the function is defined
def menu_d(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu4 = menu_d('chardonnay', 'chicken')
print(menu4)

# Since every function is an object, varibles inside a function are attributes  
def buggy(arg, result=[]):  
    print(result)          # 'result' is empty only the first time it’s called.
    result.append(arg)
    print(result)

buggy('a')
buggy('b')  # expect ['b'], but output ['a', 'b']

def works(arg):
    result = []
    result.append(arg)
    print(result)

works('a')
works('b')

def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

nonbuggy('a')
nonbuggy('b')