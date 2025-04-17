from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import ContactMessage
from .forms import ContactForm
from blog.models import BlogPost
from django.contrib import messages

# portfolio/views.py


class HomeView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"


# class BlogView(TemplateView):
#     template_name = "blog_list.html"

# class BlogPostView(TemplateView):
#     template_name = "blog-post.html"

class CaseStudy1View(TemplateView):
    template_name = "case_study_1.html"


class CaseStudy2View(TemplateView):
    template_name = "case_study_2.html"



class CaseStudy3View(TemplateView):
    template_name = "case_study_3.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_blogs'] = BlogPost.objects.all().order_by('-created_at')[:2]
        return context

class WorkView(TemplateView):
    template_name = "work.html"

class NotFoundView(TemplateView):
    template_name = "404.html"


class ContactView(CreateView):
    model = ContactMessage
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        # Save the form data to the database
        response = super().form_valid(form)
        # Add a success message that SweetAlert2 will display
        messages.success(self.request, 'Proposal received. Our team will get back to you shortly.')
        return response

    
    
