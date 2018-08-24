# inner function

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

print(knights('Ni!'))


# closure

def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')

print(type(a))
print(type(b))

print(a)
print(b)

print(a())
print(b())

# Anonymous Functions: the lambda() Function

def edit_story(words, func):
    for word in words:
        print(func(word))

def enliven(word): # give that prose more punch
    return word.capitalize() + '!'

stairs = ['thud', 'meow', 'thud', 'hiss']

edit_story(stairs, enliven)

edit_story(stairs, lambda word: word.capitalize() + '!')