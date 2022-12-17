from django import template

register = template.Library()

@register.filter
def titlecase_words(string):
    res = [word.title() for word in string.split(' ')]
    return " ".join(res)

@register.filter
def upercase_words(string):
    res = [word.upper() for word in string.split(' ')]
    return " ".join(res)

@register.filter
def lower_words(string):
    res = [word.lower() for word in string.split(' ')]
    return " ".join(res)

@register.filter
def change_words_case(string, arg='t'):
    if arg == ';l':
        res = [word.lower() for word in string.split(' ')]
    elif arg=='u':
        res = [word.upper() for word in string.split(' ')]
    else:
        res = [word.title() for word in string.split(' ')]
    return " ".join(res)