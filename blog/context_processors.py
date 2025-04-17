
from .models import BlogPost

def latest_blogs(request):
    return {
        'latest_blogs': BlogPost.objects.all().order_by('-created_at')[:2]
    }