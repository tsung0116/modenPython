from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')   # collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
print(Duck.__bases__)                    # a factory function for creating tuple subclasses with named fields

print(type(Duck))                        # All of the classes are instances of type.  Duck is also an instance of type. 
print(Duck.__class__.__mro__)            # Note: type is a subclass of object. MRO: method resolution order
                                         
                                       
duck = Duck('wide orange', 'long')      
print(type(duck))
print(duck.__class__.__mro__)
print(duck.bill)
print(duck.tail)

parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
print(duck2)