def get_description(): # see the docstring below?
    """Return random weather, just like the pros"""
    from random import choice    # within a function and know that nothing else named choice is here
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)