from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogPost, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.decorators import method_decorator




class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['post'] = self.object
        context['recent_posts'] = BlogPost.objects.order_by('-created_at')[:4]
        context['top_level_comments'] = post.comments.filter(parent__isnull=True)
        return context
    

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/blog_detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.post_instance = BlogPost.objects.get(slug=self.kwargs['slug'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.post = self.post_instance
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.post_instance
        context['recent_posts'] = BlogPost.objects.order_by('-created_at')[:4]
        context['top_level_comments'] = self.post_instance.comments.filter(parent__isnull=True)
        context['form'] = self.get_form()  # in case template expects `form` (like {{ form.as_p }})
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


