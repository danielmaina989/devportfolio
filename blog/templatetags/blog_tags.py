# blog/templatetags/blog_tags.py

from django import template
from blog.models import BlogPost

register = template.Library()

@register.inclusion_tag('partials/latest_blog_footer.html')
def latest_blog_footer():
    latest = BlogPost.objects.order_by('-created_at')[:2]
    return {'latest_blogs': latest}
