from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def is_user(context):
    request = context['request']
    if not request.user.is_authenticated:
        return False
    return request.user
