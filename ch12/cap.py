def just_do_it(text):
    # return text.capitalize()    # capitalizes only the first letter of the first word
    # return text.title()           # title() doesn’t handle apostrophes well.
    from string import capwords
    return capwords(text)