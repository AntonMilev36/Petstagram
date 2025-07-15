from django import template

register = template.Library()

@register.filter
def placeholder(value, plh_text):
    value.field.widget.attrs['placeholder'] = plh_text
    return value
