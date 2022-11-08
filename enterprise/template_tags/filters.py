from django import template

register = template.Library()

@register.filter(name='is_even')
def is_even(value):
    return True if value % 2 == 0 else False