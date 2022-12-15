from django import template

register = template.Library()


@register.simple_tag
def get_obj_by_pk(obj, pk):
    try:
        return

    except:
        return 'Error'
