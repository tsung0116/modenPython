def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result in document_it:', result)
        return result
    return new_function

def add_ints(a, b):
    return a + b

# print('Add ints', add_ints(3, 5))

cooler_add_ints = document_it(add_ints) # manual decorator assignment
ans = cooler_add_ints(3,5)
print('Result of add ints:', ans)

@document_it
def multi_ints(a, b):
    return a * b

b = multi_ints(3, 6)
print('Result of multi ints:', b)

def square_it(func):
    def new_function2(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function2

@document_it
@square_it
def add_ints2(a, b):
    return a + b

c = add_ints2(3, 6)
print('Add and then square', c)