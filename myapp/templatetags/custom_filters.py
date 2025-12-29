from django import template

register = template.Library()

@register.filter(name='currency')
def currency(value):
    return f"${value:.2f}"


@register.filter(name='discount')
def discount(value,percentage): 
    return value - (value *int(percentage)/100 )