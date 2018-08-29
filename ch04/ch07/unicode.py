print(ord('許'))             # code point (decimal)
print(chr(ord('許')))        # takes integers and returns a Unicode string of length 1 

def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value={}, name={}, value2={}'.format(value, name, value2))

unicode_test('許')
unicode_test('\u8a31')

print('caf\u00e9')
print('\N{LATIN CAPITAL LETTER U WITH DIAERESIS}')


print('許'.encode())

print('許'.encode('ascii', 'backslashreplace'))
