# portfolio/urls.py
from django.urls import path
from .views import HomeView, AboutView, BlogView, BlogPostView, CaseStudy1View, CaseStudy2View, ContactView, WorkView, NotFoundView


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogPostView.as_view(), name='blog-post'),
    path('case-study-1/', CaseStudy1View.as_view(), name='case-study-1'),
    path('case-study-2/', CaseStudy2View.as_view(), name='case-study-2'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('work/', WorkView.as_view(), name='work'),
    path('404/', NotFoundView.as_view(), name='404'),
]
