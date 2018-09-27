import logging

def use_logging(func):

    def wrapper():
        logging.warning("%s is running" % func.__name__)
        return func()   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper

def foo():
    print('i am foo')

foo = use_logging(foo)  # 因为装饰器 use_logging(foo) 返回的时函数对象 wrapper，这条语句相当于  foo = wrapper
foo()                   # 执行foo()就相当于执行 wrapper()

@use_logging
def foo():
    print("i am foo")

foo()


def use_logging(func):

    def wrapper(*args, **kwargs):
        logging.warning("%s is running" % func.__name__)
        return func(*args, **kwargs)   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper

@use_logging
def foo(name, age=None, height=None):
    print("I am %s, age %s, height %s" % (name, age, height))

foo("foo", age=18, height=178)



def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warning":
                logging.warning("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

@use_logging(level="warning")
def foo(name='foo'):
    print("i am %s" % name)

foo()

def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__)               # 输出 'fmath'
        print(func.__doc__)                # 输出 'does some math'
        return func(*args, **kwargs)
    return with_logging

# 函数
@logged
def fmath(x):
   """does some math"""
   return x + x * x

print(fmath(3))
print(fmath.__name__)              # 输出 'with_logging'
print(fmath.__doc__)               # 输出 None



from functools import wraps

def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__)      # 输出 'fmath'
        print(func.__doc__)       # 输出 'does some math'
        return func(*args, **kwargs)
    return with_logging

@logged
def fmath(x):
   """does some math"""
   return x + x * x

print(fmath(3))

print(fmath.__name__)              # 输出 'fmath'
print(fmath.__doc__)               # 输出 'does some math'