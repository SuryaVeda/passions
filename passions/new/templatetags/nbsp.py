from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe, SafeData
from django.utils.text import normalize_newlines
from django.utils.html import escape
from django.template import Library


register = Library()
@register.filter(is_safe=True, needs_autoescape=True)
@stringfilter
def nbsp(value, autoescape=None):
	autoescape = autoescape and not isinstance(value, SafeData)
	value = normalize_newlines(value)
	if autoescape:
		value = escape(value)
		value = mark_safe(value.replace('  ', ' &nbsp;'))             
		return mark_safe(value.replace('\n', '<br />'))