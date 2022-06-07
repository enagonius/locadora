from django import template

register = template.Library()

@register.filter
def verbose_name(value):
    return value._meta.verbose_name


@register.filter
def verbose_name_plural(value):
    if not value:
        return ""
    return value[0]._meta.verbose_name_plural


@register.filter
def fields(value):
    return value._meta.get_fields()
