from django.shortcuts import render
from django.views.generic import TemplateView

# portfolio/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"

class BlogView(TemplateView):
    template_name = "blog.html"

class BlogPostView(TemplateView):
    template_name = "blog-post.html"

class CaseStudy1View(TemplateView):
    template_name = "case-study-1.html"

class CaseStudy2View(TemplateView):
    template_name = "case-study-2.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class WorkView(TemplateView):
    template_name = "work.html"


class NotFoundView(TemplateView):
    template_name = "404.html"
