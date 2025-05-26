# blog/templatetags/blog_tags.py

from django import template
from blog.models import BlogPost
from django import template
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django import template
from django.utils.html import escape


register = template.Library()

@register.inclusion_tag('partials/latest_blog_footer.html')
def latest_blog_footer():
    latest = BlogPost.objects.order_by('-created_at')[:2]
    return {'latest_blogs': latest}


@register.filter
def excerpt(content, word_count=30):
    plain_text = strip_tags(content)
    return Truncator(plain_text).words(word_count, truncate='...')



@register.simple_tag(takes_context=True)
def absolute_url(context, relative_url):
    request = context['request']
    return request.build_absolute_uri(relative_url)


