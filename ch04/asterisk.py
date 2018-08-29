# Gather Positional Arguments with *
def print_args(*args):
    print('Positional argument tuple:', args)

print_args()
print_args(3, 2, 1, 'wait!', 'uh...')

#If your function has required positional arguments as well, *args goes at the end and grabs all the rest
def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

# You can have keyword only arguments after the *args
def foo(arg, kwarg=None, *args, kwarg2=None, **kwargs): 
    print(arg, kwarg, args, kwarg2, kwargs)

foo(1,2,3,4,5,kwarg2='kwarg2', bar='bar', baz='baz')

# * can be used by itself to indicate that keyword only arguments follow, without allowing for unlimited positional arguments.
def boo(arg, kwarg=None, *, kwarg2=None, **kwargs): 
    print(arg, kwarg, kwarg2, kwargs)

boo(1,2,kwarg2='kwarg2', foo='foo', bar='bar')


# Gather Keyword Arguments with **
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')


#          | In function *construction*     | In function *call*
#=======================================================================
#          |  def f(*args):                 |  def f(a, b):
# *args    |      for arg in args:          |      return a + b
#          |          print(arg)            |  args = (1, 2)
#          |  f(1, 2)                       |  f(*args)
#----------|--------------------------------|---------------------------
#          |  def f(a, b):                  |  def f(a, b):
# **kwargs |      return a + b              |      return a + b
#          |  def g(**kwargs):              |  kwargs = dict(a=1, b=2)
#          |      return f(**kwargs)        |  f(**kwargs)
#          |  g(a=1, b=2)                   |
#-----------------------------------------------------------------------
