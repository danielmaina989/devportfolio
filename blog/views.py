from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import BlogPost, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.db.models import Prefetch
from django.views.generic.edit import FormMixin



class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'


class BlogDetailView(FormMixin, DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        context.update({
            'top_level_comments': post.comments.filter(parent__isnull=True)
                                               .prefetch_related(Prefetch('replies', queryset=Comment.objects.order_by('created_at'))),
            'recent_posts': BlogPost.objects.order_by('-created_at')[:4],
        })
        
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Important to call it here
        form = self.get_form()
        if form.is_valid():
            if self.request.POST.get('honeypot'):
                return self.form_invalid(form)
            form.instance.post = self.object
            if self.request.user.is_authenticated:
                form.instance.user = self.request.user
            form.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/blog_detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(BlogPost, slug=self.kwargs['slug'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if self.request.POST.get('honeypot'):
            return self.form_invalid(form)
        form.instance.post = self.post_instance
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.post_instance
        context['recent_posts'] = BlogPost.objects.order_by('-created_at')[:4]
        context['top_level_comments'] = self.post_instance.comments.filter(parent__isnull=True)
        return context

    def get_success_url(self):
        return self.post_instance.get_absolute_url()



class ReplyCommentView(LoginRequiredMixin, View):
    def post(self, request, comment_id):
        parent_comment = get_object_or_404(Comment, id=comment_id)

        if request.user.is_superuser:
            body = request.POST.get('body')
            if body:
                Comment.objects.create(
                    post=parent_comment.post,
                    parent=parent_comment,
                    name=request.user.username,
                    email=request.user.email,
                    body=body,
                    is_admin=True,
                )

                messages.success(request, "Reply posted successfully.")

        return redirect('blog:blog_detail', slug=parent_comment.post.slug)
    


    

