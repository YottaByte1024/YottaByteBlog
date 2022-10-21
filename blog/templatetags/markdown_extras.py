from django import template
from django.template.defaultfilters import stringfilter

import markdown2 as md
import re

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(
        value,
        # extensions=['markdown.extensions.fenced_code']
        extras=['tables', 'fenced-code-blocks', 'strike', 'spoiler', 'wiki-tables']
    )

@register.filter()
@stringfilter
def replace_a(str):
    r1 = '\<a'
    r2 = 'a\>'
    r3 = '\>'
    str = re.sub(r1,'<i', str)
    str = re.sub(r2, 'i>', str)
    # str = re.sub(r3, '\\>', str)
    return str