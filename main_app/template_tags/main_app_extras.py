
from django import template


register = template.Library()

@register.simple_tag
def to_string(text):

    return str(text)