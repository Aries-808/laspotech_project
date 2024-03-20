from django import template

register = template.Library()

@register.filter(name='endswith')
def endswith(value, arg):
    """Check if the value ends with the specified substring."""
    return value.endswith(arg)
